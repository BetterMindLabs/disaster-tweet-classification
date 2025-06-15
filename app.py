import streamlit as st
import google.generativeai as genai

# Load Gemini API Key
api_key = st.secrets["api_keys"]["google_api_key"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# App UI
st.set_page_config(page_title="Disaster-Tweet Classifier")
st.title("Disaster-Tweet Classifier")
st.write("Classify tweets as disaster-relevant or irrelevant to assist emergency response teams.")

# Input field
tweet_text = st.text_area("Enter tweet text", height=150, placeholder="e.g. Fire has broken out near 5th Ave. Smoke everywhere...")

# Button
if st.button("Classify"):
    if not tweet_text.strip():
        st.warning("Please enter tweet content.")
    else:
        with st.spinner("Classifying..."):
            prompt = f"""
You are a binary classification model that processes tweets during emergencies.
Given a tweet, return the following:

Classification: Relevant or Irrelevant  
Reason: Short explanation (1-2 lines)

Tweet:
\"\"\"{tweet_text}\"\"\"
"""

            response = model.generate_content(prompt)
            result = response.text.strip()

            st.subheader("Classification Result")
            st.write(result)
