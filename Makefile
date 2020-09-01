SRC=resume-liam-beckman.tex
OUT=build

all: init clean resume

init:
	mkdir -p $(OUT)

# https://tex.stackexchange.com/a/64327
resume:
	TEXINPUTS=.//:: pdflatex -output-directory $(OUT) $(SRC)

clean:
	rm -rf $(OUT)/*

