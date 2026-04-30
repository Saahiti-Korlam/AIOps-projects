import google.generativeai as genai
import os

# Set your API key here
os.environ["GOOGLE_API_KEY"] = "XXXXXXXXX"

# Configure the Gemini model
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-3-flash-preview')

PROMPT = """
Generate an ideal Dockerfile for {language} with best practices. Just share the dockerfile without any explanation between two lines to make copying dockerfile easy.
Include:
- Base image
- Installing dependencies
- Setting working directory
- Adding source code
- Running the application
- Expose on the required port
"""

def generate_dockerfile_gemini(language):
    response = model.generate_content(PROMPT.format(language=language))
    return response.text

if __name__ == '__main__':
    language = input("Enter the programming language: ")
    dockerfile = generate_dockerfile_gemini(language)
    print("\nGenerated Dockerfile:\n")
    print(dockerfile)
