import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image # 이미지
import os

st.write("현재 경로: ", os.getcwd())
st.write("../ 경로: ", os.path.abspath("../"))
