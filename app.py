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

# --- 手機版 CSS 優化 ---
st.markdown("""
    <style>
    .stButton button {
        width: 100%;
        border-radius: 20px;
        font-weight: bold;
        border: 1px solid #ddd;
    }
    h2, h3 { padding-top: 10px; padding-bottom: 10px; }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .day-card {
        background-color: #f9f9f9;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 10px;
        border: 1px solid #eee;
    }
    </style>
""", unsafe_allow_html=True)

# --- 日期設定 ---
trip_dates = {
    "1/17 (六) Day 1: 出發 & 移動": (date(2026, 1, 17), day1),
    "1/18 (日) Day 2: 金澤市區": (date(2026, 1, 18), day2),
    "1/19 (一) Day 3: 合掌村 & 飛驒": (date(2026, 1, 19), day3),
    "1/20 (二) Day 4: 新穗高 & 高山": (date(2026, 1, 20), day4),
    "1/21 (三) Day 5: 牧歌 & 犬山": (date(2026, 1, 21), day5),
    "1/22 (四) Day 6: 名古屋榮商圈": (date(2026, 1, 22), day6),
    "1/23 (五) Day 7: 大須 & 名古屋城": (date(2026, 1, 23), day7),
    "1/24 (六) Day 8: 回程": (date(2026, 1, 24), day8),
}

# --- 自動判斷日期邏輯 ---
today = datetime.now().date()
# today = date(2026, 1, 17) # 測試用

default_index = 0
options = list(trip_dates.keys())
for i, (label, (d, module)) in enumerate(trip_dates.items()):
    if d == today:
        default_index = i
        break

# --- 介面呈現 ---
st.title("🇯🇵 2026 名古屋・北陸之旅")
selected_option = st.selectbox("📅 選擇行程日期", options, index=default_index)
st.divider()

# --- 呼叫對應的 Day 模組 ---
# 這裡會去執行該 Day 檔案裡的 show() 函式
target_module = trip_dates[selected_option][1]
target_module.show()
