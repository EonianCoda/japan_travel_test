# CLAUDE.md

本檔案提供給 Claude Code (claude.ai/code) 在本 repository 工作時的指引。

本 repository 的所有文件必須使用繁體中文撰寫。

## 重要原則

### 資訊正確性
- 所有旅遊資訊（票價、時間、開放時間等）必須有原始參考來源
- 旅遊資料具有時效性，資訊可能過時，請在引用前驗證
- 重要數據（票價、交通費用、營業時間）應交叉比對多個來源
- **嚴禁自行臆測**：嚴禁根據自身知識儲備直接回答景點、美食、交通等資訊。所有資訊必須透過 web search 查證後再提供，確保準確性與時效性

### 參考來源要求
- 每個事實性資訊（票價、時刻表、地址等）必須標註來源
- 使用爬蟲抓取網頁後，存入 `reference/` 目錄作為備份
- 在文件末尾加入「參考來源」章節，列出所有引用的 URL

### 資料更新流程
1. 發現新資訊時，先用爬蟲抓取原始頁面存入 `reference/`
2. 驗證資訊是否與現有資料衝突
3. 更新主要文件時保留參考連結

### 行程選擇階段原則
- 目前仍處於「選擇行程」階段，尚未進入「詳細規劃」階段
- 不要過早擬定「第幾天去哪裡」的具體時間表
- 優先收集候選景點、美食、活動等選項，再逐步篩選整合

## 概述

這是一個大阪・京都之旅的個人旅遊規劃 repository（2026年10月）。主要文件 `osaka_kyoto_7days.md` 包含7天行程規劃，涵蓋景點、交通、美食和購物詳情。

## 主要檔案

### 根目錄
- `大阪京都七天.html` - 旅遊計劃 HTML 版本
- `CLAUDE.md` - 本檔案

### 審核目錄 audit/
- `audit/records/` - 審核記錄（按日期存放）
- `audit/records/2026-05-24.md` - 最新審核記錄
- `audit/verified.md` - 已驗證的資訊
- `audit/discrepancies.md` - 發現的資訊不一致處

### 景點選擇輸出 attraction_selector_output/
- `attraction_selector_output/attractions.html` - 候選景點清單（多功能互動網頁）
- `attraction_selector_output/foods.html` - 美食選擇器（類似attractions.html的互動分頁）

**attractions.html 功能說明（請勿移除）**：
- 資料來源：景點資料內嵌於 HTML 中的 JavaScript `attractions` 陣列
- 篩選功能：城市（單選）、標籤（多選 AND 邏輯）、免費景點、已選景點、文字搜尋
- 檢視模式：卡片視圖 / 表格視圖，可切換
- 標籤系統：所有標籤都有顏色底色，支援多選（需同時滿足所有選中的標籤）
- 地圖連結：表格檢視有 Google Maps 📍 欄位
- 選擇功能：可勾選景點加入已選清單，支援匯出 JSON / 複製名稱
- 重要：修改 HTML 時請勿移除這些功能的核心 JavaScript 邏輯

**foods.html 功能說明（請勿移除）**：
- 資料來源：美食店家資料內嵌於 HTML 中的 JavaScript `foods` 陣列
- 結構與 attractions.html 類似，便於同步操作
- 篩選功能：地區（單選）、類別標籤（多選 AND 邏輯）、平價、已選、文字搜尋
- 標籤系統：所有標籤都有顏色底色，支援多選（需同時滿足所有選中的標籤）
- 價位標籤：自動判斷平價/中價位/高價位
- 地圖連結：表格檢視有 Google Maps 📍 欄位
- 重要：修改 HTML 時請勿移除這些功能的核心 JavaScript 邏輯

### 資料目錄 data/
- `data/attractions.json` - 景點資料庫

### 參考資料 reference/
- 爬蟲抓取的原始網頁備份（34+ 個檔案）
- 包含交通、美食、景點等各類參考資料

### docs/ 目錄結構
```
docs/
├── 01_overview/          # 概覽
│   ├── 基本資訊.md        # 基本旅遊資訊
│   └── 天氣.md           # 天氣穿搭建議
├── 02_transport/         # 交通
│   ├── 交通票券.md       # ICOCA、JR Pass 等票券
│   ├── 交通總覽.md       # 交通整體說明
│   ├── 京都車站.md       # 京都車站相關
│   ├── 嵐山小火車.md     # 嵐山小火車資訊
│   ├── 大阪車站.md       # 大阪車站相關
│   └── 機場交通.md       # 機場來往交通
├── 03_areas/             # 區域
│   ├── 京都/京都.md      # 京都區域
│   ├── 大阪/大阪.md      # 大阪區域
│   ├── 奈良/奈良.md      # 奈良區域
│   └── 區域總覽.md       # 區域分類總覽
├── 04_attractions/       # 景點
│   ├── 景點總覽.md       # 景點分類總覽
│   ├── 主題分類.md       # 主題性景點分類
│   ├── 秋季賞楓專篇.md   # 秋季賞楓推薦
│   ├── 大阪/             # 大阪景點
│   │   ├── 大阪市中心.md
│   │   ├── 大阪灣.md
│   │   └── 大阪其他.md
│   ├── 京都/             # 京都景點
│   │   ├── 京都經典.md
│   │   ├── 京都祕境.md
│   │   └── 京都文化.md
│   ├── 奈良/奈良景點.md  # 奈良景點
│   └── 關西延伸/         # 關西延伸景點
│       ├── 環球影城.md
│       ├── 動漫.md
│       └── 關西延伸.md
└── 05_food/              # 美食
    ├── 美食總覽.md       # 美食分類總覽
    ├── 伴手禮.md         # 伴手禮推薦
    ├── 大阪/             # 大阪美食
    │   ├── 道頓堀.md
    │   ├── 心齋橋.md
    │   ├── 黑門市場.md
    │   └── 臨空城.md
    ├── 京都/             # 京都美食
    │   ├── 祇園.md
    │   ├── 宇治.md
    │   └── 嵐山.md
    └── 奈良/奈良美食.md  # 奈良美食
```

## 爬蟲工具

爬蟲工具位於 `.claude/skills/web-crawler/`。使用方式：

```bash
source .venv/bin/activate
python -c "
from pathlib import Path
import sys
sys.path.insert(0, str(Path('.claude/skills/web-crawler/scripts')))
from crawl import WebCrawler
crawler = WebCrawler(output_dir='reference', delay=2)
crawler.crawl_batch(['https://example.com/page1', 'https://example.com/page2'])
"
```

## 參考資料

`reference/` 目錄包含爬蟲抓取的原始參考資料備份（34+ 個檔案），涵蓋交通、美食、景點等各類資訊。

`data/attractions.json` - 景點資料庫 JSON 檔案

## 技能工具

### .claude/skills/
- `attraction-selector/` - 景點篩選工具
- `web-crawler/` - 網頁爬蟲工具
- `fact-check/` - 資訊審核工具