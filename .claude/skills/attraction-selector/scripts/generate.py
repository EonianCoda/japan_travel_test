#!/usr/bin/env python3
"""Generate CSV and HTML from attractions.json"""

import json
import csv

DATA_FILE = "data/attractions.json"
OUTPUT_DIR = "attraction_selector_output"

def main():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    attractions = data["attractions"]

    print(f"Loaded {len(attractions)} attractions from {DATA_FILE}")

    import os
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    csv_path = f"{OUTPUT_DIR}/attractions.csv"
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=[
            "id", "name", "city", "area", "category", "features", "price",
            "duration", "address", "hours", "transport", "link", "tags"
        ])
        writer.writeheader()
        writer.writerows(attractions)

    print(f"CSV written to {csv_path}")

    attractions_json = json.dumps(attractions, ensure_ascii=False)

    html_path = f"{OUTPUT_DIR}/attractions.html"
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(f'''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>大阪・京都景點選擇器</title>
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #f5f5f5; padding: 20px; }}
h1 {{ text-align: center; color: #333; margin-bottom: 20px; }}

.view-toggle {{ text-align: center; margin-bottom: 20px; }}
.view-toggle button {{ padding: 10px 20px; margin: 0 5px; border: 1px solid #ddd; background: white; border-radius: 4px; cursor: pointer; font-size: 14px; }}
.view-toggle button.active {{ background: #4CAF50; color: white; border-color: #4CAF50; }}

.filters {{ background: white; padding: 15px; border-radius: 8px; margin-bottom: 20px; display: flex; flex-wrap: wrap; gap: 10px; align-items: center; }}
.filter-group {{ display: flex; align-items: center; gap: 5px; }}
.filter-group label {{ font-weight: 500; font-size: 14px; }}
.filter-group select {{ padding: 8px 12px; border: 1px solid #ddd; border-radius: 4px; font-size: 14px; }}
.filter-group input[type="checkbox"] {{ width: 16px; height: 16px; }}

.stats {{ background: white; padding: 10px 15px; border-radius: 8px; margin-bottom: 20px; font-size: 14px; color: #666; }}

/* Card View */
.attractions-grid {{ display: none; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 15px; }}
.attractions-grid.show {{ display: grid; }}

.card {{ background: white; border-radius: 8px; padding: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); transition: transform 0.2s; }}
.card:hover {{ transform: translateY(-2px); box-shadow: 0 4px 8px rgba(0,0,0,0.15); }}
.card.selected {{ border: 2px solid #4CAF50; background: #f8fff8; }}

.card-header {{ display: flex; justify-content: space-between; align-items: start; margin-bottom: 10px; }}
.card h3 {{ font-size: 16px; color: #333; margin-right: 10px; }}
.card h3 a {{ color: inherit; text-decoration: none; }}
.card h3 a:hover {{ text-decoration: underline; }}

.card-header input[type="checkbox"] {{ width: 20px; height: 20px; cursor: pointer; flex-shrink: 0; }}

.tags {{ display: flex; flex-wrap: wrap; gap: 5px; margin-bottom: 10px; }}
.tag {{ padding: 4px 8px; border-radius: 4px; font-size: 12px; font-weight: 500; }}
.tag.city-kyoto {{ background: #e8f5e9; color: #2e7d32; }}
.tag.city-osaka {{ background: #fff3e0; color: #e65100; }}
.tag.city-nara {{ background: #f3e5f5; color: #7b1fa2; }}
.tag.city-kansai {{ background: #e3f2fd; color: #1565c0; }}
.tag.price {{ background: #f5f5f5; color: #616161; }}
.tag.free {{ background: #c8e6c9; color: #2e7d32; }}
.tag.area {{ background: #eee; color: #666; }}
.tag.必去 {{ background: #ffcdd2; color: #c62828; }}
.tag.賞楓 {{ background: #ffccbc; color: #bf360c; }}
.tag.賞花 {{ background: #f8bbd9; color: #880e4f; }}
.tag.夜景 {{ background: #e1bee7; color: #6a1b9a; }}
.tag.美食 {{ background: #d7f9d0; color: #2e7d32; }}
.tag.購物 {{ background: #fff9c4; color: #f57f17; }}
.tag.神社寺院 {{ background: #ffe0b2; color: #e65100; }}
.tag.文化體驗 {{ background: #b3e5fc; color: #0277bd; }}
.tag.體驗 {{ background: #c8e6c9; color: #2e7d32; }}
.tag.自然 {{ background: #c8e6c9; color: #1b5e20; }}
.tag.免費 {{ background: #c8e6c9; color: #2e7d32; }}
.tag.收費 {{ background: #fff3e0; color: #e65100; }}
.tag.世界遺產 {{ background: #ffecb3; color: #ff6f00; }}
.tag.主題樂園 {{ background: #e1f5fe; color: #0277bd; }}
.tag.ACG/玩具 {{ background: #f3e5f5; color: #7b1fa2; }}
.tag.溫泉 {{ background: #e0f7fa; color: #00838f; }}

.features {{ color: #666; font-size: 14px; margin-bottom: 10px; line-height: 1.4; }}

.details {{ font-size: 13px; color: #757575; line-height: 1.6; }}
.details strong {{ color: #555; }}

/* Table View */
.attractions-table {{ display: none; background: white; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
.attractions-table.show {{ display: table; width: 100%; }}

.attractions-table table {{ width: 100%; border-collapse: collapse; }}

.attractions-table th, .attractions-table td {{ padding: 12px 15px; text-align: left; border-bottom: 1px solid #eee; font-size: 14px; }}

.attractions-table th {{ background: #f5f5f5; font-weight: 600; color: #333; }}

.attractions-table tr:hover {{ background: #f9fff9; }}

.attractions-table td input[type="checkbox"] {{ width: 18px; height: 18px; cursor: pointer; }}

.attractions-table .tag {{ display: inline-block; padding: 3px 8px; border-radius: 4px; font-size: 12px; }}

/* Export Section */
.export-section {{ background: white; padding: 20px; border-radius: 8px; margin-top: 20px; text-align: center; }}
.export-section button {{ padding: 12px 24px; font-size: 16px; border: none; border-radius: 4px; cursor: pointer; margin: 5px; }}
.btn-export {{ background: #4CAF50; color: white; }}
.btn-export:hover {{ background: #45a049; }}
.btn-copy {{ background: #2196F3; color: white; }}
.btn-copy:hover {{ background: #1976D2; }}

.result-box {{ margin-top: 15px; padding: 15px; background: #f5f5f5; border-radius: 4px; text-align: left; max-height: 200px; overflow-y: auto; display: none; }}
.result-box.show {{ display: block; }}
.result-box pre {{ white-space: pre-wrap; font-size: 13px; }}

footer {{ text-align: center; margin-top: 30px; color: #999; font-size: 12px; }}
</style>
</head>
<body>
<h1>大阪・京都之旅 - 景點選擇器</h1>

<div class="view-toggle">
    <button id="cardViewBtn" class="active" onclick="showCardView()">卡片視圖</button>
    <button id="tableViewBtn" onclick="showTableView()">表格視圖</button>
</div>

<div class="filters">
    <div class="filter-group">
        <label>城市：</label>
        <select id="cityFilter" onchange="updateTagOptions(); filterAttractions()">
            <option value="all">全部</option>
            <option value="京都">京都</option>
            <option value="大阪">大阪</option>
            <option value="奈良">奈良</option>
            <option value="關西延伸">關西延伸</option>
        </select>
    </div>
    <div class="filter-group">
        <label>標籤：</label>
        <select id="tagFilter" onchange="filterAttractions()">
            <option value="all">全部標籤</option>
        </select>
    </div>
    <div class="filter-group">
        <input type="checkbox" id="freeOnly" onchange="filterAttractions()">
        <label for="freeOnly">只顯示免費景點</label>
    </div>
    <div class="filter-group">
        <input type="checkbox" id="selectedOnly" onchange="filterAttractions()">
        <label for="selectedOnly">只顯示已選</label>
    </div>
</div>

<div class="stats">
    共 <span id="totalCount">0</span> 個景點，已選擇 <span id="selectedCount">0</span> 個
</div>

<!-- Card View -->
<div class="attractions-grid" id="cardGrid"></div>

<!-- Table View -->
<div class="attractions-table" id="tableView">
    <table>
        <thead>
            <tr>
                <th style="width:40px"></th>
                <th>景點名稱</th>
                <th>城市</th>
                <th>標籤</th>
                <th>特色</th>
                <th>票價</th>
                <th>停留</th>
                <th>開放時間</th>
                <th>交通</th>
            </tr>
        </thead>
        <tbody id="tableBody"></tbody>
    </table>
</div>

<div class="export-section">
    <button class="btn-export" onclick="exportSelected()">匯出已選景點</button>
    <button class="btn-copy" onclick="copySelected()">複製選擇</button>
    <div class="result-box" id="resultBox"><pre id="resultText"></pre></div>
</div>

<footer>用 Claude Code 整理 | 2026年5月</footer>

<script>
const attractions = {attractions_json};
let currentView = 'card';
const selectedSet = new Set();

function isFree(price) {{
    return !price || price === '免費' || price.includes('免費');
}}

function handleCheckboxChange(name, checked) {{
    if (checked) {{
        selectedSet.add(name);
    }} else {{
        selectedSet.delete(name);
    }}
    updateStats();
}}

function showCardView() {{
    currentView = 'card';
    document.getElementById('cardViewBtn').classList.add('active');
    document.getElementById('tableViewBtn').classList.remove('active');
    document.getElementById('cardGrid').classList.add('show');
    document.getElementById('tableView').classList.remove('show');
}}

function showTableView() {{
    currentView = 'table';
    document.getElementById('tableViewBtn').classList.add('active');
    document.getElementById('cardViewBtn').classList.remove('active');
    document.getElementById('cardGrid').classList.remove('show');
    document.getElementById('tableView').classList.add('show');
}}

function renderCards(filtered) {{
    const grid = document.getElementById('cardGrid');
    grid.innerHTML = filtered.map(a => {{
        const isSelected = selectedSet.has(a.name);
        const cityClass = a.city === '京都' ? 'city-kyoto' : a.city === '大阪' ? 'city-osaka' : a.city === '奈良' ? 'city-nara' : 'city-kansai';
        const priceClass = isFree(a.price) ? 'free' : 'price';
        const mapsUrl = a.link ? a.link : 'https://www.google.com/maps/search/?api=1&query=' + encodeURIComponent(a.name + ' ' + a.city);
        const tagsArr = a.tags || [];
        const tagsHtml = tagsArr.map(t => '<span class="tag tag-' + t + '">' + t + '</span>').join('');

        return '<div class="' + (isSelected ? 'card selected' : 'card') + '" data-city="' + a.city + '" data-tags="' + tagsArr.join(',') + '">' +
            '<div class="card-header">' +
            '<h3><a href="' + mapsUrl + '" target="_blank">' + a.name + '</a></h3>' +
            '<input type="checkbox" class="want-to-go" data-name="' + a.name + '"' + (isSelected ? ' checked' : '') + ' onchange="handleCheckboxChange(\\'' + a.name.replace(/'/g, "\\\\'") + '\\', this.checked)">' +
            '</div>' +
            '<div class="tags">' + tagsHtml + '</div>' +
            '<p class="features">' + (a.features || '') + '</p>' +
            '<div class="details">' +
            (a.duration ? '<strong>停留：</strong>' + a.duration + '<br>' : '') +
            (a.hours ? '<strong>時間：</strong>' + a.hours + '<br>' : '') +
            (a.transport ? '<strong>交通：</strong>' + a.transport : '') +
            '</div>' +
            '</div>';
    }}).join('');
}}

function renderTable(filtered) {{
    const tbody = document.getElementById('tableBody');
    tbody.innerHTML = filtered.map(a => {{
        const isSelected = selectedSet.has(a.name);
        const cityClass = a.city === '京都' ? 'city-kyoto' : a.city === '大阪' ? 'city-osaka' : a.city === '奈良' ? 'city-nara' : 'city-kansai';
        const priceClass = isFree(a.price) ? 'free' : 'price';
        const mapsUrl = a.link ? a.link : 'https://www.google.com/maps/search/?api=1&query=' + encodeURIComponent(a.name + ' ' + a.city);
        const tagsArr = a.tags || [];
        const tagsHtml = tagsArr.map(t => '<span class="tag tag-' + t + '">' + t + '</span>').join('');

        return '<tr>' +
            '<td><input type="checkbox" class="want-to-go" data-name="' + a.name + '"' + (isSelected ? ' checked' : '') + ' onchange="handleCheckboxChange(\\'' + a.name.replace(/'/g, "\\\\'") + '\\', this.checked)"></td>' +
            '<td><a href="' + mapsUrl + '" target="_blank">' + a.name + '</a></td>' +
            '<td><span class="tag ' + cityClass + '">' + a.city + '</span></td>' +
            '<td>' + tagsHtml + '</td>' +
            '<td>' + (a.features || '-') + '</td>' +
            '<td><span class="tag ' + priceClass + '">' + (a.price || '免費') + '</span></td>' +
            '<td>' + (a.duration || '-') + '</td>' +
            '<td>' + (a.hours || '-') + '</td>' +
            '<td>' + (a.transport || '-') + '</td>' +
            '</tr>';
    }}).join('');
}}

function filterAttractions() {{
    const cityFilter = document.getElementById('cityFilter').value;
    const tagFilter = document.getElementById('tagFilter').value;
    const freeOnly = document.getElementById('freeOnly').checked;
    const selectedOnly = document.getElementById('selectedOnly').checked;

    const filtered = attractions.filter(a => {{
        if (cityFilter !== 'all' && a.city !== cityFilter) return false;
        if (tagFilter !== 'all' && !(a.tags || []).includes(tagFilter)) return false;
        if (freeOnly && !isFree(a.price)) return false;
        if (selectedOnly && !selectedSet.has(a.name)) return false;
        return true;
    }});

    renderCards(filtered);
    renderTable(filtered);
    document.getElementById('totalCount').textContent = filtered.length;
}}

function updateStats() {{
    document.getElementById('selectedCount').textContent = selectedSet.size;
}}

function updateTagOptions() {{
    const cityFilter = document.getElementById('cityFilter').value;
    const allTags = [...new Set(attractions.filter(a => cityFilter === 'all' || a.city === cityFilter).flatMap(a => a.tags || []))];
    const select = document.getElementById('tagFilter');
    select.innerHTML = '<option value="all">全部標籤</option>' + allTags.map(t => '<option value="' + t + '">' + t + '</option>').join('');
}}

function getSelectedAttractions() {{
    return Array.from(selectedSet);
}}

function exportSelected() {{
    const selected = getSelectedAttractions();
    const resultBox = document.getElementById('resultBox');
    const resultText = document.getElementById('resultText');
    const selectedData = attractions.filter(a => selected.includes(a.name));
    resultText.textContent = JSON.stringify(selectedData, null, 2);
    resultBox.classList.add('show');
}}

function copySelected() {{
    const selected = getSelectedAttractions();
    const text = selected.join('\\n');
    navigator.clipboard.writeText(text).then(() => {{
        const btn = document.querySelector('.btn-copy');
        btn.textContent = '已複製!';
        setTimeout(() => btn.textContent = '複製選擇', 2000);
    }});
}}

document.getElementById('cityFilter').addEventListener('change', () => {{
    updateTagOptions();
    filterAttractions();
}});

// Initialize
updateTagOptions();
filterAttractions();
</script>
</body>
</html>''')

    print(f"HTML written to {html_path}")
    print(f"\\nDone! Generated {len(attractions)} attractions")

if __name__ == "__main__":
    main()