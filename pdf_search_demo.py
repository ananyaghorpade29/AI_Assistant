
from config import PDF_PATH
from tools.pdf_reader import read_pdf
from vectorstore.build_vectorstore import split_text
from vectorstore.faiss_search import  build_faiss_index, search_faiss


def main():
	print("Step 1: Reading PDF..")
	pdf_text = read_pdf(PDF_PATH)
	print("PDF read successfully")

	print("Step 2: Splitting text")
	chunks = split_text(pdf_text)
	print(f"Created {len(chunks)} chunks")

	print("Step 3: Building FAISS index...")
	index, model = build_faiss_index(chunks)
	print("FAISS created successfully")

	print("Step 4: Waiting for a question...")
	question = input("ASK A QUESTION: ")

	print("Step 5: Searching...")
	chunk, distance = search_faiss(
	question,
	chunks,
	index,
	model,
	)
	print("Search complete")

	print("\nBest Matching chunk:\n")
	print(chunk)

	print("\nDistance:")
	print(distance)

if __name__ == "__main__":
	main()


