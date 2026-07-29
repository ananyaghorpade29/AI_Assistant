"""
Simple semantic search using cosine similarity.
This version checks every chunk one by one.
"""
from sentence_transformers import util
from vectorstore.embeddings import (
	create_embedding,
	load_embedding_model,)

def semantic_search(
	query:str,
	chunks:list[str],
	) -> tuple[str,float]:
	#return most similar chunk and its score

	model  = load_embedding_model()
	query_embedding = create_embedding(query, model,)
	best_chunk= ""
	best_score =-1.0

	for chunk in chunks:
		chunk_embedding = create_embedding(chunk, model,)

		score= util.cos_sim(query_embedding, chunk_embedding,).item()
		if score > best_score:
			best_score = score
			best_chunk = chunk
	return (best_chunk, best_score,)
