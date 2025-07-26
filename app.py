from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
import fitz  # PyMuPDF
import google.generativeai as genai

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)

# Configure Gemini API securely
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_pdf():
    file = request.files['pdf']
    pdf_path = os.path.join("uploads", file.filename)
    file.save(pdf_path)

    # Read and extract text
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()

    # Generate summary
    prompt = f"Summarize the following academic paper:\n{text[:800]}"
    response = model.generate_content(prompt)
    summary = response.text

    return jsonify({"summary": summary, "context": text[:1200]})

@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.get_json()
    question = data.get("question")
    context = data.get("context")

    prompt = f"Based on the following academic paper content:\n{context[:800]}\n\nAnswer this question: {question}"
    response = model.generate_content(prompt)

    return jsonify({"answer": response.text})

if __name__ == "__main__":
    os.makedirs("uploads", exist_ok=True)
    app.run(debug=True)
