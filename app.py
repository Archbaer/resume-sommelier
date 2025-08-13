import streamlit as st
import pandas as pd
import altair as alt

st.write('Hello world!')

st.title('Resume analysis')
uploaded_file = st.file_uploader("Choose a file", type="pdf")

if 'word' not in st.session_state:
    st.session_state.word = ""

with st.form("word_form"):
    word_input = st.text_input("Enter a word", key="word_input")
    submitted = st.form_submit_button("Add word")
    if submitted:
        st.session_state.word = st.session_state.word_input
        st.write(f"Added word: {st.session_state.word}")

if st.button("Reset"):
    st.session_state.word = ""
    st.session_state.word_input = ""
    st.write('Word reset.')

st.write(f"Current word: {st.session_state.word}")