pandoc masters2.md -F pandoc-crossref -F pandoc-citeproc --mathjax --standalone --number-sections -H ..\fix-captions.tex -H ..\mm.tex --bibliography ..\library.bib -o masters2.pdf
rem "timeout /t 10"
rem "pause"