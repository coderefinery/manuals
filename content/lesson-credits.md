# Lesson credits

To acknowledge all contributors to our material, every lesson repository has a `metadata.yml` file listing authors, from which `CITATION.cff`, `bioschemas.yml`, and the Zenodo record are all generated automatically. See [lesson metadata](lesson-metadata.md) for the full reference on how this works.

We've decided not to distinguish different levels of contribution: everyone who contributed more than a typo fix is listed as an author, if they wish so.

Bioschemas' schema.org vocabulary also has a separate `contributor` concept, distinct from `author`. We keep everyone as an author rather than splitting across the two.

We're considering a more formal role of [lesson maintainer](lesson-maintainer.md) — currently just an initial suggestion, not an adopted role. `metadata.yml` already has an (optional, not yet actively used) `maintainers` field for this. See [lesson metadata](lesson-metadata.md#lesson-maintainer-metadata) for exactly what recording a maintainer there would and wouldn't carry through to `CITATION.cff`, bioschemas, and Zenodo.

## Adding an author

If you have been linked here, you might have been asked if you want to
be listed as an author.  If someone has asked you, then don't worry if
you contribution is enough: the threshold is not high.  If so,
consider:
- Your name and info will be included in the Zenodo citation, which is
  permanent
- You will be included in future releases as well, unless you ask to be removed
- Please send us: family-names, given-names, and if you want ORCID
  ([reference of valid
  keys](https://github.com/citation-file-format/citation-file-format/blob/main/schema-guide.md#definitionsperson)).

The preferred way is to open a pull request adding yourself directly to
`metadata.yml`, under the `authors:` list, for example:

```yaml
authors:
  - family-names: Doe
    given-names: Jane
    orcid: "https://orcid.org/0000-0000-0000-0000"
```

New authors are usually appended at the end of the list; there is no
strict ordering requirement. If you'd rather not deal with git/YAML,
send us the same information and someone from the CodeRefinery team
will add it for you (once the [lesson maintainer](lesson-maintainer.md)
role is adopted, maintainers would be expected to proactively reach
out to people when they contribute).

Everyone should send a pull request to be included in
`metadata.yml` if you desire.  Note that not all contributions may be visible from the Git history. Often, multiple people are involved in change discussions. Those should at least be asked if they want to be named as author.

Merging that pull request to `main` regenerates `CITATION.cff` and
`bioschemas.yml` automatically (see [lesson
metadata](lesson-metadata.md)) — there's nothing else to update by
hand when adding an author.


## Adding an acknowledgee

There are very many, so we try to add them to the lesson
README page if it's not based on a Github interaction (or if it's desired for
some other reason).




