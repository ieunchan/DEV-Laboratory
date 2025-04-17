import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from crawling.shop_crawl import coupang_best100

st.title("COUPANG BEST")

best_item = coupang_best100()

for index, item in enumerate(best_item):
    st.write(f"{index+1} : {item}")