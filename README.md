# markdown-talk

Presentation in markdown using LaTeX Beamer.

See [markdown-paper](https://github.com/ihrke/markdown-paper) for template for a scientific paper.

*NOTE*: [pandoc](http://pandoc.org/) version > 1.16 is recommended because image-attributes are not available before that version.


The Makefile details how the translation works. If you are on linux, simply calling make in the parent directory will compile the report to a pdf-format if all dependencies are installed. Edit the variables in the Makefile to choose a theme (check [this webpage](http://deic.uab.es/~iblanes/beamer_gallery/) for a gallery).


## Usage

1. Install the dependencies

    ~~~{bash}
    sudo apt-get install pandoc pandoc-citeproc
    pip install pandoc-fignos
    ~~~
2. check that pandoc has version>=1.16 (otherwise install from other source)

    ~~~{bash}
    pandoc -v
    ~~~
2. Clone this repository

    ~~~{bash}
    git clone https://github.com/ihrke/markdown-talk.git
    ~~~
3. Edit `Makefile` to choose a theme
4. Write talk in `talk.md`, refs in `bibliography.bib`, compile with `make`

There are some tips in the `talk.md` file to get you started.

NOTE: `guard.sh` is a little tool that calls `make` whenever something changes in the directory (I find it useful for updating the PDF automatically whenever I hit safe)

## Dependencies

- [pandoc](http://pandoc.org/)
- [pandoc-fignos](https://github.com/tomduck/pandoc-fignos)
- [pandoc-citeproc](https://github.com/jgm/pandoc-citeproc)
- a [latex](https://www.latex-project.org/)-distribution (e.g., [texlive](https://www.tug.org/texlive/)) including [bibtex](http://www.bibtex.org/)
- [latex-beamer](https://www.google.no/url?sa=t&rct=j&q=&esrc=s&source=web&cd=3&cad=rja&uact=8&ved=0ahUKEwiSidXzjYHLAhUjnXIKHRUEA5QQFggzMAI&url=http%3A%2F%2Fwww.ctan.org%2Ftex-archive%2Fmacros%2Flatex%2Fcontrib%2Fbeamer%2Fdoc%2Fbeameruserguide.pdf&usg=AFQjCNE2AQ9ERMbIUIUS-wzhXGtX5ozs0w&sig2=ByUFa0FTBmk44RWWL7UJEA)

---

Matthias Mittner <matthias.mittner@uit.no>
