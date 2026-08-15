
from config import PDF_FILES
from tools.pdf_reader import read_pdf
from vectorstore.build_vectorstore import split_text
from vectorstore.faiss_search import  build_faiss_index, search_faiss


def main():
	print("Step 1: Reading PDF..")
	pdf_text = read_pdf(PDF_FILES)
	print("PDF read successfully")

	print("Step 2: Splitting text")
	chunks = split_text(pdf_text)
	print(f"Created {len(chunks)} chunks")

	print("Step 3: Building FAISS index...")
	index, model = build_faiss_index(chunks)
	print("FAISS created successfully")

	print("Step 4: Waiting for a query...")
	query = input("ASK A QUERY: ")

	print("Step 5: Searching...")
	chunk,similarity_score, distance = search_faiss(
	query,
	chunks,
	index,
	model,
	)
	print("Search complete")

	print("\nBest Matching chunk:\n")
	print(chunk)

	print("\nSimilarity Score:")
	print(similarity_score)

	print("\nDistance:")
	print(distance)

if __name__ == "__main__":
	main()


