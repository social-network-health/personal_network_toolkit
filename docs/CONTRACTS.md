# M0 Data Contracts

This document defines the first-pass contracts between the toolkit components.
The contracts are intentionally small enough to implement quickly and rich enough
to avoid painting the project into a contact-schema corner.

M0 has three central contracts:

1. **Normalized contact bundle**: importer output.
2. **Directory SQLite schema**: local viewer/search database.
3. **Directory export bundle**: filtered result set for HTML, PDF, and later
   notification tools.

## Contact Schema Rationale

The contact schema is influenced by three prior inputs:

- Google People/Contacts, whose `Person` resource has many repeated fields such
  as `names`, `emailAddresses`, `phoneNumbers`, `addresses`, `organizations`,
  `photos`, `urls`, `relations`, `events`, and `userDefined`.
- PRT, which kept a compact `contacts` table with name, email, phone, profile
  image metadata, and a separate private relationship layer for tags and notes.
- `fellows_local_db`, which proved that fixed display/search columns plus
  `extra_json` overflow works well for fast directory viewing without losing
  source-specific fields.

The M0 decision is not to create a complete superset of every known contact
provider. That usually turns into a large brittle schema and still misses fields.
Instead:

- Keep a compact canonical contact row for fast display, search, and filtering.
- Preserve repeated/provider-specific fields as JSON.
- Keep source aliases so contacts can survive re-imports without losing private
  relationship metadata.
- Keep imported facts read-only; write local corrections, tags, and notes in
  separate overlay/relationship tables.

## Imported Facts And Local Overlays

The toolkit distinguishes imported contact facts from user-owned local data.

- **Imported contact facts** come from Google, Apple, Facebook, LinkedIn,
  bespoke directories, CSV files, or another source. These rows are rebuildable
  and may be overwritten on re-import.
- **Contact overlays** are local user-entered corrections or supplements that
  are safe to show in normal directory/export contexts. Examples include a
  missing email address, preferred phone number, better display name, location,
  organization, role/title, or a short non-sensitive contact note.
- **Private relationship notes** are sensitive local context. They are useful for
  search, memory, and relationship management, but are not included in directory
  exports by default.
- **Tags** are local labels attached to contacts. They are implemented as a real
  table from v0 so filtered views can be named, searched, and reconstructed
  deterministically.

This preserves the "do not modify imported contact data" rule while still making
the toolkit practical for incomplete Google Contacts or old directory imports.
The viewer should work with an effective contact assembled from imported facts
plus contact overlays.

## Normalized Contact Bundle

Importers produce a bundle directory or JSON document with this logical shape:

```json
{
  "schema_version": "pnt.contacts.v0",
  "generated_at": "2026-04-21T00:00:00Z",
  "source": {
    "type": "google_takeout",
    "name": "Google Takeout Contacts",
    "exported_at": null
  },
  "contacts": [
    {
      "source_id": "people/c123",
      "display_name": "Alice Johnson",
      "given_name": "Alice",
      "family_name": "Johnson",
      "primary_email": "alice@example.com",
      "primary_phone": "+1-555-0104",
      "primary_location": "Auckland, New Zealand",
      "primary_organization": "Example Co",
      "title": "Product Lead",
      "notes_public": "Imported bio or public note.",
      "emails": [
        {"value": "alice@example.com", "type": "home", "primary": true}
      ],
      "phones": [
        {"value": "+1-555-0104", "type": "mobile", "primary": true}
      ],
      "addresses": [],
      "organizations": [],
      "urls": [],
      "important_dates": [],
      "relations": [],
      "image": {
        "path": "images/alice-johnson.jpg",
        "mime_type": "image/jpeg",
        "source_filename": "Alice Johnson.jpg"
      },
      "extra_json": {},
      "raw_source_json": {}
    }
  ]
}
```

### Canonical Contact Fields

These fields are expected by the first database importer and viewer:

| Field | Type | Required | Notes |
| --- | --- | --- | --- |
| `source_id` | string/null | No | Stable ID from the source when available. |
| `display_name` | string | Yes | Viewer label; importer should synthesize if needed. |
| `given_name` | string/null | No | Search/display helper. |
| `family_name` | string/null | No | Search/display helper. |
| `primary_email` | string/null | No | Initial high-value contact method/filter. |
| `primary_phone` | string/null | No | Useful secondary contact method. |
| `primary_location` | string/null | No | Free-text location for v0. |
| `primary_organization` | string/null | No | Company/group/org label. |
| `title` | string/null | No | Role/title/headline. |
| `notes_public` | string/null | No | Imported bio/tagline/public note, not private notes. |
| `image.path` | string/null | No | Relative path inside the bundle when an image exists. |
| `extra_json` | object | No | Normalized but non-canonical fields. |
| `raw_source_json` | object | No | Original source object when safe and useful. |

