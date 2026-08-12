from src.schema import resume_schema


def get_resume_analysis_prompt(resume_text, job_role):

    return f"""
You are an expert recruiter and career coach.

Analyze the resume for the role:

{job_role}

Resume:

{resume_text}

Instructions:

- Score the resume out of 100.
- Identify strengths.
- Identify weaknesses.
- Identify missing skills.
- Give actionable recommendations.

{resume_schema}

Do not return markdown.

Do not use ```json.

Return only raw JSON.
"""