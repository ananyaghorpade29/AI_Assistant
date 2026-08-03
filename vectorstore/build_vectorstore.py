# responsible for embedding and semantic search

"""
Utilities for preparing documents for the vector store.

This module currently splits large text into
smaller overlapping chunks.
"""

def split_text(
	text:str,
	chunk_size= 300,
	chunk_overlap=50,
) -> list[str]:


	"""
	Split text into smaller overlapping chunks.
	Args:
	text: The complete text to split.
	chunk_size: Maximum number of characters in each chunk.
	chunk_overlap: Number of characters shared by nearby chunks.
	Returns:
	A list containing the text chunks.
	Raises:
	ValueError: If the chunk settings are invalid.
	"""

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

	for i, chunk in enumerate(chunks):
		print(f"\nChunk{i}")
		print(chunk)
		print("=" *60)

	return chunks



















