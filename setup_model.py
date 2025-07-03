from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

print("Starting model setup...")
try:
    print("Downloading DeepSeek-Coder-1.3B tokenizer...")
    model_name = "deepseek-ai/deepseek-coder-1.3b"
    tokenizer = AutoTokenizer.from_pretrained("deepseek-ai/deepseek-coder-1.3b-instruct", trust_remote_code=True)
    # tokenizer = AutoTokenizer.from_pretrained(model_name)
    print("Tokenizer downloaded.")

    print("Downloading DeepSeek-Coder-1.3B model...")
    model = AutoModelForCausalLM.from_pretrained(
        "deepseek-ai/deepseek-coder-1.3b-instruct",
        device_map="cpu",
        low_cpu_mem_usage=True,
        trust_remote_code=True,
        torch_dtype=torch.float32
    )
    print("Model downloaded.")

    print("Saving to ./deepseek_model...")
    tokenizer.save_pretrained("./deepseek_model")
    model.save_pretrained("./deepseek_model")
    print("Model and tokenizer saved successfully.")

except Exception as e:
    print(f"An error occurred: {e}")
    raise