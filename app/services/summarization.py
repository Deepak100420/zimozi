from fastapi import FastAPI
import torch
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, GenerationConfig
from dotenv import load_dotenv
import os

load_dotenv()


model_path=os.getenv("MODEL_PATH")


# Define summary generation function
def generate_summary(text: str) -> str:
    """Generate a summary for the given input text."""
    
    
    # Load tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_path)

    # Fix forced_bos_token_id issue correctly
    generation_config = GenerationConfig.from_pretrained(model_path)
    generation_config.forced_bos_token_id = 0
    generation_config.save_pretrained(model_path)  # Save the fixed config

    # Attach the updated config to the model
    model.generation_config = generation_config
    
    inputs = tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)

    summary_ids = model.generate(
        inputs["input_ids"], 
        generation_config=generation_config,  # ✅ Use fixed config
        max_length=500, 
        min_length=30, 
        num_beams=4
    )
    summary=tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    

    return summary


''''
# FastAPI endpoint
@app.post("/summarize/")
async def summarize(input_data: TextInput):
    summary = generate_summary(input_data.text)
    return {"summary": summary}

# Run this using: uvicorn filename:app --reload'''
