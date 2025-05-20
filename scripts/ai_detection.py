from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained("roberta-base-openai-detector")
model = AutoModelForSequenceClassification.from_pretrained("roberta-base-openai-detector")

def detect_ai_generated_text(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
    outputs = model(**inputs)
    prediction = torch.softmax(outputs.logits, dim=1)
    ai_score = prediction[0][1].item()
    return "Yes" if ai_score > 0.5 else "No"
