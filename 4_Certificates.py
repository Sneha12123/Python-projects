from PIL import Image
import requests
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie


img_1 = Image.open("C:\\Users\\sneha\\OneDrive\\Desktop\\website\\images\\img1.png")
img_2 = Image.open("C:\\Users\\sneha\\OneDrive\\Desktop\\website\\images\\img2.png")
img_3 = Image.open("C:\\Users\\sneha\\OneDrive\\Desktop\\website\\images\\img3.png")
img_4 = Image.open("C:\\Users\\sneha\\OneDrive\\Desktop\\website\\images\\img4.png")

with st.container():
    st.header("Certificates and Accomplishments")
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_1)
    with text_column:
        st.subheader("Participated in State level Debate Competition")
        st.write(
            """It was a pleasure participating in State level Debate competition held on February 2023, where
            the topic was "uniform civil code"."""
        )
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_2)
    with text_column:
        st.subheader("Participated in Antaragini event, as Anchor in college")
        st.write("""I was the Anchor for the anual Antaragini event held in college.""")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_3)
    with text_column:
        st.subheader("Participated and won in Tabletopics Speech contest on Club level")
        st.write(
            """"I won the first place in Impromptu speech contest, where the topic was: "We have built more walls than bridges". 
                 Here I practiced thinking and speaking on your feet. """
        )
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_4)
    with text_column:
        st.subheader("Participated in Intercollege Commerce fest: FINATEX 23 ")
        st.write(
            """"This was a commerce event held on 24th-25th March 2023, in (Christ Deemed to be University) Lavasa, Pune.  """
        )
# Contact
