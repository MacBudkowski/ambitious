# Source notice

The four reference files (`speed.md`, `depth.md`, `range.md`, `altitude.md`) each end with a section marked **BEGIN VERBATIM / END VERBATIM**. That text is quoted from:

> Felix Rieseberg, *How to be more ambitious: A tutorial for humans with models*
> <https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/>

- Rights to the quoted text stay with the original author. The package's MIT license does **not** cover it.
- The quotations are kept so an agent can apply each type from the author's own words, not from a summary. Only the section for the type in use gets loaded.
- No affiliation with or endorsement by the author is implied.
- If you redistribute this package publicly and the quoted text isn't cleared for that, replace each verbatim block with a link to the article. The guidance above each block still works without it.

`tests/test_package.py` checks that the quoted blocks match a fixed checksum, so accidental edits to the author's text are caught.
