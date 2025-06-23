Here is a **paraphrased and polished version** of your project summary and setup instructions, formatted in professional **README.md** style for GitHub:

---

#  EthioMart: Amharic Named Entity Recognition for Telegram E-Commerce

## Project Overview

**EthioMart** is an AI-driven solution designed to centralize and streamline Telegram-based e-commerce in Ethiopia. The project focuses on **extracting structured business information**—such as products, prices, and locations—from **Amharic-language messages** in Telegram channels using Named Entity Recognition (NER).

This repository features a complete pipeline: from **data collection** and **Amharic NER model training**, to **vendor scoring and analytics**. The end goal is to support micro-lending and small business profiling through intelligent data extraction.

---

## Key Features

* ** Telegram Scraper**: Automated pipeline to collect and clean e-commerce data in Amharic from Telegram channels.
* ** Multilingual NER Models**: Fine-tuned transformer models including **XLM-RoBERTa**, **mBERT**, and **DistilBERT**, optimized for identifying key entities in Amharic.
* ** Vendor Scoring System**: A lightweight analytics engine to assess vendor activity, reliability, and scale—potentially aiding micro-finance institutions.
* ** Explainable AI**: Model interpretability powered by **SHAP** and **LIME** to provide insights into how predictions are made.


---

## ⚙️ Installation & Setup

### ✅ Prerequisites

* Python 3.8+
* PowerShell (for Windows)
* NVIDIA GPU (optional but recommended for training)

### 📦 Steps

1. **Clone the repository**

   ```bash
   git clone https://github.com/Lifeconr/EthioMart_week_4.git
   cd EthioMart_week_4
   ```

2. **Create and activate a virtual environment**

   ```powershell
   python -m venv EthioMart_week_4-venv
   .\EthioMart_week_4-venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Telegram API credentials**

   Create a `.env` file in the root directory and add your API keys:

   ```env
   TELEGRAM_API_ID=your_api_id
   TELEGRAM_API_HASH=your_api_hash
   ```
