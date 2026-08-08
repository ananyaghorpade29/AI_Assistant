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
from llm.llm_router import choose_tool
from tools.database_tool import database_tool
from tools.pdf_tool import pdf_tool
from tools.tool_registry import TOOLS

def main():
#add the AI Assistant.

	print("-"*50)
	print("         AI ASSISTANT")
	print("-"*50)
	print("Type 'exit' to quit\n")

	while True:
		question = input("\n\nYou: ").strip()

		if question.lower() == "exit":
			print("Goodbye!")
			print("\n\n" + "=" *70)
			break


		tool_name = choose_tool(question)
		print("\nTool selected: ", tool_name)

		if tool_name == "unknown":
			print("\nI dont know which tool to use.\n")
			continue

		tool = TOOLS[tool_name]
		print("\nTool:",tool)

		answer = tool["function"](question)
		print(answer)
		print("="*70)



if __name__ =="__main__":
	main()