### Repeated Fields

Repeated data should be normalized into arrays when practical:

- `emails`
- `phones`
- `addresses`
- `organizations`
- `urls`
- `important_dates`
- `relations`

Each array item may keep provider-specific keys if needed. The viewer does not
need to understand every repeated field in v0, but export tools should preserve
them.

## Directory SQLite Schema

The v0 SQLite database favors simple raw SQLite over an ORM.

```sql
CREATE TABLE contacts (
    contact_id TEXT PRIMARY KEY,
    slug TEXT NOT NULL,
    display_name TEXT NOT NULL,
    given_name TEXT,
    family_name TEXT,
    primary_email TEXT,
    primary_phone TEXT,
    primary_location TEXT,
    primary_organization TEXT,
    title TEXT,
    notes_public TEXT,
    image_path TEXT,
    image_mime_type TEXT,
    image_source_filename TEXT,
    source_type TEXT,
    source_name TEXT,
    extra_json TEXT,
    raw_source_json TEXT,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);

CREATE UNIQUE INDEX idx_contacts_slug ON contacts(slug);
CREATE INDEX idx_contacts_display_name ON contacts(display_name);
CREATE INDEX idx_contacts_primary_email ON contacts(primary_email);

CREATE TABLE contact_aliases (
    source_type TEXT NOT NULL,
    source_id TEXT NOT NULL,
    contact_id TEXT NOT NULL,
    created_at TEXT NOT NULL,
    PRIMARY KEY (source_type, source_id),
    FOREIGN KEY (contact_id) REFERENCES contacts(contact_id) ON DELETE CASCADE
);

CREATE VIRTUAL TABLE contacts_fts USING fts5(
    display_name,
    given_name,
    family_name,
    primary_email,
    primary_phone,
    primary_location,
    primary_organization,
    title,
    notes_public,
    content='contacts',
    content_rowid='rowid'
);
```

`raw_source_json` is stored by default in v0. It preserves provider-specific
data while importer behavior is still evolving. Later privacy modes may allow
users to disable raw source retention for sensitive imports.

Profile images should ultimately live as files referenced by `image_path`. Some
importers may use an intermediate binary blob while parsing source archives, but
the directory database and export bundle should prefer file paths.

### Stable Identity

`contact_id` is a toolkit-generated UUID or similarly stable opaque ID. It is
not the Google resource name, email address, or slug.

Importers should resolve an incoming contact to an existing `contact_id` using:

1. `(source_type, source_id)` in `contact_aliases`.
2. Normalized primary email, when unambiguous.
3. A conservative fallback such as normalized name plus phone.
4. New generated ID.

This preserves private tags and notes across re-imports.

## Contact Overlays And Private Relationship Layer

Contact overlays and relationship metadata are writable local data. They are not
part of imported contact facts.

Contact overlays are exportable by default because they represent the user's
local correction or supplement to the visible contact record.

```sql
CREATE TABLE contact_overlays (
    contact_id TEXT PRIMARY KEY,
    display_name_override TEXT,
    primary_email_override TEXT,
    primary_phone_override TEXT,
    primary_location_override TEXT,
    primary_organization_override TEXT,
    title_override TEXT,
    contact_note TEXT,
    updated_at TEXT NOT NULL,
    FOREIGN KEY (contact_id) REFERENCES contacts(contact_id) ON DELETE CASCADE
);
```

Tags are attached to contacts from v0. A filtered view may be represented by a
combination of tags and filters, such as `#work #pickleball has:email`.
That kind of filter string can later become a deterministic search/filter DSL.

```sql
CREATE TABLE tags (
    tag_id TEXT PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);

CREATE TABLE contact_tags (
    contact_id TEXT NOT NULL,
    tag_id TEXT NOT NULL,
    created_at TEXT NOT NULL,
    PRIMARY KEY (contact_id, tag_id),
    FOREIGN KEY (contact_id) REFERENCES contacts(contact_id) ON DELETE CASCADE,
    FOREIGN KEY (tag_id) REFERENCES tags(tag_id) ON DELETE CASCADE
);

CREATE TABLE saved_networks (
    network_id TEXT PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    query_string TEXT NOT NULL,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);

CREATE TABLE private_notes (
    note_id TEXT PRIMARY KEY,
    contact_id TEXT NOT NULL,
    title TEXT,
    body TEXT NOT NULL,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    FOREIGN KEY (contact_id) REFERENCES contacts(contact_id) ON DELETE CASCADE
);
```

