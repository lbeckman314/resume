# jobs

Scripts used by the daily job-search routine to maintain the job tracker.

- `check.py [dir]` checks whether each posting saved as `<dir>/*.json` (tracker rows, each with `url` and `status`) is still open.
- `sweep.py [known-url ...]` searches Greenhouse, Ashby and Lever boards for platform and infrastructure roles in Portland, Oregon or remote US, plus IT roles on the State of Oregon's Workday site (which includes OHA). It skips any URL passed as an argument.
- `detail.py url ...` prints the pay, years of experience and key technologies for Greenhouse, Ashby or Workday postings. State of Oregon pay is monthly.

Run them with `python3 -I`. They use only the standard library.
