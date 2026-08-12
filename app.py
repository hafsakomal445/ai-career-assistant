from flask import Flask, render_template, request, send_file
import os

from src.pdf_reader import extract_text_from_pdf
from src.prompt import get_resume_analysis_prompt
from src.analyzer import analyze_resume

from src.interview_prompt import get_interview_prompt
from src.interview_generator import generate_questions

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Store latest generated report
latest_report = ""


@app.route("/", methods=["GET", "POST"])
def home():

    global latest_report

    if request.method == "POST":

        resume = request.files["resume"]
        job_role = request.form["job_role"]

        filepath = os.path.join(
            app.config["UPLOAD_FOLDER"],
            resume.filename
        )

        resume.save(filepath)

        # Extract text from PDF
        resume_text = extract_text_from_pdf(filepath)

        # Resume Analysis
        analysis_prompt = get_resume_analysis_prompt(
            resume_text,
            job_role
        )

        analysis = analyze_resume(
            analysis_prompt
        )

        # Interview Questions
        interview_prompt = get_interview_prompt(
            resume_text,
            job_role
        )

        questions = generate_questions(
            interview_prompt
        )

        # Create downloadable report
        latest_report = f"""
AI CAREER ASSISTANT REPORT

Target Role:
{job_role}

Overall Score:
{analysis['overall_score']}/100


STRENGTHS
--------------------------------
{chr(10).join(analysis['strengths'])}


WEAKNESSES
--------------------------------
{chr(10).join(analysis['weaknesses'])}


MISSING SKILLS
--------------------------------
{chr(10).join(analysis['missing_skills'])}


RECOMMENDATIONS
--------------------------------
{chr(10).join(analysis['recommendations'])}


TECHNICAL INTERVIEW QUESTIONS
--------------------------------
{chr(10).join(questions['technical_questions'])}


BEHAVIORAL INTERVIEW QUESTIONS
--------------------------------
{chr(10).join(questions['behavioral_questions'])}
"""

        return render_template(
            "result.html",
            analysis=analysis,
            questions=questions,
            job_role=job_role,
            filename=resume.filename
        )

    return render_template("index.html")


@app.route("/download-report")
def download_report():

    with open(
        "career_report.txt",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(latest_report)

    return send_file(
        "career_report.txt",
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)