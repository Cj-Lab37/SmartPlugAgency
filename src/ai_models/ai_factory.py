# ai_factory.py

""" 
Purpose: Contains the factory function to instantiate the appropriate AI model based on the configuration.

Description: This file reads the config.json file to determine which AI model to use and returns an instance of the selected model.

Interactions: Interacts with chatgpt_model.py and gemini_model.py to instantiate the respective AI models. Reads the config.json file for configuration.

"""


from chatgpt_model import ChatGPTModel
from gemini_model import GeminiModel
from grok_model import GrokModel

def get_ai_model(agent_name):
    if agent_name == "agent1":
        return ChatGPTModel(model_version="4o-mini")
    elif agent_name == "agent2":
        return GeminiModel(model_version="gemini-large")
    elif agent_name == "agent3":
        return GrokModel(model_version="grok-beta-small")
    else:
        raise ValueError(f"Unknown agent: {agent_name}")

# Example usage
agent1_model = get_ai_model("agent1")
agent2_model = get_ai_model("agent2")
agent3_model = get_ai_model("agent3")




