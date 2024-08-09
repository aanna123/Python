import pdfplumber
import re
def extractpdf(pdf_path):
    text=""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text+=page.extract_text()
    return text
extractedtext=extractpdf(r"C:\practice\progress\john.pdf")

def details(extractedtext):
    emailpattern=r'([\w\.-]+@[\w\.-]+)'
    phonepattern=r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    linkedinpattern=r'(\bhttps.*)'

    email=re.findall(emailpattern,extractedtext)
    phone=re.findall(phonepattern,extractedtext)
    linkedin=re.findall(linkedinpattern,extractedtext)
    
    return {
        "email of the applicant":email,
        "phone":phone,
        "linkedin":linkedin
    }

output=details(extractedtext)

print(output,end="\n") 



