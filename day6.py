import streamlit as st
from utils import get_gmap_link

def show():
    # ==========================================
    # 0. 早餐
    # ==========================================
    st.subheader("0️⃣ 早餐 (超商)")
    st.info("💡 11:30 吃燒肉，簡單吃，留點胃口！")
    
    st.divider()

    # ==========================================
    # 1. 唐吉訶德
    # ==========================================
    st.subheader("1️⃣ 唐吉訶德 榮本店")
    st.link_button("🐧 導航：唐吉訶德 榮本店", get_gmap_link("Don Quijote Sakae", "walking"))
    st.markdown("[折價券(滿10,000日元)](https://japanportal.donki-global.com/coupon/cp002.html)")
    st.divider()

    # ==========================================
    # 2. 午餐：馬喰一代 (訂位)
    # ==========================================
    st.subheader("2️⃣ 馬喰一代 名古屋榮")
    
    st.warning("⏰ **預約時間：11:30**")
    st.link_button("🥩 導航：馬喰一代", get_gmap_link("Bakuroichidai Nagoya Sakae", "walking"))

    st.divider()

    # ==========================================
    # 3. SKYLE (服飾雜貨)
    # ==========================================
    st.subheader("3️⃣ SKYLE")
    st.link_button("🛍️ 導航：SKYLE 名古屋", get_gmap_link("SKYLE Nagoya", "walking"))
    with st.expander("🛒 SKYLE 樓層"):
        st.markdown("""
        * **4F**: 3COINS
        * **5F**: UNIQLO
        * **6F**: GU
        """)

    st.divider()

    # ==========================================
    # 4. Onitsuka Tiger
    # ==========================================
    st.subheader("4️⃣ Onitsuka Tiger (鬼塚虎)")
    st.link_button("👟 導航：Onitsuka Tiger 榮", get_gmap_link("Onitsuka Tiger Nagoya", "walking"))
    st.divider()

    # ==========================================
    # 5. 名古屋 PARCO (潮流 & 寶可夢)
    # ==========================================
    st.subheader("5️⃣ 名古屋 PARCO")
    st.caption("東、西、南館")

    st.link_button("🏢 導航：名古屋 PARCO", get_gmap_link("Nagoya PARCO", "walking"))

    with st.expander("⚡ PARCO 樓層"):
        st.markdown("""
        * **東館2F**: **寶可夢中心**
        * **↓西館↓**
        * **B1F**: 無印良品 (MUJI)
        * **1F**: **HARBS** (千層蛋糕)
        * **6F**: ABC-MART
        """)

    st.divider()

    # ==========================================
    # 6. 熱田蓬萊軒 (晚餐 & 買鍋子)
    # ==========================================
    st.subheader("6️⃣ 松坂屋")
    st.error("⚠️ **重要**：16:00 去「南館 10F」排隊拿號碼牌！")
    st.markdown("**Step 1：前往松坂屋南館**")
    st.link_button("🍱 導航：松坂屋名古屋店 南館", get_gmap_link("Matsuzakaya Nagoya South Building", "walking"))

    st.markdown("""
    **Step 2：晚餐 - 熱田蓬萊軒(南館 10F)**
    * **必吃**：鰻魚飯三吃
    * **策略**：4點排號碼後附近逛
    """)
    st.markdown("---")
    st.markdown("**Step 3：購物(等待叫號時)**")
    st.markdown("""
    * **南館3F**:領折價券(5%)、**退稅櫃台** 
    * **南館4F-6F**: Yodobashi電器
    """)

if __name__ == "__main__":
    show()
