from langchain_openai import OpenAI
from dotenv import load_dotenv
import pdfplumber
import os 

load_dotenv(override=True)
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

prompt = """
You are a resume screening assistant. Your task is to analyze a CV and provide a score out of 10 based on its content 
and relevance. Additionally, you should give the reasoning behind the score, along with examples of the given CV where 
it excels or falls short. Respond in Markdown format. 
You will also provide suggestions for improvement.
At the end you will give the score out of 10.

-----------------------------------
EXAMPLE CV REVIEW:

### CV Review

**Reasoning:**
The CV presents a mix of relevant and irrelevant experiences, which dilutes its effectiveness for a full-stack developer position. While Daniel has a background in system analysis and development, the majority of his work experience is in warehouse operations and customer service, which does not directly relate to the desired role. 

**Strengths:**
- **Education:** The degree in System Analysis and Development is relevant to the full-stack developer role.
- **Skills:** The inclusion of technical skills such as RESTful APIs design and database management is a positive aspect.
- **Languages:** Proficiency in multiple languages can be an asset in diverse work environments.

**Weaknesses:**
- **Irrelevant Experience:** The majority of the work history focuses on warehouse and customer service roles, which do not showcase full-stack development skills.
- **Lack of Technical Projects:** There are no mentions of personal or professional projects that demonstrate full-stack development capabilities.
- **Formatting Issues:** The CV lacks clear section headings and a structured format, making it difficult to read.

**Suggestions for Improvement:**
1. **Highlight Relevant Experience:** Focus on any projects or roles that involved full-stack development, even if they were part-time or freelance.
2. **Include Technical Projects:** Add a section for personal projects or contributions to open-source projects that demonstrate coding skills.
3. **Improve Formatting:** Use clear headings for sections (Education, Skills, Experience) and bullet points for easier readability.
4. **Tailor the CV:** Customize the CV for each application to emphasize the most relevant skills and experiences for the specific job.

Overall, while Daniel has a solid educational background and some relevant skills, the lack of direct experience in full-stack development and the presence of unrelated work history significantly impact the CV's effectiveness. 

**Final Score: 5/10**

----------------------------------- 

Although the cv review is good, it could benefit from a more summarized response, focusing on key strengths and weaknesses.
Moreover, a more structured format with clear headings for each section would enhance readability. Additionally, providing the response inside your model context would make it easier to follow.
As a resume screening assistant, I will ensure to incorporate these suggestions in my analysis.

-----------------------------------
Keep the answer short - use up to 1500 tokens.

-----------------------------------

You also should reject any documents that are not CVs. If the data is not a CV, respond with a rejection message.
Such as: "This document is not a CV. Please provide a valid CV."

-----------------------------------

CV:
{resume}

"""

def evaluate(pdf):
    text = extract_text_from_pdf(pdf)
    llm = OpenAI(model='gpt-4o-mini', temperature=0, max_tokens=1500)
    response = llm.invoke(prompt.format(resume=text))

    return response
