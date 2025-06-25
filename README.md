---

# EthioMart Lite: Amharic NER for Telegram E-Commerce

📌 **Project Overview**

**EthioMart Lite** is a lightweight pipeline that transforms Telegram e-commerce messages in Amharic into structured data for Named Entity Recognition (NER). The solution includes:

* 🧲 Telegram message scraping
* 🧹 Amharic-English text preprocessing
* 🏷️ Manual token-level labeling in CoNLL format
* ⚙️ NER model training and interpretability
* 📈 Vendor analytics for business intelligence

---

## 🏆 Key Achievements

### ✅ Data Pipeline

* Scraped **1,000+ messages** from 5 Amharic Telegram vendors:

  * `ZemenExpress`, `nevacomputer`, `helloomarketethiopia`, `Fashiontera`, `kuruwear`
* Saved in `raw_telegram_data.json`

### ✅ Data Processing

* Text cleaned, tokenized, and exported to `preprocessed_data.csv`
* Nulls, emojis, and links removed
* Script: `preprocess_data.ipynb`

### ✅ Manual NER Labeling

* 30 messages (\~400+ tokens) labeled using BIO format
* Output in `labeled_data.conll`
* Script: `label_data_to_conll.ipynb`

### ✅ NER Modeling

* Transformer models fine-tuned for NER
* Performance benchmarked in `model_comparision.ipynb`
* Interpretability analysis in `model_interpretability.ipynb`

### ✅ Vendor Analytics

* Created vendor scoring logic based on:

  * Views per post
  * Posting frequency
  * Price profile
* Script: `vendor_scorecard.ipynb`

---

## 📂 Repository Structure

```plaintext
Amharic-E-commerce-Data-Extractor/
├── .github/workflows/                # GitHub Actions
├── notebooks/
│   ├── scrape_telegram.ipynb         # Task 1 - Scraping
│   ├── preprocess_data.ipynb         # Task 2 - Preprocessing
│   ├── label_data_to_conll.ipynb     # Task 3 - Manual labeling
│   ├── model_training.ipynb          # Task 4 - Fine-tuning models
│   ├── model_comparision.ipynb       # Task 5 - Benchmarking
│   ├── model_interpretability.ipynb  # Task 6 - SHAP/LIME insights
│   └── vendor_scorecard.ipynb        # Task 6 - Vendor profiling
│
├── requirements.txt                  # Python dependencies
├── README.md                         
└── .gitignore
```

---

## 🛠️ Installation Guide

### Prerequisites

* Python 3.8+
* Telegram API credentials from [my.telegram.org](https://my.telegram.org)

### Setup

```bash
# Clone the repository
git clone https://github.com/RuhamaY/Amharic-E-commerce-Data-Extractor.git
cd Amharic-E-commerce-Data-Extractor

# Install requirements
pip install -r requirements.txt
```

---

## 🚀 Usage

### 1. Scrape Messages

```bash
# Inside a Jupyter cell or CLI
!python notebooks/scrape_telegram.ipynb
```

### 2. Preprocess Text

```bash
!python notebooks/preprocess_data.ipynb
```

### 3. Label Tokens for NER

```bash
!python notebooks/label_data_to_conll.ipynb
```

### 4. Train & Evaluate Models

Open:

* `model_training.ipynb`
* `model_comparision.ipynb`

### 5. Analyze Results

* Run `model_interpretability.ipynb` for SHAP
* Run `vendor_scorecard.ipynb` for scoring vendors

---

## 🔍 NER Entity Tags

* `B-Product`, `I-Product`
* `B-PRICE`, `I-PRICE`
* `B-LOC`, `I-LOC`
* `O` – Outside any entity

---
