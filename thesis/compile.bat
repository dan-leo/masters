pandoc masters.md --filter pandoc-fignos --mathjax --standalone --number-sections -H fix-captions.tex --bibliography .\library.bib -o masters.pdf
timeout /t 10