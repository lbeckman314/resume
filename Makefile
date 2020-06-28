DIR=build
SRC=resume-liam-beckman.tex

all: init clean pdf

init:
	mkdir -p $(DIR)

clean:
	rm -rf $(DIR)/*

pdf:
	pdflatex -output-directory $(DIR) $(SRC)

