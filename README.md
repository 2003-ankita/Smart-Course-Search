# Smart Course Search - Analytics Vidhya
🚀 Project Overview
The Smart Course Search tool is designed to help users easily discover relevant free courses from Analytics Vidhya. It leverages Natural Language Processing (NLP) for semantic search and utilizes vector databases for efficient retrieval.

## 📌 Features
- Web Scraping: Extracts course data (titles, categories, URLs, ratings, and reviews).
- Vector Search: Uses ChromaDB for similarity-based search.
- NLP Embeddings: Implements all-MiniLM-L6-v2 for sentence embeddings.
- UI: Built with Streamlit for a smooth user experience.
- Efficient Storage: Saves course data in an Excel file with timestamp-based versioning.

## 🛠️ Set-up

## 1. Create Virtual Environment
   ```bash
   python -m venv env_name
   ```
## 2. Install Dependencies
Install the dependencies using:

```bash
pip install -r requirements.txt
```
## 3. Run Search Engine
Run the search engine script to process the scraped course data using:
```bash
python search_engine.py
```
## 4. Run the Streamlit App
```bash
streamlit run app.py
```
## 🚀 Deployment
The project is deployed on Hugging Face Spaces for public access: **[Smart Search Tool](https://huggingface.co/spaces/ankita0705/smart_search)**
