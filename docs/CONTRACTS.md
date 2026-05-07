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
- Keep imported facts read-only; write private tags and notes in separate tables.

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


| Field                  | Type        | Required | Notes                                                 |
| ---------------------- | ----------- | -------- | ----------------------------------------------------- |
| `source_id`            | string/null | No       | Stable ID from the source when available.             |
| `display_name`         | string      | Yes      | Viewer label; importer should synthesize if needed.   |
| `given_name`           | string/null | No       | Search/display helper.                                |
| `family_name`          | string/null | No       | Search/display helper.                                |
| `primary_email`        | string/null | No       | Initial high-value contact method/filter.             |
| `primary_phone`        | string/null | No       | Useful secondary contact method.                      |
| `primary_location`     | string/null | No       | Free-text location for v0.                            |
| `primary_organization` | string/null | No       | Company/group/org label.                              |
| `title`                | string/null | No       | Role/title/headline.                                  |
| `notes_public`         | string/null | No       | Imported bio/tagline/public note, not private notes.  |
| `image.path`           | string/null | No       | Relative path inside the bundle when an image exists. |
| `extra_json`           | object      | No       | Normalized but non-canonical fields.                  |
| `raw_source_json`      | object      | No       | Original source object when safe and useful.          |


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

### Stable Identity

`contact_id` is a toolkit-generated UUID or similarly stable opaque ID. It is
not the Google resource name, email address, or slug.

Importers should resolve an incoming contact to an existing `contact_id` using:

1. `(source_type, source_id)` in `contact_aliases`.
2. Normalized primary email, when unambiguous.
3. A conservative fallback such as normalized name plus phone.
4. New generated ID.

This preserves private tags and notes across re-imports.

## Private Relationship Layer

Relationship metadata is writable local data. It is not part of imported contact
facts.

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

CREATE TABLE notes (
    note_id TEXT PRIMARY KEY,
    title TEXT,
    body TEXT NOT NULL,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);

CREATE TABLE contact_notes (
    contact_id TEXT NOT NULL,
    note_id TEXT NOT NULL,
    created_at TEXT NOT NULL,
    PRIMARY KEY (contact_id, note_id),
    FOREIGN KEY (contact_id) REFERENCES contacts(contact_id) ON DELETE CASCADE,
    FOREIGN KEY (note_id) REFERENCES notes(note_id) ON DELETE CASCADE
);
```

This is simpler than PRT's current relationship-type model. Typed
contact-to-contact relationships can be added later.

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
      "image_path": "images/alice-johnson.jpg",
      "tags": ["family"],
      "notes": [
        {"title": "Context", "body": "Private note exported by user choice."}
      ],
      "extra_json": {}
    }
  ]
}
```

## Open Questions

- Should private notes be included in exports by default, opt-in only, or never?
- Should the v0 importer store raw source JSON by default, or require a flag for
privacy-sensitive sources?
- Should profile images be stored only as files, or can some importers store
binary blobs temporarily before export?
- Should tags be globally reusable strings, or should v0 allow per-contact ad hoc
labels without a `tags` table?
- The last question I'm not too sure about: the provider-specific repeated data. I assume you're talking about import data, and provider-specific might be, say, Google Contacts has a whole bunch of data that is specific to Google Contacts, perhaps, or maybe Facebook Imports have some data that is specific to Facebook Imports. Regarding that, on the display of the data, I think we really do need to have a couple of different views there. We'll have the full record be one view, so all the provider-specific data is probably in there. That'd be a full record view, and then we'd have a compact view. The compact view might be normal, and you might have to hit more to get the full data view. Compact view would be:
  - contact information
  - name
  - maybe their location
  - and then I suppose tags would be something that you could have shown as well
   Anything else like notes and lots of data specific to the platform they were imported from should all be in a full view that doesn't show up in the compact view. I hope that's what you were asking for. If not, please ask away and let me know what else you need on the questions at the end of Contacts MD.

