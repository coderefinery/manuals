# Releasing a new version of a lesson

Many people may be updating the lessons at any time. Though at some point the new version should be released and stored on Zenodo. A good time would usually be after a workshop. This page describes the process to **release a new version**. See [lesson metadata](lesson-metadata.md) for a reference on what each metadata field means and where it lives.

0. Prerequisites: 
- The Zenodo entry is (co-)managed by Code Refinery Zenodo user.
- The GitHub repository has a Zenodo environment set up with secret `ZENODO_TOKEN` and environment variable `ZENODO_CONCEPT_ID` (this is set to the ID shown in Zenodo for linking to ALL versions (with 10.0000/zenodo.1234567 -> 1234567 would be the concept ID)). 

1. Update `metadata.yml`

- Bump `version` to the new release date (today, format YYYY-mm-dd) — this single field also covers `CITATION.cff`'s `date-released`.
- Add/update authors if the contributor list changed. This should happen as part of updating the lesson, though may easily be forgotten, so double check: diff the commit authors since the last release tag against the `authors` list in `metadata.yml`, e.g. `git log <last-version-tag>..HEAD --format='%an <%ae>' | sort -u`. Remember that not all contributions (discussions and reviews) may be on GitHub, so also check those separately.
- Leave `doi` as-is — it is the concept ID for the whole lesson version set.

Push/merge this to `main`: `CITATION.cff` and `bioschemas.yml` regenerate themselves automatically (see [lesson metadata](lesson-metadata.md)) — there's nothing to run locally or edit by hand in either file.

2. Wait and check that GitHub pages are built

After merging the `metadata.yml` change (and the bot commit that regenerates `CITATION.cff`/`bioschemas.yml`), wait until GitHub pages were rebuilt (build action successful and `gh-pages` up to date).

3. Create a new release

Use the same version as in `metadata.yml` as new tag (you can also create the tag beforehand) and name for the release.

4. Watch the workflow run and verify the output

Confirm: new version created under the same concept DOI, both the zip and the versioned PDF attached, metadata (title/authors/license/version) matches `metadata.yml`.

Done!