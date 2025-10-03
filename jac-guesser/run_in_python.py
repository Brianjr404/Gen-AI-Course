import jaclang  # Activates Jac import hook—must be first!
from personality import get_personality, Personality  # Imports from personality.jac

import os
from dotenv import load_dotenv

load_dotenv()

def main():
    if not os.getenv('GEMINI_API_KEY'):
        os.environ['GEMINI_API_KEY'] = input("Enter your Gemini API key: ")
    
    while True:
        name = input("Enter a name (or 'q' to quit): ")
        if name.lower() == 'q':
            break
        try:
            result = get_personality(name)
            print(f"{name} is guessed as: {result}")
        except Exception as e:
            print(f"Error guessing personality: {e}")

if __name__ == "__main__":
    main()