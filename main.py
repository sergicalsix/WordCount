import streamlit as st
from animation import *
import time

st.set_page_config(
   page_title="単語カウント",
   page_icon=":shark:",
 )

st.title("単語カウント")
st.write('<style>h1 {color: green;}</style>', unsafe_allow_html=True)

#st.image('img/icons/sch.png')

user_option = st.sidebar.radio(
    "属性を選択してください",
)


st.markdown("""-----""")

st.sidebar.markdown("""-----""")

go = st.sidebar.checkbox('実行!!')

if go == True :
    st.info("hoge")

    
        
