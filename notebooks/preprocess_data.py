import json
import pandas as pd
import re

def tokenize_amharic(text):
    # Basic tokenizer using regex
    return re.findall(r'\w+|[^\w\s]', text, re.UNICODE)

def clean_text(text):
    text = text.replace('\n', ' ').replace('\r', '')
    text = re.sub(r'[^\u1200-\u137F0-9ብርa-zA-Z@፣፡።,.!?]', '', text)
    return text.strip()

with open("raw_telegram_data.json", "r", encoding="utf-8") as f:
    messages = json.load(f)

cleaned_data = []

for msg in messages:
    text = msg.get("text", "")
    if text:
        cleaned = clean_text(text)
        tokens = tokenize_amharic(cleaned)
        cleaned_data.append({
            "channel": msg["channel"],
            "date": msg["date"],
            "tokens": tokens,
            "original": text,
            "views": msg["views"]
        })

df = pd.DataFrame(cleaned_data)
df.to_csv("preprocessed_data.csv", index=False, encoding="utf-8-sig")
