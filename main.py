from fastapi import FastAPI
from ai_module import generate_content, translate_text

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to ShikshaSaarthi – AI Teaching Companion"}

@app.get("/generate/")
def get_generated_content(topic: str, level: str = "basic"):
    content = generate_content(topic, level)
    return {"topic": topic, "generated_content": content}

@app.get("/translate/")
def translate(content: str, target_lang: str = "hi"):
    translated = translate_text(content, target_lang)
    return {"translated_content": translated}
