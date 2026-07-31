#end to end semantic search demo

from config import PDF_PATH
from tools.pdf_reader import read_pdf
from vectoerstore.build_vectorstore import split_text
from vectorstore.faiss_search import  build_faiss_index, search_faiss


def main():
	pdf_text = read_pd(PDF_PATH)

	chunks = split_text(pdf_text)

	index, model = build_faiss_index(chunks)

	question = input("ASK A QUESTION: ")

	chunk, distance = search_faiss(
	question,
	chunks,
	index,
	model,
	)

	print("\nBest Matching chunk:\n")
	print(chunk)

	print("\nDistance:")
	print(distance)

if __name__ == "__main__":
	main()
