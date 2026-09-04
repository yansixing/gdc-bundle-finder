# GDC Bundle Finder · GDC 音效包查找器

[English](README.md) · **中文**

Sonniss 每年 GDC 期间免费放出的 **#GameAudioGDC** 音效包（2015 到 2024 年，共 73 卷 zip，约 190 GB），这里把每一卷里的每个音频文件都建了索引。搜一下，就知道你要的声音在哪一年的第几卷，只下那一卷就行，不用整套几十 GB 全拉下来。

**在线使用：<https://yansixing.github.io/gdc-bundle-finder/>**（右上角可切换中英文）

**本仓库不存放任何音频。** 网页只列文件名，每个音效库旁边的标签直接链到 Sonniss 服务器上对应的那一卷 zip。音效请到 <https://sonniss.com/gameaudiogdc/> 下载，全部免费、免版税、可商用，遵循 [#GameAudioGDC 协议](https://sonniss.com/gdc-bundle-license/)。协议明确禁止把音效本身转载、重新打包或上传到别处，所以这里只有索引。

## 文件说明

| 文件 | 用途 |
|---|---|
| `index.html` | 查找器网页。单个文件、自带全部数据，离线也能用，直接放 GitHub Pages。 |
| `gdc_index.csv` | 同一份索引的表格版：年份、分卷、zip 大小、库名、文件名、文件大小、zip 直链。 |
| `find-sfx.sh` | 命令行搜索：`./find-sfx.sh creak wood`，末尾会列出要下载的分卷。 |
| `zip_listings.json` | 73 卷 zip 的原始目录数据（索引的源数据）。 |
| `template.html` + `build.py` | 从 JSON 重新生成 `index.html` 和 CSV。 |

## 搜索语法

- 多个词是"且"的关系：`creak wood` 要求两个词都出现
- 减号排除：`drone -aircraft -quadcopter`
- 引号精确短语：`"wind chimes"`
- 文件名和库名都是英文，请用英文关键词搜

## 索引是怎么建的

zip 的文件列表存在压缩包尾部的中央目录里。用 HTTP Range 请求只读每卷末尾那几百 KB，就能拿到完整文件名，一个音频字节都不用下载。所以索引和 Sonniss 官方发布的压缩包完全一致。

分卷大致按"供应商 - 库名"文件夹的字母顺序切分，边界处有少量交叉。2021、2022、2023 三年合并发布为一个 14 卷的包。

## 自己部署

把这个仓库推到 GitHub，在 **Settings → Pages** 里选择分支和根目录即可，`index.html` 不需要构建步骤。改了数据或模板后运行 `python3 build.py` 重新生成。
