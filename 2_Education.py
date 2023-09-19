from PIL import Image
import requests
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie

# education
with st.container():
    st.header("Education")
    st.write("---")
    st.write("##")
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("GH Raisoni college of Arts, Commerce and Science")
        st.write(
            """Bachelor of Business Administration - Computer Application   - CGPA: 8.6"""
        )
        st.subheader("Kendriya Vidyalaya Ganeshkhind, Pune ")
        st.write("""Higher Secondary (PCM) with Computer Science - 77.6%""")
        st.subheader("Kendriya Vidyalaya Ganeshkhind, Pune ")
        st.write("""Senior Secondary - 86.2%""")
