# GDC Bundle Finder

**English** · [中文](README.zh-CN.md)

**Live: <https://yansixing.github.io/gdc-bundle-finder/>** (English / 中文 toggle in the top-right corner)

Search every audio file in the free Sonniss **#GameAudioGDC** bundles (2015–2024, 73 zip parts, ~190 GB) and see exactly which zip part to download.

**No audio is hosted here.** The site only lists file names and links each library to the official zip on Sonniss's servers. Download the bundles from <https://sonniss.com/gameaudiogdc/> — they are free and royalty-free under the [#GameAudioGDC license](https://sonniss.com/gdc-bundle-license/), which forbids re-uploading the sounds themselves.

## Files

| File | What it is |
|---|---|
| `index.html` | The finder. A single self-contained page, works offline, ready for GitHub Pages. |
| `gdc_index.csv` | The same index as a spreadsheet: year, part, zip size, library, file name, size, zip URL. |
| `find-sfx.sh` | Command-line search: `./find-sfx.sh creak wood` lists matches and the zips to download. |
| `zip_listings.json` | Raw central-directory listings of all 73 zips (the source data). |
| `template.html` + `build.py` | Regenerate `index.html` and the CSV from the JSON. |

## How the index was made

Each zip's file list was read from its central directory at the tail of the archive using HTTP range requests, so nothing but a few hundred KB per zip was transferred. The index therefore reflects the archives exactly as Sonniss publishes them. Parts are split roughly alphabetically by "Supplier - Library" folder. 2021, 2022 and 2023 were released together as one 14-part bundle.

## Publishing with GitHub Pages

Push this folder to a repository, then in **Settings → Pages** choose the branch and root folder. `index.html` needs no build step.
