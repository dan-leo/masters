pandoc metrics.md -F pandoc-crossref -F pandoc-citeproc --mathjax --standalone --number-sections -H ..\fix-captions.tex -H ..\mm.tex --bibliography ..\library.bib -o metrics.pdf
rem "timeout /t 10"
rem "pause"