# 🚀 AI Marketing Copy Generator

## 📌 Project Overview

The **AI Marketing Copy Generator** is a Generative AI application developed using **Python**, **Google Gemini API**, and **Streamlit**. It generates engaging marketing content for different platforms by using dynamic prompting and configurable AI parameters.

Users can enter product details, choose a target platform, select a writing tone, and customize AI creativity using **Temperature** and **Top_P** settings.

---

## ✨ Features

* Generate AI-powered marketing copy
* Dynamic Prompt Engineering
* Multiple Platform Support

  * Instagram
  * LinkedIn
  * Email
* Multiple Writing Tones

  * Professional
  * Friendly
  * Luxury
  * Funny
  * Witty & Energetic
* Temperature Control
* Top_P Control
* Download Generated Output
* User-Friendly Streamlit Interface
* Secure API Key Management using `.env`

---

## 🛠️ Technologies Used

* Python 3
* Streamlit
* Google Gemini API
* google-genai SDK
* python-dotenv

---

## 📂 Project Structure

```text
AI-Marketing-Copy-Generator/
│
├── app.py
├── main.py
├── .env
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/AI-Marketing-Copy-Generator.git
```

```bash
cd AI-Marketing-Copy-Generator
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure API Key

Create a **.env** file in the project folder.

```text
GEMINI_API_KEY=YOUR_API_KEY
```

Replace `YOUR_API_KEY` with your Google AI Studio Gemini API key.

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

If Streamlit is not recognized, run:

```bash
python -m streamlit run app.py
```

---

## 🧠 How It Works

1. Enter the Product Name.
2. Enter the Product Description.
3. Select the Target Platform.
4. Select the Desired Tone.
5. Adjust Temperature and Top_P.
6. Click **Generate Marketing Copy**.
7. AI generates optimized marketing content.
8. Download the generated output if needed.

---

## 📸 Supported Platforms

* Instagram
* LinkedIn
* Email

---

## 🎯 AI Parameters

### Temperature

Controls creativity.

* Low → More focused and consistent.
* High → More creative and diverse.

### Top_P

Controls token selection diversity.

* Lower values produce more focused outputs.
* Higher values produce more varied responses.

---

## 📌 Example Input

**Product Name**

```
EcoBottle X
```

**Product Description**

```
A smart self-cleaning insulated water bottle that keeps drinks cold for 24 hours.
```

**Platform**

```
Instagram
```

**Tone**

```
Friendly
```

---

## 📌 Example Output

```
💧 Stay hydrated in style!

Meet the all-new EcoBottle X — the smart self-cleaning bottle that keeps your drinks cold for up to 24 hours.

Perfect for work, travel, and fitness.

✨ Smarter hydration starts today!

#EcoBottle #Hydration #SmartBottle
```

---

## 🔒 Security

* API keys are stored securely using a `.env` file.
* Never upload your `.env` file to GitHub.
* Use `.gitignore` to exclude sensitive files.

---

## 📄 License

This project is developed for educational and internship purposes.

---

## 👨‍💻 Author

**Shozab Raza**

Internship Project – DecodeLabs

Generative AI Project 2
