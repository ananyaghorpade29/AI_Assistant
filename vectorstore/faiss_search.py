import faiss
import numpy as np
from vectorstore.embeddings import(
	create_embedding,
	load_embedding_model,)

def build_faiss_index(chunks:list[str]):
	model = load_embedding_model()
	embeddings = []
	for chunk in chunks:
		embedding = create_embedding(chunk,model)
		embeddings.append(embedding)

	embeddings = np.array(embeddings).astype("float32")
	print(type(embedding))
	print(embedding.shape)
	dimension = embeddings.shape[1]
	index = faiss.IndexFlatL2(dimension)
	index.add(embeddings)
	return index, model
def search_faiss(query:str,
		chunks:list[str],
		index,
		model,):
	query_embedding = create_embedding(query,model)
	query_embedding = np.array(query_embedding).astype("float32")
	query_embedding = query_embedding.reshape(1,-1)
	distances, indices = index.search(query_embedding, k=3)
	best_index = indices[0][0]
	best_distance = distances[0][0]
	return chunks[best_index], best_distance

def main():
	chunks =[
	"Python is a programming language.",
	"Machine learning allows computers to learn from data.",
	"SQLite is a lightweight database.",
	"Artificial intelligence uses neural networks.",
	]

	index, model = build_faiss_index(chunks)
	question = "how do computers learn data?"

	chunk, distance= search_faiss(
	question,
	chunks,
	index,
	model,)

	print("question:")
	print(question)

	print("\nBest mMatch:")
	print(chunk)

	print("\nDistance")
	print(distance)
if __name__ == "__main__":
	main()
