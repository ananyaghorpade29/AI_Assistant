"""
Demonstrate cosine similarity between sentence embeddings.
"""
from sentence_transformers import util
from embeddings import (
	create_embedding,
	load_embedding_model,)

def main():
	#compare meanings of 2 sentences

	model = load_embedding_model()
	sentence1 = ("Machine Learning uses data")
	sentence2 = ("AL models learn from examples")

	embedding1 = create_embedding(sentence1, model,)
	embedding2 = create_embedding(sentence2, model,)

	similarity = util.cos_sim(embedding1, embedding2)
	print("Sentence1: ")
	print(sentence1)

	print("Sentence2: ")
	print(sentence2)

	print("\nCosine Similarity: ")
	print(similarity)

	score = similarity.item()
	print(score)


if __name__ == "__main__":
	main()
