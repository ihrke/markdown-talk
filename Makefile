THEME=CambridgeUS
COLORTHEME=crane
TEMPLATE=templates/amsterdam.beamer
PANDOC=pandoc #/usr/local/bin/pandoc
BIBLIOGRAPHY=bibliography.bib
MD_FILES=talk.md


TEX_FILES:=$(MD_FILES:.md=.tex)
PDF_FILES:=$(MD_FILES:.md=.pdf)
TEMPLATE_FILES:=$(wildcard templates/*.beamer)

all: $(TEX_FILES) $(PDF_FILES)

%.pdf: %.md $(TEMPLATE_FILES)
	$(PANDOC) -s -S -t beamer $< -V theme:$(THEME) -V colortheme:$(COLORTHEME) --filter pandoc-citeproc --bibliography $(BIBLIOGRAPHY) --template $(TEMPLATE) -o $@

%.tex: %.md $(TEMPLATE_FILES)
		$(PANDOC) -s -S -t beamer $< -V theme:$(THEME) --filter pandoc-citeproc --bibliography $(BIBLIOGRAPHY) --template $(TEMPLATE) -o $@

.PHONY : clean
clean :
	-rm $(PDF_FILES) *.aux *.out *.log *.fdb_latexmk *.fls *.synctex.gz
