# GDC Bundle Finder

**English** · [中文](README.zh-CN.md)

**Live: <https://yansixing.github.io/gdc-bundle-finder/>** (English / 中文 toggle in the top-right corner)

Search every audio file in the free Sonniss **#GameAudioGDC** bundles (2015–2026, 78 zip parts, ~200 GB) and see exactly which zip part to download.

**No audio is hosted here.** The site only lists file names and links each library to the official zip on Sonniss's servers. Download the 2015–2024 bundles from <https://sonniss.com/gameaudiogdc/> and the 2026 bundle from <https://gdc.sonniss.com/> — they are free and royalty-free under the [#GameAudioGDC license](https://sonniss.com/gdc-bundle-license/), which forbids re-uploading the sounds themselves.

## Preview single files without downloading a zip

Every entry in a zip is an independent byte range, and Sonniss's download server honours HTTP range requests. The finder fetches just the one file you press ▶ on (typically 5–30 MB), inflates it with the browser's built-in `DecompressionStream`, decodes it with Web Audio and plays it. Nothing is re-hosted: the bytes go from Sonniss to your browser, one file at a time.

Browsers block cross-site requests, so this only works when the page runs on Sonniss's own download host. Setup is two clicks: drag the "GDC Finder preview" bookmark from the page to your bookmarks bar, open <https://downloads.sonniss.com/gdc-finder> (a "Not Found" page — that's expected) and click the bookmark there. The finder loads in that tab with working ▶ buttons. Needs a current Chrome, Edge, Firefox or Safari.

## Files

| File | What it is |
|---|---|
| `index.html` | The finder. A single self-contained page, works offline, ready for GitHub Pages. |
| `gdc_index.csv` | The same index as a spreadsheet: year, part, zip size, library, file name, size, zip URL. |
| `find-sfx.sh` | Command-line search: `./find-sfx.sh creak wood` lists matches and the zips to download. |
| `zip_listings.json` | Raw central-directory listings of all 78 zips (the source data). |
| `template.html` + `build.py` | Regenerate `index.html` and the CSV from the JSON. |

## How the index was made

Each zip's file list was read from its central directory at the tail of the archive using HTTP range requests, so nothing but a few hundred KB per zip was transferred. The index therefore reflects the archives exactly as Sonniss publishes them. Parts are split roughly alphabetically by "Supplier - Library" folder. 2021, 2022 and 2023 were released together as one 14-part bundle. There was no 2025 bundle; 2026 lives on its own site and Sonniss says it may grow, so the index is a snapshot.

## Publishing with GitHub Pages

Push this folder to a repository, then in **Settings → Pages** choose the branch and root folder. `index.html` needs no build step.
