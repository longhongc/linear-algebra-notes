# Linear Algebra Notes

Personal linear algebra notes distilled from discussions with ChatGPT. The focus is on topics that are easy to misunderstand and on small extensions or side thoughts that came up while learning.

GitHub: [https://github.com/longhongc/linear-algebra-notes](https://github.com/longhongc/linear-algebra-notes)

## Repo structure
- `raws/`: original notes.
- `docs/`: MkDocs site root (`index.md` lives here).
- `docs/notes/`: MkDocs-compatible notes (mainly for LaTeX syntax).
- `format_raw_to_docs.py`: script that converts `raws/` into `docs/notes/`.
- `mkdocs.yml`: MkDocs configuration.

## Resources used
### Books
- Sheldon Axler, *Linear Algebra Done Right*.
- Gilbert Strang, *Linear Algebra and Its Applications*.

### Video series
- 3Blue1Brown, [*Essence of Linear Algebra* (YouTube)](https://youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab&si=ULx7NuL18mrh5fla).
- Visual Kernel, [*Matrix* series (YouTube)](https://youtube.com/playlist?list=PLWhu9osGd2dB9uMG5gKBARmk73oHUUQZS&si=9g14KcG363GJ7BHS).

## Notes
If you want to rebuild the rendered notes, update content in `raws/` and run `format_raw_to_docs.py` to regenerate `docs/notes/`.
