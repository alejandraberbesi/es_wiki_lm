# 🧠 Spanish Wikipedia Language Model (2020)

This project demonstrates the construction and training of a Spanish language model using FastAI v2 on a custom Wikipedia dataset. It was created in **2020**, using the tooling, libraries, and best practices available at that time.

> ⚠️ **Note:** This work was built on early versions of FastAI v2 and PyTorch 1.6. Some parts may be outdated by today's standards.

---

## 📚 Overview

The goal was to build a **language model** trained on Spanish Wikipedia-style articles to capture the structure and vocabulary of Spanish text. It includes:

- Drive integration with Google Colab
- Text preprocessing (cleaning, renaming, tokenization, numericalization)
- FastAI v2 `LMDataLoader` pipeline setup
- AWD-LSTM training using `language_model_learner`

---

## 🛠️ Tech Stack (2020 Versions)

- **Python** (via Google Colab)
- **FastAI v2** (`fastai2`)
- **PyTorch 1.6**
- **Google Drive** for data/model persistence
- **AWD_LSTM** architecture
