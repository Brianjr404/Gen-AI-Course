import from byllm {Model}

glob llm = Model(model_name="gemini/gemini-2.0-flash");

enum Personality {
    INTROVERT,
    EXTROVERT,
    AMBIVERT,
    CREATIVE  # Added for fun—try it!
}

def get_personality(name: str) -> Personality by llm();