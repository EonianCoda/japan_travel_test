# 大阪・京都 7日旅遊參考資料

> 2026年10月旅行規劃用

## 爬蟲結果總覽

| 狀態 | 數量 |
|------|------|
| ✅ 成功 | 14 |
| ❌ 失敗 | 1 |
| **總計** | **15** |

---

## ✅ 成功爬取

### 天氣與穿著

| 檔案 | 來源 | 大小 |
|------|------|------|
| `tw_4945.md` | MATCHA 京阪神9、10月穿搭 | 18KB |
| `japan-outfits.md` | 穿搭哲學 | 53KB |
| `archives_683738.md` | 大阪天氣11月穿搭建議 | 15KB |
| `archives_344905.md` | 京都行程規劃詳細指南 | 42KB |

### 行程規劃

| 檔案 | 來源 | 大小 |
|------|------|------|
| `tw_18058.md` | MATCHA 大阪自由行懶人包 | 35KB |
| `world-trip_kyoto-osaka.md` | 七天六夜全攻略 | 22KB |

### 交通攻略

| 檔案 | 來源 | 大小 |
|------|------|------|
| `guide_transport_關西+JR+Pass.html.md` | Trip.com JR Pass比較 | 1KB |
| `kansai-jrpass.md` | 關西廣域pass | 18KB |
| `kansai-transport-passes.md` | 私鐵周遊券比較 | 45KB |

### 賞楓情報

| 檔案 | 來源 | 大小 |
|------|------|------|
| `archives_55899.md` | 京都賞楓景點26選、紅葉時間預測 | 58KB |
| `moments_detail_kyoto-430-139065264.md` | 清水寺賞楓攻略 | 2KB |

### 美食推薦

| 檔案 | 來源 | 大小 |
|------|------|------|
| (部分失敗，見下方) | - | - |

### 購物指南

| 檔案 | 來源 | 大小 |
|------|------|------|
| `2014-12-osaka-omiyage.html.md` | 大阪必買伴手禮20選 | 60KB |
| `shinsaibashi.md` | 心齋橋攻略 | 21KB |
| `zh-tw_in-kansai_in-pref-kyoto_in-kyoto-station_to-ji-temple_article-a2000788.md` | 京都逛街25選 | 80KB |

---

## ❌ 爬取失敗

| 原始URL | 錯誤 |
|--------|------|
| auntie.tw | 403 Forbidden |

### 替代方案

此網站可手動複製內容或使用瀏覽器 Bookmarklet 取得。

---

## 資料庫結構

```
/home/user/personal/202610_japenese_travel/
├── osaka_kyoto_7days.md          # 主要旅遊計畫文件
├── crawl.py                      # Python爬蟲腳本
├── reference/                    # 爬取的原文資料
│   ├── *.md                      # 各URL內容
│   └── README.md                 # 本文件
└── .venv/                        # Python虛擬環境
```

---

## 使用方式

### 重新爬取所有URL
```bash
source .venv/bin/activate
python crawl.py
```

### 爬取特定URL
```python
from crawl import WebCrawler

crawler = WebCrawler()
crawler.crawl_and_save("https://example.com/article")
```

---

*最後更新：2026年5月24日*