# 📚 AI-Powered Study Buddy

> **IBM SkillsBuild Internship Project**

## 📖 Overview

**AI-Powered Study Buddy** is an AI-based learning assistant developed to help students study more efficiently. It enables users to upload PDF study notes and leverage Natural Language Processing (NLP) and Transformer-based AI models to summarize content, answer questions, generate quizzes, and create flashcards.

The project is designed with a simple and interactive **Streamlit** interface, making AI-assisted learning accessible without requiring technical expertise.

---

## 🎯 Problem Statement

Students often face challenges while studying:

* Reading lengthy notes is time-consuming.
* Understanding complex concepts can be difficult.
* Teachers may not always be available for doubt clarification.
* Creating revision materials manually takes significant effort.

This project addresses these challenges by providing an intelligent AI assistant capable of generating summaries, answering questions, and creating revision content automatically.

---

## 🚀 Features

### 📂 Upload Study Notes

* Upload PDF files
* Extract text automatically
* Preview extracted content

---

### 📄 AI Notes Summarizer

Generate three different types of summaries:

* Short Summary
* Detailed Summary
* Key Points Extraction

---

### 💬 AI Study Assistant

Ask questions directly from uploaded notes.

Examples:

* What is Machine Learning?
* Explain supervised learning.
* What are the advantages?

The assistant answers using the uploaded study material.

---

### ❓ AI Quiz Generator

Automatically generates Multiple Choice Questions (MCQs) from uploaded notes.

Features:

* Easy
* Medium
* Hard difficulty
* Adjustable number of questions

Each quiz contains:

* Question
* Four options
* Correct answer
* Explanation

---

### 📝 AI Flashcard Generator

Generate AI-powered flashcards from uploaded study notes.

Each flashcard contains:

* Question
* Answer

Ideal for quick revision before exams.

---

## 🛠 Technologies Used

| Category           | Technologies                  |
| ------------------ | ----------------------------- |
| Language           | Python                        |
| Framework          | Streamlit                     |
| NLP                | spaCy, NLTK                   |
| Transformer Models | Google FLAN-T5, Facebook BART |
| PDF Processing     | PyPDF2, pdfplumber            |
| Data Processing    | NumPy, Pandas                 |
| Machine Learning   | Scikit-learn                  |
| Visualization      | Plotly                        |

---

## 🤖 AI Models Used

### Facebook BART Large CNN

Used for:

* Text Summarization
* Detailed Summaries
* Key Point Extraction

---

### Google FLAN-T5 Base

Used for:

* Question Answering
* Quiz Generation
* Flashcard Generation

---

## 📂 Project Structure

```text
AI_Study_Buddy/
│
├── app.py
│
├── modules/
│   ├── pdf_reader.py
│   ├── summarizer.py
│   ├── study_assistant.py
│   ├── quiz_generator.py
│   ├── flashcard_generator.py
│   └── text_preprocessing.py
│
├── assets/
│
├── data/
│
├── requirements.txt
│
└── README.md
```

---

## ⚙ Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/AI_Study_Buddy.git
```

---

### Move into project folder

```bash
cd AI_Study_Buddy
```

---

### Install dependencies

```bash
pip install -r requirements.txt
```

---

### Download spaCy language model

```bash
python -m spacy download en_core_web_sm
```

---

### Run the application

```bash
streamlit run app.py
```

---

## 📌 Workflow

```text
Upload PDF
      │
      ▼
Extract Text
      │
      ▼
AI Processing
      │
      ├────────► Summarizer
      │
      ├────────► Study Assistant
      │
      ├────────► Quiz Generator
      │
      └────────► Flashcard Generator
```

---

## 📊 Future Enhancements

* Voice-to-Notes Conversion
* OCR Support for Scanned PDFs
* Multi-language Support
* AI Mind Map Generator
* Progress Tracking Dashboard
* Export Summaries and Flashcards as PDF
* Personalized Learning Recommendations

---

## 🎓 Learning Outcomes

Through this project, the following concepts were implemented:

* Natural Language Processing (NLP)
* Transformer-based Generative AI
* Text Summarization
* Question Answering
* Quiz Generation
* Flashcard Generation
* PDF Text Extraction
* Streamlit Application Development

---

## 👩‍💻 Author

**Rishita Pola**

IBM SkillsBuild Internship Project

---

## 📜 License

This project is developed for educational purposes as part of the **IBM SkillsBuild Internship Program**.
