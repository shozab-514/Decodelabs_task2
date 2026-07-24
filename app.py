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
st.markdown("""
# 🚀 AI Marketing Copy Generator
### Generate Professional Marketing Copy using **Google Gemini AI**
""")

st.markdown("""
<style>

.stApp{
background: linear-gradient(135deg,#0f172a,#1e293b,#0f766e);
}

h1{
text-align:center;
color:Gold;
}

h3{
text-align:center;
color:Gold;
}

label{
font-weight:bold;
}

div[data-baseweb="select"]{
border-radius:12px;
}

.stTextInput input{
border-radius:12px;
}

.stTextArea textarea{
border-radius:12px;
}

.stButton>button{

width:100%;
height:55px;

background:#14b8a6;

color:Gold;

font-size:20px;

font-weight:bold;

border-radius:12px;

border:none;
}

.stButton>button:hover{

background:#0f766e;

color:Gold;

}

div[data-testid="stDownloadButton"] button{

width:100%;

background:#2563eb;

color:Gold;

border-radius:10px;

}

</style>
""",unsafe_allow_html=True)
with st.sidebar:

    st.image("https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png",width=100)

    st.title("About")

    st.write("""
AI Marketing Copy Generator

Powered by

Google Gemini

Python

Streamlit
""")

    st.success("Project 2")
    product = st.text_input("📦 Product Name")

description = st.text_area("📝 Product Description")

platform = st.selectbox(
"🌍 Platform",
["Instagram","LinkedIn","Email"]
)

tone = st.selectbox(
"🎭 Tone",
[
"Professional",
"Friendly",
"Luxury",
"Funny",
"Witty & Energetic"
]
)
temperature = st.slider(
"🔥 Temperature",
0.0,
1.0,
0.7
)

top_p = st.slider(
"🎯 Top P",
0.0,
1.0,
0.9
)
if st.button("✨ Generate Marketing Copy"):
    st.balloons()

st.success("Marketing Copy Generated Successfully!")
st.balloons()

st.success("Marketing Copy Generated Successfully!")

st.markdown("---")

st.markdown(
"<center>Made with ❤️ using Streamlit & Google Gemini</center>",
unsafe_allow_html=True
)

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
