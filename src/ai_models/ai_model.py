"""
AIModel Abstract Base Class
This file contains the AIModel abstract base class with methods that all AI models must implement.
Methods:
    generate_response: Abstract method to generate a response based on input data.
    analyze_text: Abstract method to analyze text and provide insights.
Interactions:
    Other AI model implementations will inherit from this class.
"""



# ai_model.py
from abc import ABC, abstractmethod

class AIModel(ABC):
    @abstractmethod
    def generate_response(self, prompt: str) -> str:
        pass

    @abstractmethod
    def analyze_text(self, text: str) -> dict:
        pass
