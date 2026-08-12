# AI Career Assistant

An AI-powered career coaching application built with Flask and Gemini API.

The app analyzes a user's resume against a target job role, identifies strengths and weaknesses, recommends improvements, and generates personalized interview questions.

---

## Features

- Upload Resume (PDF)
- Resume Text Extraction
- AI Resume Analysis
- Resume Scoring
- Missing Skills Detection
- Personalized Recommendations
- Technical Interview Questions
- Behavioral Interview Questions
- Downloadable Career Report
- Structured JSON Output

---

## Tech Stack

### Backend
- Python
- Flask

### AI
- Google Gemini API
- Prompt Engineering
- Structured Outputs (JSON)

### Document Processing
- PyPDF

### Frontend
- HTML
- Bootstrap 5

---

## Project Workflow

Resume PDF
↓
Text Extraction
↓
Gemini Analysis
↓
Structured JSON Output
↓
Resume Score
↓
Interview Questions
↓
Download Report

---

## Installation

Clone the repository:

```bash
git clone https://github.com/hafsakomal445/ai-career-assistant.git
cd ai-career-assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create .env:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Run:

```bash
python app.py
```

---

## Example Output

### Resume Analysis

- Overall Score: 84/100
- Strengths
- Weaknesses
- Missing Skills
- Recommendations

### Interview Questions

Technical Questions:
- Explain overfitting.
- What is cross-validation?

Behavioral Questions:
- Tell me about a challenging project.
- How do you handle deadlines?

---

## Future Improvements

- ATS Compatibility Score
- Resume Keyword Optimization
- PDF Report Export
- Multi-Role Comparison
- Resume Rewriting Suggestions

---

## Author

Hafsa Komal

GitHub:
https://github.com/hafsakomal445