# Natural Language Processing Notes

This repository contains my hands-on NLP learning notes using Python and NLTK.
It includes notebooks, short scripts, and concept lists covering core NLP topics.

## Repository Structure

- `tokenization/` — notebook and starter scripts for tokenization
- `preprocessing/` — text-cleaning and normalization notes
- `stemming/` — basic stemming example with `PorterStemmer`
- `lemmatization/` — notebook on lemmatization with `WordNetLemmatizer`
- `vectorization/` — placeholders for Bag of Words, TF-IDF, and similarity notes
- `classification/` — placeholders for text classification and Naive Bayes
- `probabilistic_models/` — concept checklist (`concepts-needed.txt`)
- `attention_models/` — Transformer/attention concept checklist (`core-concepts.txt`)

## Topics Covered

- Text preprocessing (lowercasing, punctuation cleanup, whitespace cleanup)
- Word tokenization
- Stopword removal
- Stemming
- Lemmatization
- Handling numbers, URLs, and special characters
- Probabilistic NLP concepts:
  - Naive Bayes
  - N-gram language model
  - Perplexity
  - Hidden Markov Model (HMM)
  - Maximum Likelihood Estimation (MLE)
- Attention and Transformer concepts:
  - Query, Key, Value
  - Self-attention and cross-attention
  - Scaled dot-product attention and multi-head attention
  - Positional encoding
  - Encoder/decoder architecture
  - Residual connections, layer normalization, and feed-forward blocks
  - Causal masking, padding mask, teacher forcing, and beam search

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Current requirements:

- `nltk`
- `ipykernel`

## Notes

Most folders are learning notes and work-in-progress files.
Some `.py` files are placeholders for future expansions.