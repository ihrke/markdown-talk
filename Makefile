THEME=default
PANDOC=pandoc #/usr/local/bin/pandoc
BIBLIOGRAPHY=bibliography.bib
MD_FILES=talk.md


TEX_FILES:=$(MD_FILES:.md=.tex)
PDF_FILES:=$(MD_FILES:.md=.pdf)


all: $(TEX_FILES) $(PDF_FILES)

%.pdf: %.md
	$(PANDOC) -s -S -t beamer $< -V theme:$(THEME) --filter pandoc-citeproc --bibliography $(BIBLIOGRAPHY) -o $@

%.tex: %.md
		$(PANDOC) -s -S -t beamer $< -V theme:$(THEME) --filter pandoc-citeproc --bibliography $(BIBLIOGRAPHY) -o $@

.PHONY : clean
clean :
	-rm $(PDF_FILES) *.aux *.out *.log *.fdb_latexmk *.fls *.synctex.gz
