# 📚 SmartStudyAI

An AI-powered web application that helps students improve their learning experience by generating questions, summarizing text, answering questions, creating study plans, and analyzing PDF documents.

---

## 🚀 Features

* ❓ **Question Generator**
  Generate practice questions from any paragraph using NLP models.

* 📝 **Text Summarizer**
  Convert long text into short, easy-to-read summaries.

* 🤖 **Question Answering System**
  Ask questions based on a given context and get accurate answers.

* 📅 **Study Plan Generator**
  Create a structured study plan based on syllabus, topics, and timeline.

* 📄 **PDF Analyzer**
  Upload PDF files and:

  * Extract text
  * Summarize content
  * Generate questions
  * Ask questions based on PDF

---

## 🛠️ Tech Stack

### 💻 Backend

* Python
* Flask

### 🤖 AI / NLP Models (Hugging Face Transformers)

* **Question Generation** → `valhalla/t5-base-qg-hl`
* **Summarization** → `facebook/bart-large-cnn`
* **Question Answering** → `distilbert-base-uncased-distilled-squad`

### 🌐 Frontend

* HTML
* CSS
* Jinja Templates

### 📦 Libraries

* `transformers`
* `torch`
* `pypdf`
* `textwrap`

---

## 🧠 How It Works

1. User inputs text or uploads a PDF
2. Backend processes the input using Flask
3. NLP models generate:

   * Questions
   * Summary
   * Answers
4. Results are displayed dynamically on the UI

---

## 📂 Project Structure

```
AI-Study-Assistant/
│
├── app.py
├── config.py
├── requirements.txt
│
├── templates/
│   ├── index.html
│   ├── question_generator.html
│   ├── summarizer.html
│   ├── qa.html
│   ├── study_plan.html
│   ├── upload_pdf.html
│   └── ...
│
└── static/
```

---

## ⚙️ Installation & Setup

1. Clone the repository:

```bash
git clone https://github.com/prachiraut711/AI-Study-Assistant.git
cd AI-Study-Assistant
```

2. Create virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the app:

```bash
python app.py
```

5. Open in browser:

```
http://127.0.0.1:5000
```

---

## 🎯 Use Cases

* Students preparing for exams
* Quick revision of notes
* Understanding long documents
* Generating practice questions

---

## ⚠️ Limitations

* Uses pre-trained models (no custom training)
* Large models may take time to load initially
* Study plan generator uses basic logic

---

## 👩‍💻 Author

**Prachi Raut**
GitHub: https://github.com/prachiraut711

---

## ⭐ Acknowledgements

* Hugging Face Transformers
* Open-source NLP models
* Flask framework

---
