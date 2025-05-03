"""مقایسه رزومه با شغل و درصد شباهت """

from fuzzywuzzy import fuzz

def calculate_match_percentage(resume_skills, job_description):
    job_description = job_description.lower()
    match_score = 0
    for skill in resume_skills:
        if fuzz.partial_ratio(skill, job_description) >= 80:
            match_score += 1
    if len(resume_skills) == 0:
        return 0
    return round(match_score / len(resume_skills) * 100, 2)

# test
resume_skills = ['python', 'django', 'sql']
job_posting_1 = "We are looking for a backend developer with experience in Python, Django, and PostgreSQL."

user1 = calculate_match_percentage(resume_skills, job_posting_1)
print("درصد تطابق با آگهی شغلی:", user1, "%")