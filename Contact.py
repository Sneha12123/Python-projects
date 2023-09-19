from PIL import Image
import requests
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie

# css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("C:\\Users\\sneha\\OneDrive\\Desktop\\Portfolio website\\css\\style.css")




with st.container():
    st.header("Get in contact with me!")
    st.write("---")
    st.write("##")

    contact_form = """
<form action="https://formsubmit.co/snehathaur2004@gmail.com" method="POST">
     <input type="hidden" name="_captvha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>"""

left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()
