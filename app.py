import os
import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types
import streamlit as st
from google import genai

client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

# Load API Key
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

st.set_page_config(
    page_title="AI Marketing Copy Generator",
    page_icon="🚀",
    layout="centered"
)

st.title("🚀 AI Marketing Copy Generator")
st.write("Generate marketing copy using Gemini AI")

# Inputs
product = st.text_input("Product Name")

description = st.text_area("Product Description")

platform = st.selectbox(
    "Select Platform",
    ["Instagram", "LinkedIn", "Email"]
)

tone = st.selectbox(
    "Select Tone",
    [
        "Professional",
        "Friendly",
        "Luxury",
        "Funny",
        "Witty & Energetic"
    ]
)

temperature = st.slider(
    "Temperature",
    0.0,
    1.0,
    0.7,
    0.1
)

top_p = st.slider(
    "Top P",
    0.0,
    1.0,
    0.9,
    0.1
)

if st.button("Generate Marketing Copy"):

    prompt = f"""
You are an expert marketing copywriter.

Create marketing copy.

Product Name:
{product}

Product Description:
{description}

Platform:
{platform}

Tone:
{tone}

Requirements:

- Instagram → Caption + Emojis + Hashtags
- LinkedIn → Professional post
- Email → Subject + Greeting + Body + CTA

Maintain a {tone} tone.
"""

    with st.spinner("Generating..."):

        try:

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=temperature,
                    top_p=top_p,
                    max_output_tokens=500
                )
            )

            st.success("Generated Successfully")

            st.text_area(
                "Generated Copy",
                response.text,
                height=300
            )

            st.download_button(
                "Download Output",
                response.text,
                file_name="marketing_copy.txt"
            )

        except Exception as e:
            st.error(e)