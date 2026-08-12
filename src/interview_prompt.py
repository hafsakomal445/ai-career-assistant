def get_interview_prompt(resume_text, job_role):

    return f"""
You are a senior technical interviewer.

Based on the following resume and target role:

Role:
{job_role}

Resume:
{resume_text}

Generate:

- 5 Technical Interview Questions
- 5 Behavioral Interview Questions

Return ONLY valid JSON.

{{
    "technical_questions": [
        "question"
    ],
    "behavioral_questions": [
        "question"
    ]
}}
"""