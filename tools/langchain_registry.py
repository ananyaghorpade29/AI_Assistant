from langchain_core.tools import StructuredTool
from tools.database_tool import database_tool
from tools.pdf_tool import pdf_tool
from tools.web_search import web_search_tool

database_langchain_tool = StructuredTool.from_function(
	func = database_tool,
	name = "Database",
	description =(
		"Search the student database for student records, "
		"enrollment information, and student counts."
		),
		)

pdf_langchain_tool = StructuredTool.from_function(
	func = pdf_tool,
	name = "Pdf",
	description = (
		"Search the provided PDF documents and answer "
		"questions using information from those documents."
		),
		)

web_langchain_tool = StructuredTool.from_function(
	func= web_search_tool,
	name= "Web",
	description= (
		"Search the web for current or external information "
		"that is not available in the local database or PDFs."
		),
		)

LANGCHAIN_TOOLS= [
	database_langchain_tool,
	pdf_langchain_tool,
	web_langchain_tool,
	]
