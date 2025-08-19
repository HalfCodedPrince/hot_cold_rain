A script for **mass-renaming** .md files and changing the links, if the header is compliant with the style standard.

- **mapping.csv** - you put filename.md,filename_want_to_have.md there (no spaces, separated by a comma)
- **periodize_preflight.sh** is a sanity-check for formatting of mapping.csv
- **periodize_many.sh** has two modes. Default one is dry-run, telling you what it would do. Add APPLY as an argument to run it.

If something doesn't work, make sure that mapping.csv is compliant. I suggest running
```
dos2unix your_location/mapping.csv
```