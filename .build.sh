# build file for jenkins
SOURCE="resume.tex"
RESUME="resume.pdf"
PRODUCTION="/var/www/pkgs/resume"

pdflatex $SOURCE
cp $RESUME $PRODUCTION
