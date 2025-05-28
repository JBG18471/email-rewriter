import streamlit as st

st.title("Email Rewriter")
original = st.text_area("Paste your original email here:")

if st.button("Rewrite"):
    prompt = f"Rewrite this email to be professional, clear, and concise:\n\n{original}"
    st.write("Rewritten version:")
    st.write("➡️ " + original.upper())  # Placeholder, we'll replace this later
