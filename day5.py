import streamlit as st
from utils import get_gmap_link

def show():

    # ==========================================
    # 1. 牧歌之里 (玩雪 & 午餐)
    # ==========================================
    st.subheader("1️⃣ 牧歌之里")
    st.markdown("**Step 1：車機導航**")
    st.code("電話：0575-73-2888", language="text")
    st.markdown("**Step 2：手機導航**")
    st.link_button("⛄ 導航：牧歌之里", get_gmap_link("Bokka no Sato", "driving"))

    with st.expander("🍽️ 餐點"):
        st.markdown("""
        * **午餐**：園區內餐廳提供飛驒牛料理、蛋包飯。
        * **必吃**：牧場自家製霜淇淋、牛奶布丁 (非常濃郁)。
        """)

    st.divider()

    # ==========================================
    # 2. 犬山城 (國寶名城)
    # ==========================================
    st.subheader("2️⃣ 犬山城")
    st.warning("⚠️ **時間**：16:30 最後入場，17:00 關門")

    st.markdown("**Step 1：車機導航**")
    st.caption("目的地：犬山城第1停車場")
    st.code("MapCode：70 157 836*35\n電話：0568-61-1711", language="text")

    st.markdown("**Step 2：手機導航**")
    st.link_button("🏯 導航：犬山城第1停車場", get_gmap_link("Inuyama Castle Parking Lot 1", "driving"))

    st.divider()

    # ==========================================
    # 3. 還車 (TOYOTA 白川店)
    # ==========================================
    st.subheader("3️⃣ 名古屋白川店還車")
    st.markdown("記得附近加滿油再還車")
    
    st.markdown("**Step 1：車機導航**")
    st.caption("TOYOTA租車 名古屋白川店")
    st.code("電話：052-204-0100\nMapCode：428 849 4*83", language="text")

    st.markdown("**Step 2：手機導航**")
    st.link_button("🚗 導航：Toyota租車 白川店", get_gmap_link("Toyota Rent a Car Shirakawa Shop", "driving"))
    
    st.caption("加油站建議：Google Map 搜尋附近的 \"Gas Station\"。")

    st.divider()

    # ==========================================
    # 4. 飯店 Check-in
    # ==========================================
    st.subheader("4️⃣ 榮弗爾札飯店 (Hotel Forza)")
    st.markdown("還車後，步行前往飯店 Check-in。")

    st.markdown("**Step 1：步行導航**")
    st.link_button("🏨 導航：Hotel Forza Nagoya Sakae", get_gmap_link("Hotel Forza Nagoya Sakae", "walking"))

    st.divider()

    # ==========================================
    # 5. 晚餐 (味噌豬排)
    # ==========================================
    st.subheader("5️⃣ 晚餐：黑豚屋 (Kurobutaya)")
    st.markdown("名古屋必吃美食：味噌豬排")

    st.markdown("**Step 1：步行導航**")
    st.link_button("🐷 導航：名古屋味噌豬排黑豚屋", get_gmap_link("Kurobutaya Ramuchii Nagoya", "walking"))

    with st.expander("🥢 推薦菜單"):
        st.markdown("""
        * **味噌炸豬排定食**：濃郁的紅味噌醬汁淋在酥脆豬排上
        * **蔥花味噌豬排**：加上大量蔥花，口感更清爽
        """)

if __name__ == "__main__":
    show()
