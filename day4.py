# 檔案名稱：day4.py
import streamlit as st
from utils import get_gmap_link

def show():
    st.header("🍣 Day 2: 金澤文化巡禮")
    st.info("🚧 詳細行程建置中...")
    
    # 下面是你之前給的大綱，先放著備忘
    places = ["近江町市場 (早餐)", "東茶屋街", "兼六園", "21世紀美術館", "金澤 Focus / 金澤車站 (晚餐)", "Uniqlo / 金澤寶可夢"]
    for place in places:
        st.checkbox(place)
    
    st.link_button("📍 導航至：近江町市場", get_gmap_link("Omicho Market"))
