from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments, TextDataset, DataCollatorForLanguageModeling

model_name = "./deepseek_model"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def load_dataset(file_path, tokenizer):
    dataset = TextDataset(
        tokenizer=tokenizer,
        file_path=file_path,
        block_size=128
    )
    return dataset

data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)
train_dataset = load_dataset("data.json", tokenizer)

training_args = TrainingArguments(
    output_dir="./finetuned_deepseek",
    overwrite_output_dir=True,
    num_train_epochs=3,
    per_device_train_batch_size=2,
    save_steps=500,
    save_total_limit=2
)

trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=train_dataset
)

trainer.train()
model.save_pretrained("./finetuned_deepseek")
tokenizer.save_pretrained("./finetuned_deepseek")