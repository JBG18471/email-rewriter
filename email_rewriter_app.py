import streamlit as st
import openai
import os

st.set_page_config(page_title="Email Rewriter", layout="centered")

st.title("📧 Email Rewriter (OpenAI-powered)")
st.markdown("Paste your original email below and get a professional, concise version:")

# Get the API key from Streamlit secrets
api_key = st.secrets.get("OPENAI_API_KEY")

email_input = st.text_area("✍️ Paste your original email here:", height=300)

if st.button("🔁 Rewrite Email"):
    if not api_key:
        st.error("OpenAI API key not found. Please set it in Streamlit Secrets.")
    elif not email_input.strip():
        st.warning("Please paste your email before clicking 'Rewrite Email'.")
    else:
        try:
            openai.api_key = api_key

            with st.spinner("Rewriting your email..."):
                response = openai.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a helpful assistant that rewrites emails in a business professional tone. Make them clear and concise."
                        },
                        {"role": "user", "content": f"Rewrite this email:\n\n{email_input.strip()}"}
                    ],
                    temperature=0.7,
                    max_tokens=500
                )

                rewritten_email = response.choices[0].message.content.strip()
                st.success("✅ Here's your rewritten email:")
                st.text_area("📬 Rewritten Email", rewritten_email, height=300)

        except Exception as e:
            st.error(f"❌ Something went wrong: {e}")
