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
    search_faiss,)
from tools.tool_router import choose_tool



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
	create_database()
	index = load_index()
	chunks = load_chunks()
	model = load_embedding_model()
	while True:
		show_menu()
		choice  = input("\nChoose an option: ")

		if choice == "1":
			question = input("\nAsk your Question: ").strip()
			if not question:
				print("Please enter a question.")
				input("\nPress Enter to continue...")
				continue

			print(type(index))
			print(index)

			chunk,similarity_score = search_faiss(
				question,
				chunks,
				index,
				model,
				)
			print("\nBest_match:\n")
			print(chunk)

			print(f"\nSimilarity_score: {similarity_score:.4f}\n")

			input("\nPress Enter to continue...")

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


