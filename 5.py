import logging
import sys
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Suppress warnings
logging.disable(logging.WARNING)

# Check for GPU
if not torch.cuda.is_available():
    print("❌ Error: GPU not available.")
    sys.exit(1)

print("✅ GPU is available. Proceeding with model loading...")
device = torch.device("cuda")

# Load model and tokenizer
model_path = "./qwen_model"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path).to(device)

# Get user input
prompt = input("\nEnter your question: ")

# Tokenize and generate
inputs = tokenizer(prompt, return_tensors="pt").to(device)
outputs = model.generate(
    **inputs,
    max_new_tokens=300,
    temperature=0.7,
    do_sample=True
)

# Decode and print response
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print("\nResponse:\n")
print(response)
