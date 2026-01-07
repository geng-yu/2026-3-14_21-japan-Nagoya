# 檔案名稱：app.py
import streamlit as st
from datetime import datetime, date

# 匯入每一天的模組 (確保這些 .py 檔案都在同一個資料夾)
import day1, day2, day3, day4, day5, day6, day7, day8

# --- 頁面基本設定 ---
st.set_page_config(
    page_title="2026 名古屋",
    page_icon="🇯🇵",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- CSS 優化 (包含橫向滑動選單與手機版按鈕) ---
st.markdown("""
    <style>
    /* 全域按鈕樣式 (原本的設定) */
    .stButton button {
        width: 100%;
        border-radius: 20px;
        font-weight: bold;
        border: 1px solid #ddd;
    }
    
    /* 隱藏預設選單與頁尾 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Day Card 樣式 */
    .day-card {
        background-color: #f9f9f9;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 10px;
        border: 1px solid #eee;
    }

    /* --- 重點：橫向滑動導覽列 CSS 魔改 --- */
    
    /* 1. 針對 Radio 元件的容器設定：強制不換行、允許橫向滑動 */
    div[role="radiogroup"] {
        flex-direction: row;
        overflow-x: auto; /* 允許左右滑動 */
        white-space: nowrap; /* 強制文字不換行 */
        padding-bottom: 10px; /* 預留捲軸空間或呼吸空間 */
        flex-wrap: nowrap !important; /* 覆寫 Streamlit 預設 */
        gap: 10px; /* 按鈕之間的間距 */
        -webkit-overflow-scrolling: touch; /* 讓 iOS 滑動更順暢 */
    }

    /* 2. 隱藏原本 Radio 的圓圈圈 */
    div[role="radiogroup"] label > div:first-child {
        display: none;
    }

    /* 3. 設定按鈕的外觀 (未選中狀態) */
    div[role="radiogroup"] label {
        background-color: #f0f2f6;
        padding: 10px 15px;
        border-radius: 15px;
        border: 1px solid #ddd;
        cursor: pointer;
        transition: all 0.3s;
        margin-right: 0px; /* 間距由 gap 控制 */
        display: inline-flex;
        align-items: center;
        justify-content: center;
        min-width: 80px; /* 確保按鈕有最小寬度 */
    }

    /* 4. 設定被選中時的樣式 (High Light) */
    div[role="radiogroup"] label[data-baseweb="radio"] > div {
        color: #31333F; /* 文字顏色 */
    }
    
    /* 這裡稍微 tricky，Streamlit 選中時會加 data-checked 屬性，
       或是我們可以透過 CSS 選取 checked 的 input 的父層 (較難)，
       通常 Streamlit 會幫選中的項目加特定 class，但最簡單是看 UI 變化。
       比較穩定的做法是讓所有選項都長得像按鈕，
       Streamlit 原生選中時會有一個背景色變化，我們利用那個變化。
    */
    
    div[role="radiogroup"] label:hover {
        border-color: #ff4b4b;
        color: #ff4b4b;
    }

    /* 隱藏捲軸本身但保留功能 (可選) */
    div[role="radiogroup"]::-webkit-scrollbar {
        height: 4px;
    }
    div[role="radiogroup"]::-webkit-scrollbar-thumb {
        background: #ccc; 
        border-radius: 10px;
    }

    </style>
""", unsafe_allow_html=True)

# --- 日期與資料設定 ---
# 為了讓橫向按鈕不要太長導致字被切掉，建議這裡的 Key (顯示文字) 可以精簡一點
# 或者是用兩行顯示，這裡示範稍微縮短一點的標題，或者保留原樣
trip_dates = {
    "1/17 (六)\nDay 1": (date(2026, 1, 17), day1),
    "1/18 (日)\nDay 2": (date(2026, 1, 18), day2),
    "1/19 (一)\nDay 3": (date(2026, 1, 19), day3),
    "1/20 (二)\nDay 4": (date(2026, 1, 20), day4),
    "1/21 (三)\nDay 5": (date(2026, 1, 21), day5),
    "1/22 (四)\nDay 6": (date(2026, 1, 22), day6),
    "1/23 (五)\nDay 7": (date(2026, 1, 23), day7),
    "1/24 (六)\nDay 8": (date(2026, 1, 24), day8),
}

# 為了方便顯示詳細標題，我們另外做一個 Mapping
trip_details = {
    "1/17 (六)\nDay 1": "Day 1: 出發 & 移動",
    "1/18 (日)\nDay 2": "Day 2: 金澤市區",
    "1/19 (一)\nDay 3": "Day 3: 合掌村 & 飛驒",
    "1/20 (二)\nDay 4": "Day 4: 新穗高 & 高山",
    "1/21 (三)\nDay 5": "Day 5: 牧歌 & 犬山",
    "1/22 (四)\nDay 6": "Day 6: 名古屋榮商圈",
    "1/23 (五)\nDay 7": "Day 7: 大須 & 名古屋城",
    "1/24 (六)\nDay 8": "Day 8: 回程",
}

# --- 自動判斷日期邏輯 ---
today = datetime.now().date()
# today = date(2026, 1, 17) # 測試用：取消註解可測試效果

default_index = 0
options = list(trip_dates.keys())

for i, (label, (d, module)) in enumerate(trip_dates.items()):
    if d == today:
        default_index = i
        break

# --- 介面呈現 ---
st.title("🇯🇵 2026 名古屋")

# 使用 Radio 元件，但透過 CSS 偽裝成橫向選單
selected_short_label = st.radio(
    "選擇行程日期", # label，已被 CSS 隱藏或可保留
    options,
    index=default_index,
    horizontal=True, # 這是關鍵，讓它水平排列
    label_visibility="collapsed" # 隱藏 "選擇行程日期" 這幾個字
)

st.divider()

# --- 顯示詳細標題 ---
# 既然上面的按鈕簡化了，這裡就顯示完整標題
full_title = trip_details[selected_short_label]
st.markdown(f"### {full_title}")

# --- 呼叫對應的 Day 模組 ---
target_module = trip_dates[selected_short_label][1]
target_module.show()
