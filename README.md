# Amharic E-commerce Data Extractor

This project scrapes e-commerce messages from Ethiopian Telegram channels, preprocesses the Amharic text, and prepares data for Named Entity Recognition (NER) fine-tuning.

## 📦 Project Structure

- `scrape_telegram.py` - Scrapes messages from selected Telegram channels.
- `preprocess_data.py` - Cleans and tokenizes raw messages.
- `label_data_to_conll.py` - Interactive CLI tool for labeling tokens in CoNLL format.
- `raw_telegram_data.json` - Raw scraped data.
- `preprocessed_data.csv` - Cleaned and tokenized data.
- `labeled_data.conll` - Manually labeled dataset for NER.

## 🧪 Task Objectives

### ✅ Task 1: Data Ingestion & Preprocessing
- Collect messages from 20+ Ethiopian Telegram channels.
- Preprocess text by normalizing, tokenizing, and cleaning.
- Save structured message data with metadata.

### ✅ Task 2: Label Data in CoNLL Format
- Load preprocessed messages.
- Manually annotate 30–50 messages with `B-Product`, `B-PRICE`, `B-LOC`, etc.
- Save in standard CoNLL format for model fine-tuning.

### ✅ Task 3: Exploratory Data Analysis (EDA)
Identified high-frequency terms and patterns in e-commerce messages.

Noted consistent formats for prices (e.g., 1000 ብር), products, and locations.

Insights used to guide labeling logic and entity class definitions.

### ✅ Task 4: Manual Annotation
Interactive labeling interface using Python CLI.

30 messages labeled using BIO tagging scheme.

Supported entities: B-Product, I-Product, B-PRICE, I-PRICE, B-LOC, I-LOC, and O.

### ✅ Task 5: CoNLL Format Output
Each token is aligned with its label.

Sentences are separated by a blank line.

Format is compatible with common NLP training pipelines.

### ✅ Task 6: Preparation for Training
Project organized to support:

Data loading for transformers and CRF models

Further annotation

Integration with spaCy NER training pipelines

Label consistency ensured for reproducible training

## 📋 How to Run

### 1. Clone the repository and install requirements
```bash
git clone https://github.com/Samrwitt/Amharic-E-commerce-Data-Extractor.git
cd amharic-ner-telegram
pip install -r requirements.txt
````

---
