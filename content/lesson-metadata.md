# Lesson metadata

To make our lessons citable, findable, and machine-readable (see
[making lessons FAIR](lesson-fair.md)), each lesson repository carries
two metadata files. This page is the reference for what they contain,
where they live, and when they get updated — including a field-by-field
guide for [setting up metadata on a new
lesson](#setting-up-metadata-for-a-new-lesson). For the human side of
"who gets listed", see [lesson credits](lesson-credits.md); for the
step-by-step update process, see [releasing a new
version](lesson-version.md).

## Overview

| File               | Location                | Added | Main fields                                                    | Read by                                            |
|--------------------|--------------------------|-------|------------------------------------------------------------------|-----------------------------------------------------|
| `CITATION.cff`     | root of each lesson repo | 2025  | authors, contact, title, abstract, version, date-released, doi (concept ID), license, url, repository-code, type, message, cff-version | GitHub "Cite this repository" button, Zenodo release |
| `bioschemas.yml`   | root of each lesson repo | 2026  | name, author, version, license, identifier (from CITATION.cff); description, keywords, educationalLevel, inLanguage, teaches, url, isPartOf (Bioschemas-specific) | Bioschemas/schema.org crawlers and catalogs          |

## `CITATION.cff`

This is the [Citation File Format](https://citation-file-format.github.io/)
standard. GitHub detects it automatically and shows a "Cite this
repository" button on the repo page.

Example, based on the [documentation lesson](https://github.com/coderefinery/documentation)'s `CITATION.cff`:

```yaml
cff-version: 1.2.0
message: "If you use this lesson material, please cite it using these metadata."
authors:
- name: "CodeRefinery"
- family-names: "Doe"
  given-names: "Jane"
- family-names: "Foe"
  given-names: "John"
title: "How to document your research software - CodeRefinery lesson"
type: "dataset"
abstract: "The lesson 'How to document your research software' gives an overview of the different ways how a code project can be documented: from small projects to larger projects. Markdown and Sphinx are central tools in this lesson."
version: 2026-08-03
doi: "10.5281/zenodo.8280234"
date-released: 2026-08-03
url: "https://coderefinery.github.io/documentation/"
license: CC-BY-4.0
repository-code: "https://github.com/coderefinery/documentation"
```

Fields we maintain, grouped by how often they change:

Set once, rarely touched afterwards:
- `cff-version` — version of the CFF schema itself, not our lesson.
  Set by the lesson template.
- `message` — boilerplate citation instruction, the same across lessons.
- `type` — always `"dataset"`; CFF has no dedicated "training material" type.
- `url` — link to the built lesson site.
- `license` — e.g. `CC-BY-4.0`.
- `repository-code` — link to the GitHub source repo.
- `doi` — left as-is; it is the Zenodo *concept* DOI that links all
  versions together, not the version-specific one.

Updated whenever the lesson content or people change:
- `title` and `abstract` — updated if the lesson's scope or focus
  changes materially. Note that title should include " - CodeRefinery lesson" in the end of the title so that lessons can be connected to CodeRefinery from the citation.
- `authors` — one entry per contributor. Individual people use
  `family-names`/`given-names` (and optionally `orcid`); the project as
  a whole is also listed as a single organizational author via `name:
  "CodeRefinery"`. See [lesson credits](lesson-credits.md) for how a
  person gets added. We don't distinguish smaller "contributor"-level
  credit — anyone listed here is an author.
- `contact` — the current [lesson maintainer(s)](lesson-maintainer.md),
  same person format as `authors`. Updated whenever the maintainer
  changes.

Updated at release time:
- `version` — set to the release date, not a semantic version, e.g.
  `2026-08-03`. In practice this is kept identical to `date-released`.
- `date-released` — the release date, format `YYYY-MM-DD`.

Authors are updated on an ongoing basis, whenever someone contributes
(via pull request, or a maintainer adding them). `version` and
`date-released` only change as part of a release, see [releasing a new
version](lesson-version.md).

## `bioschemas.yml`

This provides [Bioschemas](https://bioschemas.org/)/schema.org markup,
using the `LearningResource` type. It's built into the lesson's HTML
pages as embedded JSON-LD, without being visible on the page itself —
it's meant to be read by crawlers and catalogs, not learners.

Example, based on the [documentation
lesson](https://github.com/coderefinery/documentation) (this is the
JSON-LD actually embedded in the page; the source `bioschemas.yml` is
equivalent):

```json
{
    "@context": "https://schema.org/",
    "@type": "LearningResource",
    "@id": "https://coderefinery.github.io/documentation/",
    "description": "The lesson 'How to document your research software' gives an overview of the different ways how a code project can be documented: from small projects to larger projects. Markdown and Sphinx are central tools in this lesson.",
    "keywords": "Documentation, Sphinx",
    "name": "How to document your research software",
    "author": [
        {
            "@type": "Organization",
            "name": "CodeRefinery"
        },
        {
            "@type": "Person",
            "name": "Jane Doe"
        }
    ],
    "educationalLevel": "Beginner",
    "identifier": "https://doi.org/10.5281/zenodo.8280234",
    "inLanguage": "en-UK",
    "license": "https://creativecommons.org/licenses/by/4.0/",
    "teaches": "Understand the importance of writing code documentation together with the source code, Know what makes a good documentation, Learn what tools can be used for writing documentation, Be able to motivate a balanced decision: sometimes READMEs are absolutely enough",
    "url": "https://coderefinery.github.io/documentation/",
    "isPartOf": "https://coderefinery.org",
    "version": "2023-08-03"
}
```

Its metadata is regenerated from `CITATION.cff` by running
`get_schema_info_from_cff.py` locally, so it should stay in sync
automatically as part of a release rather than being edited by hand,
but only for a subset of fields — the rest are Bioschemas-specific and
maintained directly in `bioschemas.yml`.

Auto-regenerated from `CITATION.cff` (see [releasing a new
version](lesson-version.md)) — don't hand-edit these, they'll be
overwritten at the next release:
- `name` — from `title`
- `author` — from `authors`; each `family-names`/`given-names` pair
  becomes a single `name` string, and CodeRefinery keeps its
  `Organization` type
- `version` — from `version`
- `license` — from `license`, converted from the SPDX identifier
  (`CC-BY-4.0`) to its full URL
- `identifier` — from `doi`, converted from the bare DOI to a full
  `https://doi.org/...` URL

Maintained directly in `bioschemas.yml` (no `CITATION.cff` equivalent
— edit these by hand when they change):
- `@context`, `@type` — fixed (`https://schema.org/`,
  `LearningResource`)
- `@id`, `url` — the canonical lesson URL
- `description` — kept in sync with `abstract` in `CITATION.cff` by
  hand
- `keywords` — comma-separated topics
- `educationalLevel` — e.g. `Beginner`
- `inLanguage` — e.g. `en-UK`
- `teaches` — comma-separated learning objectives
- `isPartOf` — fixed, `https://coderefinery.org` for every lesson

It also defines a separate `contributor` field distinct from
`authors`. We've decided not to use that distinction: everyone stays
under `authors` in both files, matching the `CITATION.cff` side.

## Zenodo

Every GitHub release triggers a new version in our [CodeRefinery
Zenodo community](https://zenodo.org/communities/coderefinery), under
the same concept DOI as previous releases (the concept DOI is the one
kept as `doi` in `CITATION.cff`). The Zenodo record's metadata
(title/authors/license/version) comes directly from `CITATION.cff` at
release time — see the verification step in [releasing a new
version](lesson-version.md).

## Lesson maintainer metadata

We started a more formal [lesson maintainer](lesson-maintainer.md) role
in 2026. The current maintainer(s) are recorded in the `contact` field
of `CITATION.cff` (same person format as `authors`), and are also named
in the lesson's README.

This still needs to be carried through to the other two places lesson
metadata ends up:

- **`bioschemas.yml`** — the closest semantic match is schema.org's
  `maintainer` property. This isn't generated yet: the
  `get_schema_info_from_cff.py` script currently only carries over
  name/authors/version/license/identifier, so it needs a small update
  per lesson repo to also map `contact` → `maintainer`.
- **Zenodo** — our deposits go through a custom release workflow
  (using the `ZENODO_TOKEN`/`ZENODO_CONCEPT_ID` secrets), not GitHub's
  built-in Zenodo integration, so nothing is added automatically.
  The natural mapping is a `contributors` entry with the Zenodo/DataCite
  contributor type `ContactPerson`. That workflow lives in each lesson
  repository rather than in this manuals repo, so it needs to be
  updated there too, and it's worth checking what it currently sends
  before assuming this mapping is live.

## Setting up metadata for a new lesson

New lessons start from the [Sphinx lesson
template](https://github.com/coderefinery/sphinx-lesson-template),
which already includes a skeleton `CITATION.cff` and `bioschemas.yml`.
Go through both files field by field when setting up a new lesson.

### `CITATION.cff`

Leave as the template sets them:
- `cff-version`, `message`, `type`
- `license` — `CC-BY-4.0` for all our lessons

Fill in now:
- `title` — the lesson's title, ending in " - CodeRefinery lesson"
- `abstract` — a short (1-3 sentence) description of what the lesson
  covers
- `authors` — start with the `CodeRefinery` organizational entry, plus
  whoever is creating the lesson; more are added as people contribute,
  see [lesson credits](lesson-credits.md)
- `contact` — the initial [lesson maintainer](lesson-maintainer.md),
  if one has already been assigned; otherwise add this once one is
- `url` — the lesson's future GitHub Pages URL, i.e.
  `https://coderefinery.github.io/<repo-name>/`
- `repository-code` — the new GitHub repository's URL
- `version`, `date-released` — today's date, format `YYYY-MM-DD`

Leave blank until the first release:
- `doi` — there's no concept DOI yet. Follow the prerequisites in
  [releasing a new version](lesson-version.md) to set up the Zenodo
  entry, then fill this in with the resulting concept DOI. Once set,
  it never changes again.

### `bioschemas.yml`

Leave as the template sets them:
- `@context`, `@type`

Fill in now, matching the corresponding `CITATION.cff` fields (from
the next release onward these stay in sync automatically, see above):
- `name` — same as `title`, but without the " - CodeRefinery lesson"
  suffix
- `author` — the same people/organization as `authors`, one `name`
  string per entry
- `version` — same as `version` in `CITATION.cff`
- `license` — full URL form of the license, e.g.
  `https://creativecommons.org/licenses/by/4.0/`

Fill in now, Bioschemas-specific (these are never auto-generated, so
they need to be set once and kept up to date by hand as the lesson
changes):
- `@id`, `url` — same as `url` in `CITATION.cff`
- `description` — same as `abstract`
- `keywords` — comma-separated topics/tools covered
- `educationalLevel` — e.g. `Beginner`, matching the lesson's stated
  audience
- `inLanguage` — `en-UK` for our English-language lessons
- `teaches` — comma-separated learning objectives, matching the
  lesson's own learning objectives if defined
- `isPartOf` — always `https://coderefinery.org`

Leave blank until the first release:
- `identifier` — same reasoning as `doi` above; fill in once the
  concept DOI exists.

## When things get updated, at a glance

- **As people contribute:** `CITATION.cff` authors list.
- **When the maintainer changes:** `contact` in `CITATION.cff` (and,
  once implemented, the corresponding `bioschemas.yml`/Zenodo fields).
- **When the lesson's scope changes materially:** `title`, `abstract`.
- **At release time:** `version`, `date-released` in `CITATION.cff`;
  regenerate `bioschemas.yml`; new Zenodo version created.
- **Rarely/manually:** `doi` (never, once set), `cff-version`,
  `message`, `type`, `url`, `license`, `repository-code`.
