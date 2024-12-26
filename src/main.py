# main.py
from ai_factory import get_ai_model

def main():
    ai_model = get_ai_model()
    
    prompt = "Tell me a joke."
    response = ai_model.generate_response(prompt)
    print(response)

if __name__ == "__main__":
    main()
