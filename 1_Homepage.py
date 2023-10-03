
import requests
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie



# Page title with emoji importing
st.set_page_config(page_title="My webpage", page_icon="🖐 ", layout="wide")


# func for animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("C:\\Users\\sneha\\OneDrive\\Desktop\\Portfolio website\\css\\style.css")
# loading assets
lottie_coding = load_lottieurl(
    "https://lottie.host/e003551b-5ea6-4ff8-86b4-d30423061257/mLfxbyTFPj.json"
)


# header section
with st.container():
    st.subheader("Heiya!, This is Sneha :wave:")
    st.title("A Techophile | Codegeek | Toastmaster")
    st.write("Final year Student at GHRCACS")
    st.write("[Checkout Linkedln>](https://www.linkedin.com/in/sneha-kumari-3483169a/)")


# About me
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About me")
        st.write("##")
        st.write(
            """I am a Final year student pursuing Bachelor of Computer Applications at GH Raisoni college of Arts Commerce & Science, Pune, to learn and explore of world of IT along with Administrative and Management skills. 

- I am very passionate about Cybersecurity and networing. 
  Currently I'm training for Comptia Network+ exam

- I enjoy competitive coding and I actively practice as well compete on codechef as well as hackerrank.

- I enjoy coding in Python. I'm familiar with C and C++ as well as MySQL. I know HTML, CSS and 
  Javascript. Also I can work on Linux Ubuntu.

- Apart from that I'm a Toastmaster at Raisoni Ace Toastmasters Club, I actively participate in roleplays 
   and currently I'm completed my Level 1 of pathway: Motivational Strategis

- I love doing Art and Craft work, Sketching, Painting especially on Canvas."""

        )
    with right_column:
     st_lottie(lottie_coding, height=300, key="coding")



st.sidebar.success("Main menu")
