import pandas as pd
from sentence_transformers import SentenceTransformer
import chromadb

# Load data from Excel file
df = pd.read_excel("AnalyticsVidhya_Free_Courses.xlsx")

# Extract relevant columns
course_titles = df["Course Title"].astype(str).tolist()
categories = df["Categories"].astype(str).tolist()
course_urls = df["Course URL"].astype(str).tolist()

# Initialize Sentence-Transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Initialize ChromaDB
client = chromadb.PersistentClient(path="chromadb_store")
collection = client.get_or_create_collection(name="courses")

# Generate embeddings and store in ChromaDB
for i, title in enumerate(course_titles):
    text = f"{title} {categories[i]}"  # Combine title and category
    embedding = model.encode(text)
    
    collection.add(
        ids=[str(i)],
        embeddings=[embedding],
        metadatas=[{"title": title, "url": course_urls[i], "categories": categories[i]}]
    )

print(f"✅ Stored {len(course_titles)} courses in ChromaDB.")

# Search function
def search_course(query, top_n=10):
    query_embedding = model.encode(query)
    
    results = collection.query(query_embeddings=[query_embedding], n_results=top_n)
    
    # Extract metadata correctly
    metadata_results = results["metadatas"][0]  
    
    return metadata_results 


if __name__ == "__main__":
    query = input("🔎 Enter search query: ")
    results = search_course(query)
    for res in results:
        print(f"📌 {res['title']} - {res['categories']} [🔗 {res['url']}]")
