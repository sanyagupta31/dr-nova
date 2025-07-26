
🧠 Dr. Nova – AI Research Assistant

Dr. Nova is an AI-powered research assistant that:

* Reads academic PDF papers
* Summarizes content using Gemini API
* Answers questions based on the uploaded paper

Built with Flask and PyMuPDF, it offers a simple web interface for researchers and students.

---

## 📁 Project Structure

```
DrNova/
│
├── app.py                  # Main Flask app
├── .env                    # API key stored here (not tracked by git)
├── .gitignore              # Ignores env, uploads, cache, etc.
├── /uploads/               # Uploaded PDFs (auto-created)
├── /templates/
│   └── index.html          # Frontend UI
└── README.md
```

---

## 🔧 Setup Instructions

### 1. 📦 Install Requirements

```bash
pip install flask python-dotenv google-generativeai PyMuPDF
```

---

### 2. 🗝️ Add Your Gemini API Key

Create a `.env` file in the root:

```
GEMINI_API_KEY=your_actual_gemini_api_key
```

---

### 3. 🚀 Run the App

```bash
python app.py
```

Visit [http://localhost:5000](http://localhost:5000) in your browser.

---

## 💡 Features

* 📄 Upload any academic/research PDF
* 🧠 Summarize using Gemini 1.5 Flash
* ❓ Ask questions based on PDF context
* 🔒 Uses `.env` for secure API handling

---

## 📷 Screenshot

> *Optional: Insert a screenshot of the web UI here if you have one.*

---

## 🛠️ Built With

* [Flask](https://flask.palletsprojects.com/)
* [Gemini API (Google Generative AI)](https://ai.google.dev/)
* [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/)
* HTML/CSS (custom landing page design)

---

## 🧑‍💻 Author

**Sanya Gupta**
*AI Developer building GenAI apps like Dr. Nova and Ms. Friday*

