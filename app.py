from analysis import evaluate
import streamlit as st

st.title('CV Analysis - LLM Powered Application')

if 'uploaded_file' not in st.session_state:
    st.session_state.uploaded_file = None

uploaded_file = st.session_state.uploaded_file

if uploaded_file == None:
    st.write("Please upload a CV file to proceed.")
    uploaded_file = st.file_uploader("Choose a file", type="pdf")

if uploaded_file:
    with st.spinner('Processing...'):
        response = evaluate(uploaded_file)

    st.write(response)

st.divider()

st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        color: gray;
        text-align: center;
        padding: 10px 0;
        z-index: 100;
    }
    </style>
    <div class="footer">
        © 2025 Resume Sommelier
        | <a href="https://www.linkedin.com/in/daniel-pereira-2409991bb/" target="_blank">LinkedIn</a>
        | <a href="https://www.github.com/archbaer" target="_blank">GitHub</a>
    </div>
    """,
    unsafe_allow_html=True
)