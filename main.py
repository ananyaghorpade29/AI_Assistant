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
from tools.database_tool import database_tool
from tools.pdf_tool import pdf_tool
from tools.tool_registry import TOOLS
from llm.llm_router import (build_tool_list,choose_tool)



def execute_tool(tool_name:str, arguments:dict, query:str, max_retries:int=2,):
#execute selected too safely

	if tool_name not in TOOLS:
		return "Unknown tool selected."
	tool= TOOLS[tool_name]

	for attempt in range(max_retries + 1):

		try:
			print(
			f"Executing tool"
			f"(attempt {attempt+1})..."
			)


			if arguments:
				return tool["function"](**arguments)
			return tool["function"](query)

		except Exception as error:
			print(f"Tool Execution failed: {error}")

			if attempt < max_retries:
				print("Retrying...")

	print("Tool failed after all trials")
	return None



def main():
#add the AI Assistant.

	print("-"*50)
	print("         AI ASSISTANT")
	print("-"*50)
	print("Type 'exit' to quit\n")


	while True:
		query = input("\nYou: ").strip()

		if query.lower() == "exit":
			print("Goodbye!")
			print("\n" + "=" *70)
			break


		tool_name,arguments = choose_tool(query)


		print("\nTool: ",tool_name)
		print("Arguments: ", arguments)

		if tool_name is None:
			print("I could not determine which to use.")
			continue

		answer = execute_tool(tool_name, arguments, query, max_retries=2)

		if answer is None:
			print("The tool couldnt complete the request")
			continue

		print("\nAnswer: ")
		print(answer)

		print("="*70)




if __name__ =="__main__":
	main()



