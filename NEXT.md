# Next

## P05 · Reliable Data Pipeline and Analytics · 5A Tested ingestion CLI

**One ten-minute task:** Propose a name and typed signature for the function that will read one CSV file. Explain what the path argument represents, how the header and string-valued fields map to the returned rows, and what the caller observes if the file is missing.

Use the standard library (`pathlib.Path` and `csv.DictReader`). For this first slice, assume well-formed input with a header and a fixed number of fields per row. Return a list of row dictionaries and allow `FileNotFoundError` to propagate. Write the proposed signature and explanation for review before implementing the reader.

This is the file-source slice of the ingestion module. The CLI, validation, deterministic output and failure tests are later acceptance work for 5A.
