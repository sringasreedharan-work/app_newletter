#!/usr/bin/env python
# coding: utf-8

# In[3]:


import streamlit as st
import requests
from bs4 import BeautifulSoup
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-flash-latest")

st.title("Article Summarizer: Get Headline & Short Story from a URL")

url = st.text_input("Enter article URL")

if st.button("Get Headline & Story"):
    try:
        r = requests.get(url, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        paragraphs = [p.get_text() for p in soup.find_all("p")]
        article_text = " ".join(paragraphs[:20])

        prompt = f"""
        You are a newsletter writer.
        Summarize the following article into a newsletter format.

        Output must be:
        Heading: <catchy headline>
        Story: <2–3 sentence summary>

        Article:
        {article_text}
        """

        response = model.generate_content(prompt)

        st.subheader("Newsletter")
        st.write(response.text.strip())

    except Exception as e:
        st.error(f"Error: {e}")


# In[ ]:




