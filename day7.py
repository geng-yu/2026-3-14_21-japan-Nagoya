import streamlit as st
from utils import get_gmap_link, show_food_table

def show():
    # ==========================================
    # 1. 早餐：Konparu
    # ==========================================
    st.subheader("1️⃣ Konparu 大須本店 (早餐)")
    st.markdown("**Step 1：步行導航**")
    st.link_button("☕ 導航：Konparu 大須本店", get_gmap_link("Konparu Osu", "walking"))

    with st.expander("🥪 必吃菜單"):
        st.markdown("""
        * **炸蝦三明治** 、 **冰咖啡**
        """)

    st.divider()

    # ==========================================
    # 2. 大須商店街
    # ==========================================
    st.subheader("2️⃣ 大須商店街")

    st.markdown("**Step 1：步行導航 (從 Konparu 出發)**")
    st.caption("建議路線：大須觀音 → 商店街 → 招財貓")
    st.link_button("🏮 導航：大須觀音寺", get_gmap_link("Osu Kannon", "walking"))
    
    st.markdown("**Step 2：地標導航**")
    st.link_button("🐱 導航：巨型招財貓", get_gmap_link("Osu Maneki Neko", "walking"))

    with st.expander("🍡 小吃 & 買"):
        st.markdown("""
        * **李桑的台灣名物**：「辣味鹽酥雞」
        * **包包亭**：肉包與煎包
        * **大須五平餅**：味噌烤米餅
        * **Alice on Wednesday**：愛麗絲夢遊仙境主題店 (特殊零食)
        * **Seria (百元店)**：大型購物中心裡
        """)

    st.divider()

    # ==========================================
    # 3. 名古屋城 (地鐵移動)
    # ==========================================
    st.subheader("3️⃣ 名古屋城")

    st.markdown("**Step 1：搭乘地鐵 (名城線)**")
    st.markdown("""
    1. 走到 **「上前津站」** (招財貓旁邊就是入口)
    2. 搭乘 **名城線 (右回 / 紫色線)**
    3. 下車：**「名古屋城站」** (Nagoyajo) 7號出口
    """)
    st.link_button("🚇 導航：上前津站 (入口)", get_gmap_link("Kamimaezu Station", "walking"))

    st.markdown("**Step 2：抵達景點**")
    st.link_button("🏯 導航：名古屋城 (正門)", get_gmap_link("Nagoya Castle Main Gate", "walking"))

    with st.expander("🍦 金查橫丁 (美食街)"):
        st.markdown("""
        * **金箔霜淇淋** 、 **矢場味噌豬排**
        * **伴手禮**：印有金鯱圖案的蝦餅
        """)

    st.divider()

    # ==========================================
    # 4. mont-bell & 晚餐
    # ==========================================
    st.subheader("4️⃣ 榮商圈：購物(Montbell)&晚餐")
    st.caption("搭地鐵回到「榮站」或「矢場町站」")

    st.markdown("**Step 1：購物 - 中日大樓**")
    st.link_button("⛰️ 導航：中日大樓", get_gmap_link("mont-bell Nagoya Sakae", "walking"))
    with st.expander("🛒 中日樓層"):
        st.markdown("""
        * **1F** :藍瓶咖啡、HOKA、RedWing
        * **2F**：Montbell、退稅櫃檯
        """)
    st.markdown("**Step 2：晚餐 - 世界的山將**")
    st.link_button("🍗 導航：世界的山將 本店", get_gmap_link("Sekai no Yamachan Honten", "walking"))

    with st.expander("🍻 世界的山將必吃"):
        st.markdown("""
        * **幻之手羽先**：胡椒辣味雞翅，建議一人先點 5 支
        * **味噌串炸**：配啤酒絕佳
        * **台灣拉麵具**：名古屋特色的台灣拉麵炒料
        """)

    st.divider()

    # ==========================================
    # 5. 夜景 & 甜點外帶
    # ==========================================
    st.subheader("5️⃣ 夜景 & HARBS 甜點")

    st.markdown("**Step 1：Oasis 21 (水的宇宙船)**")

    st.link_button("🌃 導航：Oasis 21", get_gmap_link("Oasis 21", "walking"))

    st.markdown("**Step 2：HARBS 外帶 (LACHIC店)**")
    st.warning("⚠️ 注意打烊時間 (通常 21:00)")
    st.link_button("🍰 導航：HARBS 名古屋 LACHIC", get_gmap_link("HARBS Nagoya LACHIC", "walking"))

    with st.expander("🍓 必吃蛋糕"):
        st.markdown("""
        * **水果千層蛋糕** 、 **草莓蛋糕**
        """)

if __name__ == "__main__":
    show()
