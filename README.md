[![Build status](https://github.com/lbeckman314/resume/actions/workflows/build.yaml/badge.svg)](https://github.com/lbeckman314/resume/actions)

# Overview ⚙️

My resume and coverletter!

# Quick Start ⚡

To automatically compile both the resume and coverletter, run:

```sh
➜ make

➜ ls build
coverletter.pdf  <---- Cover Letter
resume.pdf       <---- Resume
```

Alternatively, to manually create these files, run:

```sh
➜ TEXINPUTS=.//:: pdflatex resume.tex

➜ TEXINPUTS=.//:: pdflatex coverletter.tex
```

# Requirements

- [texlive](http://www.tug.org/texlive/): includes the `pdflatex` command for building a PDF from tex files.

## TeX Packages

- datetime2
- easylist
- enumitem
- ifoddpage
- tikzpagenodes
- titlesec
- titling

![Resume](./resume.png)
