import fitz

"""دریافت فایل از جویای کار"""

def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
        return text

 # تست دریافت با موفقیت

if __name__ == "__main__":
    pdf_path = "./Jobinja-SC-8971516.pdf"  # آدرس فایل رزومه
    resume_text = extract_text_from_pdf(pdf_path)
    print(resume_text)
