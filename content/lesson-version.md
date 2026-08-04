# Releasing a new version of a lesson

Many people may be updating the lessons at any time. Though at some point the new version should be released and stored on Zenodo. A good time would usually be after a workshop. This page describes the process to **release a new version**. See [lesson metadata](lesson-metadata.md) for a reference on what each metadata field means and where it lives.

0. Prerequisites: 
- The Zenodo entry is (co-)managed by Code Refinery Zenodo user.
- The GitHub repository has a Zenodo environment set up with secret `ZENODO_TOKEN` and environment variable `ZENODO_CONCEPT_ID` (this is set to the ID shown in Zenodo for linking to ALL versions (with 10.0000/zenodo.1234567 -> 1234567 would be the concept ID)). 

1. Update `CITATION.cff`

- Bump `version` and `date-released` to the new release date (today, format YYYY-mm-dd).
- Add/update authors if the contributor list changed. This should happen as part of updating the lesson, though may easily be forgotten, so double check: diff the commit authors since the last release tag against the `authors` list in `CITATION.cff`, e.g. `git log <last-version-tag>..HEAD --format='%an <%ae>' | sort -u`. Remember that not all contributions (discussions and reviews) may be on GitHub, so also check those separately. 
- Leave `doi` as-is —  it is the concept ID for the whole lesson version set.

2. Regenerate `bioschemas.yml`

Run `python3 get_schema_info_from_cff.py` locally so the Bioschemas/schema.org metadata (name, authors, version, license, identifier) stays in sync with the `CITATION.cff` changes from step 1. You may also do manual updates to `bioschemas.yml` if there are any other developments. 

3. Wait and check that GitHub pages are built

After merging above changes, wait until GitHub pages were rebuilt (build action successful and `gh-pages` up to date). 

4. Create a new release 

Use the same version as in `CITATION.cff` as new tag (you can also create the tag beforehand) and name for the release. 

5. Watch the workflow run and verify the output

Confirm: new version created under the same concept DOI, both the zip and the versioned PDF attached, metadata (title/authors/license/version) matches the updated CITATION.cff. 

Done!