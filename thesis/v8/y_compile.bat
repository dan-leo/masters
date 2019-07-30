set file=%~1
pandoc "%~1" -F pandoc-crossref -F pandoc-citeproc --mathjax --standalone -o "%file:~0,-2%pdf" --pdf-engine=xelatex
rem "timeout /t 10"
rem "pause"
rem "-F mermaid-filter.cmd"
rem "--number-sections"