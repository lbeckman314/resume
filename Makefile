RESUME=resume-liam-beckman.tex
COVER=coverletter-liam-beckman.tex
OUT=build

.PHONY: all
all: init clean resume cover

.PHONY: init
init:
	mkdir -p $(OUT)

# Execute pdflatex in build directory.
# https://tex.stackexchange.com/a/64327
resume:
	TEXINPUTS=.//:: pdflatex -output-directory $(OUT) $(RESUME)

cover:
	TEXINPUTS=.//:: pdflatex -output-directory $(OUT) $(COVER)

.PHONY: clean
clean:
	rm -rf $(OUT)/*

