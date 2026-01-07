# 檔案名稱：app.py
import streamlit as st
from datetime import datetime, date

# 匯入每一天的模組
import day1, day2, day3, day4, day5, day6, day7, day8

# --- 頁面基本設定 ---
st.set_page_config(
    page_title="2026 名古屋",
    page_icon="🇯🇵",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- CSS 優化 (修復置中與深色模式) ---
st.markdown("""
    <style>
    /* 全域按鈕樣式 */
    .stButton button {
        width: 100%;
        border-radius: 20px;
        font-weight: bold;
        border: 1px solid var(--text-color); /* 改用變數，適應深淺色 */
        opacity: 0.8;
    }
    
    /* 隱藏預設選單與頁尾 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Day Card 樣式 - 使用變數適應深色模式 */
    .day-card {
        background-color: var(--secondary-background-color);
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 10px;
        border: 1px solid rgba(128, 128, 128, 0.2);
    }

    /* --- 橫向滑動導覽列 CSS (核心修改) --- */
    
    /* 1. 容器設定 */
    div[role="radiogroup"] {
        flex-direction: row;
        overflow-x: auto;
        flex-wrap: nowrap !important;
        gap: 8px;
        padding-bottom: 5px;
        -webkit-overflow-scrolling: touch; 
    }

    /* 2. 隱藏 Radio 的圓圈 (這是造成偏掉的主因之一，必須徹底隱藏) */
    div[role="radiogroup"] label > div:first-child {
        display: none !important;
    }

    /* 3. 按鈕外觀 (未選中) - 改用 CSS 變數 */
    div[role="radiogroup"] label {
        /* 使用 secondary-background-color (在深色模式是深灰，淺色是淺灰) */
        background-color: var(--secondary-background-color);
        color: var(--text-color); /* 文字顏色自動跟隨系統 */
        
        padding: 6px 4px; /* 稍微縮小內距 */
        border-radius: 10px;
        border: 1px solid rgba(128, 128, 128, 0.2); /* 淡淡的邊框 */
        cursor: pointer;
        transition: all 0.2s;
        
        /* 絕對置中設定 */
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center; 
        
        min-width: 68px; /* 固定寬度 */
        height: 52px;    /* 固定高度 */
    }

    /* 4. 文字內容設定 (修復置中) */
    div[role="radiogroup"] label p {
        font-size: 14px;
        line-height: 1.3;
        font-weight: bold;
        margin: 0px !important; /* 強制移除預設邊距 */
        padding: 0px !important;
        width: 100%;
        white-space: pre-wrap; /* 允許換行 */
        text-align: center; /* 文字置中 */
    }

    /* 5. 被選中/滑鼠滑過時的樣式 */
    div[role="radiogroup"] label:hover {
        border-color: #ff4b4b; /* 紅色邊框 */
        background-color: var(--background-color); /* 稍微變色 */
    }

    /* 如果被選中 (利用 Streamlit 內部的 checked 狀態樣式特徵) 
       注意：Streamlit 選中時會自動改變字體顏色，我們這裡加強邊框 */
    div[role="radiogroup"] label[data-baseweb="radio"] {
        border-color: #ff4b4b !important;
        background-color: var(--background-color) !important;
    }

    /* 隱藏捲軸 */
    div[role="radiogroup"]::-webkit-scrollbar {
        display: none;
    }

    </style>
""", unsafe_allow_html=True)

# --- 日期與資料設定 ---
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

default_index = 0
options = list(trip_dates.keys())

for i, key in enumerate(options):
    d = trip_dates[key][0]
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

# --- 顯示內容 ---
selected_data = trip_dates[selected_key]
target_module = selected_data[1]
full_title = selected_data[2]

st.markdown(f"### {full_title}")
target_module.show()
