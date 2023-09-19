import streamlit as st

with st.container():
    st.header("Skills")
    st.write("---")
    st.write("##")
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("1. HTML ")
        st.subheader("2. CSS ")
        st.subheader("3. Javascript ")
        st.subheader("4. Python ")
        st.subheader("5. Streamlit ")
        st.subheader("6. C ")
    
