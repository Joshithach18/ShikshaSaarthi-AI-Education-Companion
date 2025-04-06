# ai_module.py
from transformers import pipeline

# Simple text generation using a Hugging Face model (stub)
def generate_content(topic: str, level: str = "basic") -> str:
    # For demo: generate generic text based on topic
    generator = pipeline("text-generation", model="gpt2")
    prompt = f"Explain {topic} for a {level} school student."
    result = generator(prompt, max_length=100, num_return_sequences=1)
    return result[0]["generated_text"]

# Translate using Hugging Face models (or stub for now)
def translate_text(content: str, target_lang: str = "hi") -> str:
    # Stub: You can later replace with an actual translation pipeline
    return f"[Translated to {target_lang}]: {content}"
