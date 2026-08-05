import faiss
import numpy as np
from vectorstore.embeddings import(
	create_embedding,
	load_embedding_model,)
from vectorstore.index_manager import (save_index, save_chunks,)


def build_faiss_index(chunks:list[str]):
	model = load_embedding_model()
	embeddings = model.encode(
		chunks,
		convert_to_numpy=True,
		show_progress_bar=True
		).astype("float32")
	embeddings = np.array(embeddings).astype("float32")
	faiss.normalize_L2(embeddings)
	print(type(embeddings))
	print(embeddings.shape)
	index = faiss.IndexFlatIP(embeddings.shape[1])
	index.add(embeddings)

	save_index(index)
	save_chunks(chunks)

	return index, model


def search_faiss(query:str,
		chunks:list[str],
		index,
		model,
		k: int=3,
		):
	query_embedding = create_embedding(query,model)
	query_embedding = np.array(query_embedding).astype("float32").reshape(1,-1)
	faiss.normalize_L2(query_embedding)

	similarity_score, indices = index.search(query_embedding, k)

	best_index = indices[0][0]
	best_similarity_score = similarity_score[0][0]
	best_chunk = chunks[best_index]

	chunk_embedding = create_embedding(best_chunk, model)
	chunk_embedding = np.array(chunk_embedding).astype("float32").reshape(1,-1)
	faiss.normalize_L2(chunk_embedding)

	distance = np.linalg.norm(query_embedding - chunk_embedding)

	return chunks[best_index], best_similarity_score, distance


def main():
	chunks =[
	"Python is a programming language.",
	"Machine learning allows computers to learn from data.",
	"SQLite is a lightweight database.",
	"Artificial intelligence uses neural networks.",
	]

	index, model = build_faiss_index(chunks)
	question = "how do computers learn data?"

	chunk, similarity_score= search_faiss(
	question,
	chunks,
	index,
	model,)

	print("question:")
	print(question)

	print("\nBest mMatch:")
	print(chunk)

	print("\nSimilarity Score")
	print(similarity_score)
if __name__ == "__main__":
	main()
