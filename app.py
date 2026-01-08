# 檔案名稱：app.py
import streamlit as st
from datetime import datetime, date
import pytz # 用於處理時區

# 匯入每一天的模組 (確保這些 .py 檔案都在同一個資料夾)
import day1, day2, day3, day4, day5, day6, day7, day8

# --- 頁面基本設定 ---
st.set_page_config(
    page_title="2026 名古屋",
    page_icon="🇯🇵",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- CSS 優化 (深色模式適應 + 橫向捲動 + 按鈕置中) ---
st.markdown("""
    <style>
    /* 全域按鈕樣式 */
    .stButton button {
        width: 100%;
        border-radius: 20px;
        font-weight: bold;
        border: 1px solid var(--text-color);
        opacity: 0.8;
    }
    
    /* 隱藏預設選單與頁尾 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Day Card 樣式 - 自動適應深淺色 */
    .day-card {
        background-color: var(--secondary-background-color);
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 10px;
        border: 1px solid rgba(128, 128, 128, 0.2);
    }

    /* --- 橫向滑動導覽列 CSS 魔改 --- */
    
    /* 1. 容器設定：橫向排列、可滑動 */
    div[role="radiogroup"] {
        flex-direction: row;
        overflow-x: auto;
        flex-wrap: nowrap !important;
        gap: 8px;
        padding-bottom: 5px;
        -webkit-overflow-scrolling: touch; 
    }

    /* 2. 徹底隱藏 Radio 的圓圈 */
    div[role="radiogroup"] label > div:first-child {
        display: none !important;
    }

    /* 3. 按鈕外觀 (未選中) - 使用變數適應深淺色模式 */
    div[role="radiogroup"] label {
        background-color: var(--secondary-background-color); /* 跟隨系統次要背景色 */
        color: var(--text-color); /* 跟隨系統文字顏色 */
        
        padding: 6px 4px;
        border-radius: 12px;
        border: 1px solid rgba(128, 128, 128, 0.2);
        cursor: pointer;
        transition: all 0.2s;
        
        /* 絕對置中設定 */
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center; 
        
        min-width: 68px; /* 固定寬度 */
        height: 55px;    /* 固定高度 */
    }

    /* 4. 文字內容設定 (修復置中與換行) */
    div[role="radiogroup"] label p {
        font-size: 14px;
        line-height: 1.3;
        font-weight: bold;
        margin: 0px !important; /* 強制移除邊距 */
        padding: 0px !important;
        width: 100%;
        white-space: pre-wrap; /* 允許 \n 換行 */
        text-align: center; /* 文字置中 */
    }

    /* 5. 滑鼠滑過或被選中時的樣式 */
    div[role="radiogroup"] label:hover {
        border-color: #ff4b4b;
        background-color: var(--background-color);
    }

    /* 加強選中時的邊框顯示 */
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

# --- 資料設定 ---
# 格式: Key顯示文字 : (日期物件, 模組, 完整標題)
trip_dates = {
    "Day1\n1/17 六": (date(2026, 1, 17), day1, "Day 1(六): 出發 & 移動"),
    "Day2\n1/18 日": (date(2026, 1, 18), day2, "Day 2(日): 金澤市區"),
    "Day3\n1/19 一": (date(2026, 1, 19), day3, "Day 3(一): 合掌村 & 飛驒"),
    "Day4\n1/20 二": (date(2026, 1, 20), day4, "Day 4(二): 新穗高 & 高山"),
    "Day5\n1/21 三": (date(2026, 1, 21), day5, "Day 5(三): 牧歌 & 犬山"),
    "Day6\n1/22 四": (date(2026, 1, 22), day6, "Day 6(四): 名古屋榮商圈"),
    "Day7\n1/23 五": (date(2026, 1, 23), day7, "Day 7(五): 大須 & 名古屋城"),
    "Day8\n1/24 六": (date(2026, 1, 24), day8, "Day 8(六): 回程"),
}

# --- 自動判斷日期邏輯 (使用日本時間) ---
# 1. 設定日本時區
japan_tz = pytz.timezone('Asia/Tokyo')

# 2. 取得目前的日本日期
today = datetime.now(japan_tz).date()

# --- 測試區 (測試完請註解掉下面這行) ---
# today = date(2026, 1, 18) 
# ------------------------------------

default_index = 0
options = list(trip_dates.keys())

# 3. 比對日期
for i, key in enumerate(options):
    d = trip_dates[key][0]
    if d == today:
        default_index = i
        break

# --- 介面呈現 ---
st.title("🇯🇵 2026 名古屋")
st.caption("1/17~24")
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

# 顯示詳細標題
st.markdown(f"### {full_title}")

# 呼叫對應模組的 show()
target_module.show()
