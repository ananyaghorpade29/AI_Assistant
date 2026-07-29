#convert text to vectors

"""
Embedding utilities for the AI Assistant.

This module loads a sentence-transformer model
and converts text into numerical embeddings.
"""

from sentence_transformers import SentenceTransformer

MODEL_NAME = "all-MiniLM-L6-v2"

def load_embedding_model() -> SentenceTransformer:

	model = SentenceTransformer(MODEL_NAME)
	return model

def create_embedding(
	text:str,
	model:SentenceTransformer,
	):

	embedding = model.encode(text)
	return embedding

