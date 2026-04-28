RESUME=resume.tex
COVER=coverletter.tex
OUT=build

.PHONY: all
all: init resume cover

.PHONY: init
init:
	mkdir -p $(OUT)

# Execute pdflatex in build directory.
# https://tex.stackexchange.com/a/64327
resume build:
	TEXINPUTS=.//:: pdflatex --shell-escape -output-directory $(OUT) $(RESUME)

cover:
	TEXINPUTS=.//:: pdflatex --shell-escape -output-directory $(OUT) $(COVER)

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

