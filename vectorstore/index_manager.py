import pickle

import faiss

from config import FAISS_INDEX_DIR

INDEX_PATH = FAISS_INDEX_DIR / "index.faiss"
CHUNKS_PATH = FAISS_INDEX_DIR / "chunks.pkl"


def save_index(index):
	"""Save the FAISS index to disk."""
	faiss.write_index(index, str(INDEX_PATH))


def load_index():
	"""Load the FAISS index from disk."""
	return faiss.read_index(str(INDEX_PATH))


def save_chunks(chunks):
	"""Save the list of document chunks."""
	with open(CHUNKS_PATH, "wb") as file:
		pickle.dump(chunks, file)


def load_chunks():
	"""Load the list of document chunks."""
	with open(CHUNKS_PATH, "rb") as file:
		return pickle.load(file)import pickle

