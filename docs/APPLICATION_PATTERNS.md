# Application Patterns

Personal Network Toolkit is not only one application. It is a set of reusable
local-first tools and contracts for building applications around contacts,
directories, and personal networks.

The core modules are:

- **Importer**: turns source-specific contact exports into normalized contact
  bundles.
- **Directory DB**: stores normalized contact facts, local overlays, tags, notes,
  aliases, and FTS indexes.
- **Viewer**: provides a fast local PWA/web UI for browsing, filtering, and
  inspecting contacts.
- **Search/filter**: turns text, filters, tags, and later DSL/natural language
  into deterministic result sets.
- **Exporter**: turns a result set into portable JSON, HTML, PDF, email lists,
  or other downstream artifacts.

Developers should be able to use all of these pieces together or replace any
one of them with their own script or application.

## Pattern 1: Hosted Or Distributed Group Directory

This is the pattern proven by `fellows_local_db`.

Use this when an organization, fellowship, event, club, school, or community has
directory data and wants a durable, fast, offline-capable directory for members.

Flow:

```text
old directory export
  -> importer / cleanup script
  -> normalized contact bundle
  -> directory DB
  -> PWA directory app
  -> optional magic-link / allowlist distribution
```

The resulting app can be installed as a PWA, cached offline, and distributed to
members. It can preserve richer data and images that do not fit naturally in a
spreadsheet.

This pattern is not necessarily the default personal-contact flow. Magic links,
email gates, and hosted deployment are optional pieces that become useful when a
group directory needs controlled distribution.

## Pattern 2: Personal Contact Import And Curation

Use this when a person wants to bring together contacts from Google, Apple,
Facebook, LinkedIn, CSV files, or bespoke directories and keep private
relationship context locally.

Flow:

```text
personal contact exports
  -> import adapters
  -> directory DB
  -> local viewer/search
  -> contact overlays + tags + private notes
```

Imported facts remain read-only and rebuildable. Local overlays correct or
supplement incomplete records. Tags and private notes let the user organize
contacts into meaningful personal networks without sending sensitive context
back to centralized vendors.

## Pattern 3: Filtered Network Export

Use this when a user has a large noisy directory and needs a small useful subset.

Flow:

```text
directory DB
  -> viewer/search/filter
  -> filtered result set
  -> export bundle
  -> HTML / PDF / list / downstream tool
```

Examples:

- A family face/name PDF before a visit.
- A small event roster.
- A work-plus-pickleball list.
- A static website directory for a group.
- A shareable JSON bundle for another tool.

The exporter is valuable even when the viewer is not. A developer could import
contacts with PNT, run their own filter script, and still use the export bundle
contract to generate HTML or PDF.

## Pattern 4: Directory-App Starter Kit

Use this when a developer wants to build a new app like `fellows_local_db`
without starting from scratch.

Flow:

```text
normalized contact bundle
  -> directory DB
  -> generic PWA viewer
  -> app-specific branding/copy/filters/deployment
```

The toolkit should make this boring:

- define the fields
- load the images
- build the SQLite DB
- expose the API
- provide the local/offline viewer
- let the developer customize app-specific details

This is one of the strongest arguments for keeping the modules simple. A
developer should be able to use the importer and DB, swap the viewer, or keep the
viewer and swap the importer.

## Pattern 5: Communication-Oriented Network Tool

Use this when a user wants to find the right people and act quickly.

Flow:

```text
viewer/search/filter
  -> filtered result set
  -> mailto links or notifier
  -> later channel plugins / community protocols
```

The first proof can be simple: generated HTML and directory views can include
individual `mailto:` links and possibly group mail links. Later, a notifier can
support richer delivery reports, templates, and channel plugins.

## Pattern 6: Future Community Relationship Layer

Use this later when personal network data becomes the substrate for
peer-to-peer, encrypted, community-aware tools.

Flow:

```text
local personal network
  -> explicit user/community rules
  -> encrypted messages or signals
  -> nudges / introductions / community-health workflows
```

This is not part of the first implementation, but the core contracts should keep
the door open: stable IDs, exportable result sets, local relationship metadata,
and pluggable communication channels.

