
from vectorstore.embeddings import load_embedding_model
from vectorstore.faiss_search import search_faiss
from vectorstore.index_manager import (load_chunks, load_index)


def pdf_tool(query:str):
#search the pdf for user query
	index = load_index()
	chunks = load_chunks()
	model = load_embedding_model()
	chunk,similarity_score, distance = search_faiss(
		query,
		chunks,
		index,
		model,
		)
	return (
		f"\nBest Match:\n {chunk}"
		f"\n\nSimilarity score: \n{similarity_score:.4f}"
		f"\n\nDistance: \n{distance:.4f}"
		)
