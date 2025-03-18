import streamlit as st

st.title("JD's AI - Auto Video Creation App")
st.write("Welcome to JD's AI! Create videos effortlessly.")

text = st.text_input("Enter your text:")
if st.button("Generate Video"):
    st.write(f"Generating video for: {text}")
    # Add your video generation logic here
