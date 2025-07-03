# test_env.py
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
print(torch.__version__)  # E.g., 2.6.0
print("Environment setup complete!")