[![Build status](https://github.com/lbeckman314/resume/actions/workflows/build.yaml/badge.svg)](https://github.com/lbeckman314/resume/actions)

# Resume & Cover Letter

LaTeX source for Liam Beckman's resume and cover letter, currently targeting the [AI Automation Specialist](https://www.governmentjobs.com/careers/oregonmetro/jobs/4858424/ai-automation-specialist) role at Oregon Metro (Job No. 2026-0069-IT-4).

The cover letter includes a Claude Project system prompt built for the role — see the interactive demo at [lbeckman314.github.io/metro-ai](https://lbeckman314.github.io/metro-ai).

## Quick start

```sh
make
```

Output:

```sh
ls build/
coverletter.pdf
resume.pdf
```

To build individually:

```sh
make resume
make cover
```

To check all URLs in the source files:

```sh
make check
```

## Manual compilation

Both files require `--shell-escape` for `minted` (syntax highlighting):

```sh
TEXINPUTS=.//:: pdflatex --shell-escape -output-directory build src/resume.tex
TEXINPUTS=.//:: pdflatex --shell-escape -output-directory build src/coverletter.tex
```

## Requirements

### TeX Live

Install [TeX Live](http://www.tug.org/texlive/) for the `pdflatex` command and `tlmgr` package manager.

### LaTeX packages

```sh
sudo tlmgr install \
  datetime2      \
  easylist       \
  enumitem       \
  environ        \
  etoolbox       \
  eso-pic        \
  fontawesome5   \
  fvextra        \
  framed         \
  ifoddpage      \
  minted         \
  pdfcol         \
  pgf            \
  tcolorbox      \
  tikzfill       \
  tikzpagenodes  \
  titlesec       \
  titling        \
  tools          \
  upquote        \
  xstring
```

### Pygments

Required by `minted` for syntax highlighting:

```sh
pip3 install pygments
```

## Structure

```
src/
├── resume.tex          # resume entry point
├── coverletter.tex     # cover letter entry point
├── main.tex            # shared preamble (packages, commands, admonitions)
└── include/
    ├── header.tex      # name, contact, summary
    ├── education.tex
    ├── ohsu.tex        # Research Software Engineer, OHSU (2023–present)
    ├── saltire.tex     # Full Stack Developer, Saltire Software (2022)
    ├── reactome.tex    # Research Software Developer, OHSU (2019–2020)
    ├── published.tex   # publications and presentations
    └── footer.tex
```

## CI

GitHub Actions builds both PDFs on every push to `main` using [`xu-cheng/texlive-action`](https://github.com/xu-cheng/texlive-action). Artifacts are uploaded and retained for 30 days. Tagged releases (`v*.*.*`) attach the PDFs to a GitHub Release.

See [`.github/workflows/build.yaml`](.github/workflows/build.yaml).

## Author

Liam Beckman — [liambeckman.com](https://liambeckman.com/code) · [liam@liambeckman.com](mailto:liam@liambeckman.com)
