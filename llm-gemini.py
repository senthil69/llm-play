import os
from dotenv import load_dotenv
import vertexai
from vertexai.generative_models import (GenerationConfig, GenerativeModel)
load_dotenv()

PROJECT_ID = os.getenv('PROJECT_ID')
LOCATION = os.getenv('LOCATION')
MODEL_NAME = "gemini-pro" # or "gemini-pro-vision" if applicable

# Initialize Vertex AI
vertexai.init(project=PROJECT_ID, location=LOCATION)

# Load the Generative Model
model = GenerativeModel(MODEL_NAME)
print(model)
GOOGLE_APPLICATION_CREDENTIALS = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
print(f"GOOGLE_APPLICATION_CREDENTIALS: {GOOGLE_APPLICATION_CREDENTIALS}")

def generate_response(prompt):
    """Generates text using the Gemini model."""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"
    
if __name__ == "__main__":
    prompt = "explain the concept of a four stroke engine as a professor to a first year engineering student"
    result = generate_response(prompt)
    print(result)

