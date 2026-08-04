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



def main():
#add the AI Assistant.

	print("-"*50)
	print("         AI ASSISTANT")
	print("-"*50)
	print("Type 'exit' to quit\n")

	while True:
	question = input("You: ").strip()

	if question.lower() == "exit":
		print("Goodbye!")
		break
	tool = choose_tool(question)
	print(f"Selected Tool: {tool}")

	if tool == "database":
		if "count" in question.lower() or "how many"in question.lower():
			print(count_students_tool())
		else:
			students = get_all_students
			for student in students:
				print(student)

	elif tool == "pdf":
		index = load_index()
		chunks = load_chunks()
		model = load_embedding_model()
		chunk,similarity_score = search_faiss(
			question,
			chunks,
			index,
			model,
			)
		print("\nAnswer:\n")
		print(chunk)

	else:
		print("Sorry, i dont know which tool can answer that :(")





if __name__ =="__main__":
	main()


