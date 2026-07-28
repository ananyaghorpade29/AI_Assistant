# responsible for embedding and semantic search

"""
Utilities for preparing documents for the vector store.

This module currently splits large text into
smaller overlapping chunks.
"""

def split_text(
	text:str,
	chunk_size= 500,
	chunk_overlap=100,
) -> list[str]:

	if chunk_size <= 0:
		raise ValueError(" chunk_size must be greater than 0.")

	if chunk_overlap < 0:
		raise ValueError("chunk_overlap cannot be negative.")

	if chunk_overlap >= chunk_size:
		raise ValueError(
			"chunk_overlap is small than chunk_size"
		)

	if not text.strip():
		return []

	chunks = []
	start = 0
	step = chunk_size - chunk_overlap

	while start < len(text):
		end = start + chunk_size
		chunk = text[start:end]
		chunks.append(chunk)
		start += step
	return chunks
