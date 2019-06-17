# build file for jenkins
SOURCE="resume-liam-beckman.tex"
RESUME="resume-liam-beckman.pdf"
PRODUCTION="/var/www/pkgs/resume"

pdflatex $SOURCE
cp $RESUME $PRODUCTION
