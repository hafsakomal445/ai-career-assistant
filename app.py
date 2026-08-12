from flask import Flask, render_template, request
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


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        # Get uploaded resume
        resume = request.files["resume"]

        # Get target job role
        job_role = request.form["job_role"]

        # Save resume
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

        # Render Results
        return render_template(
            "result.html",
            analysis=analysis,
            questions=questions,
            job_role=job_role,
            filename=resume.filename
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)