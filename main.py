
import spacy
from nltk import download
from resume_analyzer import extract_text_from_pdf


"""دانلود خودکار مدل spaCy در صورت عدم یافت شدن"""
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")


# لیست مهارت های مورد نیاز نیرو

SKILLS = [
    "python", "java", "javascript", "django", "flask", "machine learning",
    "deep learning", "react", "sql", "mongodb", "docker", "git", "linux"
]

def extract_skills_from_text(text, skills_list):
    text = text.lower()
    doc = nlp(text)
    extracted = set()
    for token in doc:
        if token.text in skills_list:
            extracted.add(token.text)
    return list(extracted)


# test 1

if __name__ == "__main__":
    text = extract_text_from_pdf("./Jobinja-SC-8971516.pdf")
    skills = extract_skills_from_text(text, SKILLS)
    print("✅ مهارت‌های شناسایی‌شده:")
    for skill in skills:
        print(".", skill)