This is simpler than PRT's current relationship-type model. Typed
contact-to-contact relationships can be added later.

Private notes are never included in normal directory exports. A future explicit
"include private notes" export mode could exist for personal backups, but not
for shareable directories, websites, PDFs, or notifier input.

Tags are not exported as contact metadata by default. They may influence the
filtered result set and the default network/export name, but the export should
not expose the tag list for each contact unless a later explicit option is
added.

Saved networks store reusable search/filter strings. The app may auto-generate a
network name from the full search context, including tags, filters, and bare text
terms. For example, `#work #pickleball has:email` could become
`work_pickleball_hasemail`. The user should be able to rename the network when
saving or exporting it.

If an export filename or network name includes tag/filter information, the UI
should show a dismissible warning the first time:

```text
This export name includes tag/filter terms from your search. Rename it before
exporting if that reveals more than you want.
```

## Viewer Record Shapes

The first viewer should have at least two record shapes:

- **Compact view**: name, primary contact information, maybe location, and tags.
  This is the normal high-speed browsing/search result view.
- **Full record view**: all imported canonical fields, repeated provider fields,
  `extra_json`, raw/source-specific fields when retained, contact overlay data,
  tags, and private notes.

Provider-specific repeated data belongs in the full record view by default. The
compact view should stay quiet and useful.

Full record view should render provider-specific data in a human-friendly form
whenever possible. Raw JSON is the fallback when a field cannot be rendered
clearly yet.

## Search DSL v0

The first search/filter DSL should be familiar and small, roughly inspired by
Google-style search:

- bare words search text fields
- quoted phrases search exact-ish phrases where supported
- `#tag` filters by tag
- `has:email` filters to contacts with an effective email address
- `has:phone` filters to contacts with an effective phone number
- `has:image` filters to contacts with an image
- default operator is `AND`
- explicit `OR` can combine terms or filters

Examples:

```text
#work #pickleball has:email
"Auckland" OR "Wellington"
#family has:image
```

The DSL should compile into an inspectable structured query before execution, so
future natural-language search can translate into the same representation.
Saved networks store the DSL string, not the compiled structured query. This
keeps saved data easier for the user to inspect and avoids storing hidden query
context that may expose more than the visible search string.

## Directory Export Bundle

Exports represent a filtered result set. They are the bridge to static HTML,
PDF, and later notifier tools.

Candidate layout:

```text
directory.json
manifest.json
images/
README.md
```

### `manifest.json`

```json
{
  "schema_version": "pnt.directory_export.v0",
  "created_at": "2026-04-21T00:00:00Z",
  "generator": "pnt-export",
  "source_database": "contacts.db",
  "result_count": 2,
  "query": {
    "text": "family",
    "filters": [
      {"field": "tag", "op": "equals", "value": "family"},
      {"field": "primary_email", "op": "present", "value": true}
    ]
  }
}
```

### `directory.json`

```json
{
  "schema_version": "pnt.directory.v0",
  "contacts": [
    {
      "contact_id": "018f5c2f-0000-7000-9000-example",
      "slug": "alice-johnson",
      "display_name": "Alice Johnson",
      "primary_email": "alice@example.com",
      "primary_phone": "+1-555-0104",
      "primary_location": "Auckland, New Zealand",
      "primary_organization": "Example Co",
      "title": "Product Lead",
      "notes_public": "Imported public bio.",
      "contact_note": "Exportable local note or supplement.",
      "image_path": "images/alice-johnson.jpg",
      "extra_json": {}
    }
  ]
}
```

Exports include imported facts, contact overlays, and referenced image files.
They do not include private relationship notes or per-contact tag lists by
default.

## M0 Decisions

- Private relationship notes are not included in normal exports.
- Contact overlays are included in exports by default.
- The v0 importer stores raw source JSON by default.
- Profile images are stored as files in the durable data/export model; importer
  internals may use binary blobs temporarily.
- Tags are implemented as a real table from v0.
- Provider-specific repeated data appears in full record view, not compact view
  by default.
- Tags are not exported as per-contact metadata by default.
- Saved networks store reusable search DSL strings and may use auto-generated
  names based on tags, filters, and bare text terms.
- The first search DSL uses Google-like bare terms, `#tag`, `has:*`, default
  `AND`, and explicit `OR`.
- The first `has:*` filters are `has:email`, `has:phone`, and `has:image`.
- Saved networks store only the DSL string, not the compiled structured query.
- Full record view uses friendly formatting first, with raw JSON as fallback.

## Remaining Open Questions

- Which additional `has:*` filters should be added after email, phone, and image?
- Should the first export warning be shown for all generated names, or only names
  containing tags and bare text terms?
