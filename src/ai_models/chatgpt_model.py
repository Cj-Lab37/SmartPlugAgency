# chatgpt_model.py

"""
Purpose: Implements the AIModel interface for the ChatGPT model.

Description: This file contains the ChatGPTModel class, which provides methods to interact with the ChatGPT API.

Interactions: Inherits from AIModel and interacts with the ChatGPT API.

"""

import os
from dotenv import load_dotenv
from ai_model import AIModel
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

class ChatGPTModel(AIModel):
    def __init__(self, model_version):
        api_key = os.getenv("CHATGPT_API_KEY")
        self.client = OpenAI(api_key=api_key, base_url="https://api.openai.com/v1")
        self.model_version = model_version

    def generate_response(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model_version,
            messages=[
                {"role": "system", "content": "You are ChatGPT."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message

    def analyze_text(self, text: str) -> dict:
        # Implement text analysis using ChatGPT
        pass
