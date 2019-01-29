pandoc masters5.md -F pandoc-crossref -F pandoc-citeproc --pdf-engine=xelatex --variable classoption=twocolumn --mathjax --standalone --number-sections -H ..\fix-captions.tex -H ..\mm.tex --bibliography ..\library.bib -o masters5.pdf --filter=abbrevs.py
rem "timeout /t 10"
rem "pause"