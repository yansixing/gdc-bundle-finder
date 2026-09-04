#!/bin/bash
# 用法: ./find-sfx.sh 关键词 [关键词2 ...]   (多个词是"或",不分大小写,搜库名和文件名)
# 输出: 年份 | 分卷 | 库 | 文件名 —— 分卷号就是官网那个 zip 的序号
CSV="$(dirname "$0")/gdc_index.csv"
[ $# -eq 0 ] && { echo "用法: $0 creak wood"; exit 1; }
PAT=$(printf "%s|" "$@"); PAT=${PAT%|}
python3 - "$CSV" "$PAT" <<'PY'
import csv,re,sys,collections
csvf,pat=sys.argv[1],sys.argv[2];rx=re.compile(pat,re.I)
rows=[r for r in csv.DictReader(open(csvf,encoding='utf-8')) if rx.search(r['FILENAME']) or rx.search(r['SUPPLIER - LIBRARY'])]
for r in rows: print(f"{r['YEAR']:<9} | Part {r['PART']:>2} | {r['SUPPLIER - LIBRARY'][:46]:<46} | {r['FILENAME'][:60]}")
zips=collections.Counter((r['YEAR'],int(r['PART'])) for r in rows)
print(f"\n共 {len(rows)} 个文件。要下的 zip:")
for (y,p),n in sorted(zips.items()): print(f"  {y} Part {p}  ({n} 个命中)")
PY
