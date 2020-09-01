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

It will output the resume as a PDF.

![Second page of resume.](./resume-liam-beckman-0.png)
![First page of resume.](./resume-liam-beckman-1.png)

# CI/CD

The document is built every time a push is made to the `master` branch. Build commands are defined in the [Jenkinsfile](./Jenkinsfile), and build results can be viewed at either of the following URL's.

- [Jenkins (standard)](https://liambeckman.com/jenkins/job/resume/)
- [Jenkins (Blue Ocean)](https://liambeckman.com/jenkins/blue/organizations/jenkins/resume/activity)

[![Screenshot of resume in Jenkins](./build.png)](https://liambeckman.com/jenkins/blue/organizations/jenkins/resume/)
