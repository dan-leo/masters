set file=%~1
rem "pandoc "%~1" -H ..\fix-captions.tex -F pandoc-tablenos -F pandoc-crossref -F pandoc-citeproc --mathjax --standalone -o "%file:~0,-2%pdf" --pdf-engine=xelatex --bibliography ..\library.bib > err.log"
rem "pdflatex "%file:~0,-2%tex" > err.log"
pandoc "%~1" -H ..\fix-captions.tex -F pandoc-tablenos -F pandoc-crossref -F pandoc-citeproc --mathjax --standalone -o "%file:~0,-2%tex" --pdf-engine=xelatex --bibliography ..\library.bib
pdflatex -interaction=nonstopmode -quiet "%file:~0,-2%tex
rem "-H ..\fix-captions.tex"
rem "-H ..\mm.tex"
rem "timeout /t 1"
rem "pause"
rem "-F mermaid-filter.cmd"
rem "--number-sections"