[![Jenkins Badge][badge]][jenkins]

# About

A simple resume (and coverletter template)!

# Requirements

- [texlive](http://www.tug.org/texlive/): includes the `pdflatex` command for building a PDF from tex files.

## Packages

- babel
- datetime2
- easylist
- enumitem
- eso-pic
- fontenc
- geometry
- hyperref
- inputenc
- multicol
- tikz
- tikzpagenodes
- titlesec
- titling
- xcolor

# Building

To compile the tex file into a pdf, run:

```sh
make
```

It will output the resume and coverletter as PDFs.

![Second page of resume.](./resume-liam-beckman-0.png)
![First page of resume.](./resume-liam-beckman-1.png)

# CI/CD

The document is built every time a push is made to the `master` branch. Build commands are defined in the [Jenkinsfile](./Jenkinsfile), and build results can be viewed at either of the following URL's.

- [Jenkins (standard)][jenkins]
- [Jenkins (Blue Ocean)][blue]

[![Jenkins screenshot](./build.png)][blue]

[jenkins]: https://liambeckman.com/jenkins/job/git.liambeckman.com/job/resume/job/master/
[blue]: https://liambeckman.com/jenkins/blue/organizations/jenkins/git.liambeckman.com%2Fresume
[badge]: https://liambeckman.com/jenkins/job/git.liambeckman.com/job/resume/job/master/badge/icon?

