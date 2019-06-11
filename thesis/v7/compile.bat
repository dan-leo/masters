pandoc martinez.md -F pandoc-crossref -F pandoc-citeproc --pdf-engine=xelatex --mathjax --standalone --number-sections -H ..\fix-captions.tex -H ..\mm.tex --bibliography ..\library.bib -o masters7.pdf
rem "timeout /t 10"
rem "pause"