import torch
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM

# Initialize model and tokenizer
model_path = "./qwen_model"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path).to("cuda" if torch.cuda.is_available() else "cpu")

# Check for GPU
if not torch.cuda.is_available():
    raise SystemExit("❌ GPU not available. Exiting.")

device = torch.device("cuda")
model.to(device)

# FastAPI setup
app = FastAPI(title="Qwen2.5-0.5B-Instruct API", version="1.0")

class QuestionRequest(BaseModel):
    prompt: str

@app.post("/ask")
async def ask_model(request: QuestionRequest):
    try:
        inputs = tokenizer(request.prompt, return_tensors="pt").to(device)
        outputs = model.generate(
            **inputs,
            max_new_tokens=300,
            temperature=0.7,
            do_sample=True
        )
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
