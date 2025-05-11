import logging
import sys
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Suppress warnings (optional)
logging.disable(logging.WARNING)

# Check for GPU
if not torch.cuda.is_available():
    print("❌ Error: GPU not available. This script requires a CUDA-enabled GPU to run.")
    sys.exit(1)

print("✅ GPU is available. Proceeding with model loading...")

# Set device
device = torch.device("cuda")

model_path = "./qwen_model"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path).to(device)

# Example prompt
prompt = "Explain quantum physics in simple terms."
inputs = tokenizer(prompt, return_tensors="pt").to(device)

# Generate response
outputs = model.generate(
    **inputs,
    max_new_tokens=300,
    temperature=0.7,
    do_sample=True
)

# Decode and print
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print("\nResponse:\n")
print(response)
