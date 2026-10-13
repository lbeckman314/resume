RESUME=resume-liam-beckman.tex
COVER=coverletter-liam-beckman.tex
RESUME_GH=resume-liam-beckman-google-health.tex
COVER_GH=coverletter-google-health.tex
OUT=build

.PHONY: all
all: init resume cover google-health

.PHONY: init
init:
	mkdir -p $(OUT)

# Execute pdflatex in build directory.
# https://tex.stackexchange.com/a/64327
resume build:
	TEXINPUTS=.//:: pdflatex --shell-escape -output-directory $(OUT) $(RESUME)

cover:
	TEXINPUTS=.//:: pdflatex --shell-escape -output-directory $(OUT) $(COVER)

.PHONY: google-health
google-health:
	TEXINPUTS=.//:: pdflatex --shell-escape -output-directory $(OUT) $(RESUME_GH)
	TEXINPUTS=.//:: pdflatex --shell-escape -output-directory $(OUT) $(COVER_GH)

check:
	@echo "Checking URLs in LaTeX files..."
	@find src -name "*.tex" -exec grep -oE 'https://[^}]+' {} \; | sort -u | while read url; do \
		echo "Checking: $$url ... "; \
		if curl -s -o /dev/null -w "%{http_code}" "$$url" | grep -q "200"; then \
			echo "✅ OK"; \
		else \
			echo "❌ Failed (Status: $$(curl -s -o /dev/null -w "%{http_code}" "$$url"))"; \
		fi; \
	done

.PHONY: clean
clean:
	rm -rf $(OUT)/*

