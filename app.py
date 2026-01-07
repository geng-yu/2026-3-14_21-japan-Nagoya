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
    /* 全域按鈕樣式 */
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

    /* --- 橫向滑動導覽列 CSS --- */
    
    /* 1. 容器設定：橫向排列、可滑動 */
    div[role="radiogroup"] {
        flex-direction: row;
        overflow-x: auto;
        flex-wrap: nowrap !important;
        gap: 8px; /* 按鈕間距 */
        padding-bottom: 5px;
        -webkit-overflow-scrolling: touch; 
    }

    /* 2. 隱藏 Radio 的圓圈 */
    div[role="radiogroup"] label > div:first-child {
        display: none;
    }

    /* 3. 按鈕外觀 (未選中) */
    div[role="radiogroup"] label {
        background-color: #f0f2f6;
        padding: 8px 12px;
        border-radius: 12px;
        border: 1px solid #ddd;
        cursor: pointer;
        transition: all 0.2s;
        
        /* 關鍵：讓內容可以換行並置中 */
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center; 
        
        /* 固定最小寬度，讓按鈕看起來整齊 */
        min-width: 70px; 
        height: 55px; /* 固定高度確保對齊 */
    }

    /* 4. 強制文字內容允許換行 (針對 Streamlit 內部結構) */
    div[role="radiogroup"] label p {
        font-size: 14px;
        line-height: 1.2; /* 縮小行距讓兩行更緊湊 */
        font-weight: bold;
        margin: 0px;
        white-space: pre-wrap; /* 這是關鍵！允許 \n 換行 */
    }

    /* 5. 被選中時的樣式 (Streamlit 預設選中會變色，這裡加強邊框) */
    div[role="radiogroup"] label:hover {
        border-color: #ff4b4b;
    }

    /* 隱藏捲軸 */
    div[role="radiogroup"]::-webkit-scrollbar {
        height: 0px;
        width: 0px;
    }

    </style>
""", unsafe_allow_html=True)

# --- 日期與資料設定 ---
# 字典 Key 改成包含換行符號 \n 的格式
trip_dates = {
    "Day 1\n1/17": (date(2026, 1, 17), day1, "Day 1: 出發 & 移動"),
    "Day 2\n1/18": (date(2026, 1, 18), day2, "Day 2: 金澤市區"),
    "Day 3\n1/19": (date(2026, 1, 19), day3, "Day 3: 合掌村 & 飛驒"),
    "Day 4\n1/20": (date(2026, 1, 20), day4, "Day 4: 新穗高 & 高山"),
    "Day 5\n1/21": (date(2026, 1, 21), day5, "Day 5: 牧歌 & 犬山"),
    "Day 6\n1/22": (date(2026, 1, 22), day6, "Day 6: 名古屋榮商圈"),
    "Day 7\n1/23": (date(2026, 1, 23), day7, "Day 7: 大須 & 名古屋城"),
    "Day 8\n1/24": (date(2026, 1, 24), day8, "Day 8: 回程"),
}

# --- 自動判斷日期邏輯 ---
today = datetime.now().date()
# today = date(2026, 1, 17) # 測試用

default_index = 0
options = list(trip_dates.keys())

# 迴圈尋找今天的日期
for i, key in enumerate(options):
    d = trip_dates[key][0] # 取出日期物件
    if d == today:
        default_index = i
        break

# --- 介面呈現 ---
st.title("🇯🇵 2026 名古屋")

# 橫向按鈕選單
selected_key = st.radio(
    "選擇行程日期",
    options,
    index=default_index,
    horizontal=True,
    label_visibility="collapsed"
)

st.divider()

# --- 讀取並顯示內容 ---
# 從字典中取出對應的資料: (日期物件, 模組, 完整標題)
selected_data = trip_dates[selected_key]
target_module = selected_data[1]
full_title = selected_data[2]

# 顯示詳細標題
st.markdown(f"### {full_title}")

# 執行該 Day 的顯示函式
target_module.show()
