from pypdf import  PdfReader
from database.database import (create_database,
				add_student,
				get_all_students,
				update_student_info,
				delete_student)
from tools.database_tool import (add_student_tool,
				 list_students_tool,
				 count_students_tool)
from config  import PDF_FILES
from tools.pdf_reader import read_pdf
from vectorstore.build_vectorstore import split_text
from vectorstore.embeddings import (create_embedding, load_embedding_model,)
from vectorstore.semantic_search import semantic_search
from vectorstore.faiss_search import search_faiss
from vectorstore.index_manager import (load_chunks, load_index,)
from vectorstore.faiss_search import (
    build_faiss_index,
    search_faiss,
)


def show_menu():
	print("\n" + "=" *50)
	print("        AI Assistant")
	print("="*50)
	print("Welcome to the AI Assistant")
	print("1. Search PDF")
	print("2. Show Students")
	print("3. Count Students")
	print("4. Exit")



def main():
#add the AI Assistant.
	print("Starting AI Assistant...")
	create_database()

#add students.
#print all students
	print("\nCurrent Students\n")
	print(list_students_tool())

	students = get_all_students()

#print students according to their info
	print("\nStudents in Database: ")
	for student in students:
		print(f"ID: {student['id']}")
		print(f"Name: {student['name']}")
		print(f"Course: {student['course']}")
		print(f"CGPA: {student['cgpa']}")
		print(f"Email: {student['email']}")
		print("-" * 50)

#count total students
	print(count_students_tool())
	print("-" * 50)

#print pdf in chunks
	all_chunks =[]
	for pdf_path in PDF_FILES:
		print(f"Readinf {pdf_path.name}...")
		pdf_text = read_pdf(pdf_path)
		chunks =split_text(pdf_text)
		all_chunks.extend(chunks)
	index, model = build_faiss_index(all_chunks)

	print(f"Number of chunks:{len(chunks)}\n")
	for number, chunk in enumerate(chunks,start=1):
		print(f"---chunk{number}---")
		print(chunk)
		print()

#creating embeddings
	print("Loading Embedding model...")
	model = load_embedding_model()
	sentence1 = "Python is a widely used in data science and linux in software developer and IT operations"
	sentence2= "I am working on AI Assistant porject"
	embedding1 =  create_embedding(sentence1,model)
	embedding2 = create_embedding(sentence2,model)

	print("-"*50)
	print("\nOriginal text: ")
	print(f"{sentence1}\n{sentence2}")

	print("-"*50)
	print("\nEmbedding value:")
	print(f"{embedding1}\n{embedding2}")

	print("-"*50)
	print("\nEmbedding type:")
	print(f"{type(embedding1)}\n{type(embedding2)}")

	print("-"*50)
	print("\nEmbedding Shape:")
	print(f"{embedding1.shape}\n{embedding2.shape}")

#semnatic search
	chunks = [
		"Python is a programming language.",
		"Machine learning allows computers to learn from data.",
		"SQLite is a lightweight database.",
		"Artificial intelligence uses neural networks.",
		"Deep learning is a subset of machine learning.",
		]
	question =("what is deep learning??")
	chunk,  score = semantic_search(question,chunks,)
	print("Question:")
	print(question)

	print("\nBest match:")
	print(chunk)

	print("\nSimilarity:")
	print(score)

	while True:
		show_menu()
		choice  = input("\nChoose an option: ")

		if choice == "1":
			question = input("\nAsk your Question: ")
			index = load_index()
			chunks = load_chunks()
			model = load_embedding_model()
			while True:
				chunk,similarity_score = search_faiss(
					question,
					chunks,
					index,
					model
					)
			print("\nBest_match:\n")
			print(chunk)

			print(f"\nSimilarity_score: {similarity_score:.4f}\n")

			print("\n" + "Press Enter to continue...")

		elif choice == "2":
			students = list_students_tool()

			print("\nStudents\n")
			for index,student in enumerate(students,start=1):
				student_id, name, course, cgpa, email = tuple(student)
				print(
				f"{index}. | "
				f"ID: {student_id:<3} | "
				f"Name: {name:<10} | "
				f"Course: {course:<12} | "
				f"CGPA: {cgpa:<5} | "
				f"Email: {email}"
				)
			print("=" * 50)
			input("\nPress Enter to continue...")

		elif choice == "3":
			total = count_students_tool()
			print()
			print(total)
			input("\nPress Enter to continue...")


		elif choice == "4":
			print("\nGoodbye!")
			break

		else:
			print("Invalid option.")
			input("\nPress Enter to continue...")

if __name__ =="__main__":
	main()


