import streamlit as st
import pandas as pd
from utils import get_gmap_link, show_food_table

def show():
    
    st.caption("3/14")
    # --- 飛機 ---
    with st.container(border=True):
        st.markdown("### 🛫 中華航空 CI 154")
        col1, col2 = st.columns(2)
        col1.write("7:35 TPE 起飛 → 11:05 NGO 抵達")

    # --- Step 1: 機場到名古屋 (電車) ---
    st.subheader("1️⃣ 機場 ➔ 名鐵名古屋站")
    
    # [修正] 紅色提醒：加入 Highwaybus 連結
    st.warning("⚠️ 重要提醒：確認車次後，巴士 **發車前 30 分鐘** 付款取票！[巴士付款頁面](https://www.highwaybus.com/gp/reference/refCertification?refCertSelected=selected)")
    st.info("💡 搭乘 **名鐵電車 (Meitetsu Line)** 前往市區")
    
    # [修正] 時刻表：加入名鐵官網連結與現金提醒
    with st.expander("🚆 點我看：名鐵電車時刻表 (11:45-13:00)", expanded=False):
        st.markdown("機器買只能用現金，建議搭乘 μ-Sky (+450円)")
        st.markdown("[官網時刻表](https://trainbus.meitetsu.co.jp/meitetsu-transfer-zh-tw/pc/transfer/DepArrTimeList?snode=00009406&gnode=00004372&date=2026-03-14&depTime=12)")
        schedule_data = [
             {"發車": "11:47", "抵達": "12:24", "搭乘時間": "37分", "車種": "特急"},
             {"發車": "11:52", "抵達": "12:40", "搭乘時間": "48分", "車種": "準急"},
             {"發車": "12:07", "抵達": "12:35", "搭乘時間": "28分", "車種": "μ-Sky"},
             {"發車": "12:17", "抵達": "12:54", "搭乘時間": "37分", "車種": "特急"},
             {"發車": "12:22", "抵達": "13:10", "搭乘時間": "48分", "車種": "準急"},
             {"發車": "12:37", "抵達": "13:05", "搭乘時間": "28分", "車種": "μ-Sky"},
             {"發車": "12:47", "抵達": "13:24", "搭乘時間": "37分", "車種": "特急"},
             {"發車": "12:52", "抵達": "13:40", "搭乘時間": "48分", "車種": "準急"},
        ]
        
        df = pd.DataFrame(schedule_data)
        st.dataframe(
            df, 
            hide_index=True, 
            use_container_width=True,
            column_order=["發車", "抵達", "搭乘時間", "車種"]
        )

    # --- Step 2: 轉乘與購物 ---
    st.subheader("2️⃣ 轉乘：名鐵巴士中心")
    
    # [修正] 這裡也補上 Highwaybus 連結
    st.markdown("🔗 [巴士預約付款頁面](https://www.highwaybus.com/gp/reference/refCertification?refCertSelected=selected)")

    st.markdown("""
    **動線指引：**
    1. **[中央札口]** 出站
    2. 搭手扶梯(單人)後左轉
    3. 走到底右轉(出百貨、遇彩卷行)
    4. 星巴克右轉(路在左  百貨在右)
    5. 直走到大型人偶 手扶梯上3F
    """)
    
    st.link_button("📍 導航：名鐵巴士中心 (6號乘車處)", get_gmap_link("名鐵巴士中心 1 Chome-2-4 Meieki, Nakamura Ward, Nagoya, Aichi 450-0002日本", "transit"), type="primary")

    

    # --- Step 3: 巴士前往金澤 ---
    st.subheader("3️⃣ 高速巴士 ➔ 金澤")
    st.write("🚌 **乘車處：3樓 6號月台 ** ")
    st.info("💡 在附近購買點心、晚餐 (稍後車上吃)")
    # --- Step 4: 住宿資訊 ---
    st.divider()
    # [修正] 標題改為飯店名稱
    st.subheader("🏨 金澤站西口大和Roynet飯店")
    
    # [修正] 導航按鈕移至這裡
    st.link_button("🗺️ 導航", get_gmap_link("1 Chome-12-17 Hirooka, Kanazawa, Ishikawa 920-0031日本", "walking"))
    
    with st.container(border=True):
        st.text("Daiwa Roynet Hotel KANAZAWAEKI-NISHIGUCHI")
        st.text("ダイワロイネットホテル 金沢駅西口")
        st.text("📍 日：〒920-0031 石川県金沢市広岡1-12-17")
        st.text("📍 英：1-12-17, Hirooka, Kanazawa-shi, Ishikawa 920-0031")


    # 在 show() 函式的最後面加入：
    show_food_table("金澤")
