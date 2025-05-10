from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import logging
from datetime import datetime

# Initialize logging
logging.basicConfig(
    filename="api_requests.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

app = FastAPI()

# Load model
model_path = "./qwen_model"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path).to("cuda" if torch.cuda.is_available() else "cpu")

class PromptRequest(BaseModel):
    prompt: str

@app.post("/api/ask")
async def ask(prompt_data: PromptRequest, request: Request):
    # Log the incoming request
    client_ip = request.client.host
    logging.info(f"Request from {client_ip}: {prompt_data.prompt}")

    try:
        inputs = tokenizer(prompt_data.prompt, return_tensors="pt").to(model.device)
        outputs = model.generate(**inputs, max_new_tokens=300)
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)

        # Log the response (optional: you can truncate if it's long)
        logging.info(f"Response to {client_ip}: {response[:200]}...")

        return {"response": response}
    except Exception as e:
        logging.error(f"Error processing request from {client_ip}: {str(e)}")
        raise HTTPException(status_code=500, detail="An error occurred while generating the response.")

