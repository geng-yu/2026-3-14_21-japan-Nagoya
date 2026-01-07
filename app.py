import streamlit as st
import pandas as pd
from datetime import datetime, date

# --- 設定頁面配置 (必須在第一行) ---
st.set_page_config(
    page_title="2026 名古屋北陸行",
    page_icon="🇯🇵",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- 自定義 CSS (讓手機版更好看) ---
st.markdown("""
    <style>
    .stButton button {
        width: 100%;
        border-radius: 20px;
        font-weight: bold;
    }
    .stAlert {
        padding: 10px;
        border-radius: 15px;
    }
    /* 隱藏預設選單和 footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- 日期判斷邏輯 ---
# 定義旅遊日期範圍
trip_dates = {
    "1/17 (六) 出發日": date(2026, 1, 17),
    "1/18 (日) Day 2": date(2026, 1, 18),
    "1/19 (一) Day 3": date(2026, 1, 19),
    "1/20 (二) Day 4": date(2026, 1, 20),
    "1/21 (三) Day 5": date(2026, 1, 21),
    "1/22 (四) Day 6": date(2026, 1, 22),
    "1/23 (五) Day 7": date(2026, 1, 23),
    "1/24 (六) 回程": date(2026, 1, 24),
}

# 取得今天日期
today = datetime.now().date()
# today = date(2026, 1, 17) # 解除註解可用來測試特定日期

# 決定預設選項
default_index = 0
options = list(trip_dates.keys())
for i, (label, d) in enumerate(trip_dates.items()):
    if d == today:
        default_index = i
        break

# --- 頂部導航列 ---
st.title("🇯🇵 2026 名古屋・北陸之旅")
selected_day = st.selectbox("📅 選擇行程日期", options, index=default_index)

# --- Google Map 連結產生器 ---
def get_gmap_link(query, mode="transit"):
    # mode: driving, walking, transit (大眾運輸)
    base_url = "https://www.google.com/maps/dir/?api=1"
    # destination 留空則由使用者輸入，這裡我們直接指定目的地
    # origin 留空則預設為使用者當前位置
    return f"{base_url}&destination={query}&travelmode={mode}"

# --- 內容顯示區 ---

if selected_day == "1/17 (六) 出發日":
    st.header("✈️ Day 1: 啟程前往金澤")
    
    # 1. 航班資訊
    with st.container(border=True):
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown("### CX530")
            st.caption("國泰航空")
        with col2:
            st.write("🛫 **12:00** 台北 TPE")
            st.write("🛬 **15:35** 名古屋 NGO")
    
    st.divider()

    # 2. 機場移動與購票提醒
    st.subheader("🚌 中部機場 ➔ 名鐵巴士中心")
    
    st.warning("⚠️ **重要提醒：巴士付款**\n\n巴士預約：17:30 或 18:30。\n**發車前 30 分鐘需付款取票！")

    # 地圖按鈕：名鐵巴士中心
    st.link_button(
        "📍 導航：名鐵巴士中心 (3F 6號乘車處)", 
        get_gmap_link("Meitetsu Bus Center", "transit"),
        type="primary"
    )

    # 3. 名鐵電車時刻表 (Expander)
    with st.expander("🚆 點我看：名鐵電車時刻表 (機場→名古屋)", expanded=True):
        st.markdown("""
        **買票：名鐵名古屋站 (Meitetsu Nagoya)** *註：μ = μ-Sky 特急 (全車指定席 +450円)*
        """)
        
        # 製作表格數據
        schedule_data = [
            {"發車": "16:07", "抵達": "16:35", "分": "28", "備註": "μ (+450円)"},
            {"發車": "16:17", "抵達": "16:54", "分": "37", "備註": "特急"},
            {"發車": "16:21", "抵達": "17:10", "分": "49", "備註": "準急"},
            {"發車": "16:36", "抵達": "17:05", "分": "29", "備註": "μ (+450円)"},
            {"發車": "16:44", "抵達": "17:24", "分": "40", "備註": "特急"},
            {"發車": "16:51", "抵達": "17:40", "分": "49", "備註": "準急"},
            {"發車": "17:06", "抵達": "17:35", "分": "29", "備註": "μ (+450円)"},
            {"發車": "17:14", "抵達": "17:54", "分": "40", "備註": "特急"},
            {"發車": "17:21", "抵達": "18:10", "分": "49", "備註": "準急"},
            {"發車": "17:36", "抵達": "18:05", "分": "29", "備註": "μ (+450円)"},
        ]
        
        df = pd.DataFrame(schedule_data)
        st.dataframe(
            df, 
            hide_index=True, 
            column_config={
                "備註": st.column_config.TextColumn(
                    "車種/費用",
                    help="μ需要加購μ-ticket",
                    validate="^μ.*" # 簡單的 regex 驗證(這裡僅作展示)
                )
            },
            use_container_width=True
        )
        st.caption("建議搭乘 μ-Sky 或 特急，時間較省。車上可吃點心 🍘")

    # 4. 名古屋站內動線
    st.info("🚶 **站內動線 (重要)**\n\n1. 到達名鐵名古屋站 (B1F)\n2. 找 **[西改札口]** 出站\n3. 搭電梯至 **3F** (名鐵巴士中心)")

    st.divider()

    # 5. 抵達金澤與住宿
    st.subheader("🏨 住宿：金澤大和西口")
    st.write("預計搭乘巴士前往金澤。")
    
    # 地圖按鈕：金澤住宿
    st.link_button(
        "📍 導航：金澤大和西口 (Daiwa Roynet Hotel)", 
        get_gmap_link("Daiwa Roynet Hotel Kanazawa-Miyabi", "walking"), # 假設是這間，可修正
        type="primary"
    )

elif selected_day == "1/18 (日) Day 2":
    st.info("🚧 Day 2 行程建置中...")
    # 這裡放入第二天的代碼

# ... 其他日期的 elif 區塊 ...

else:
    st.write("請選擇日期查看詳細行程。")
