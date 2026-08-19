from langchain_core.tools import StructuredTool
from tools.database_tool import database_tool
from tools.pdf_tool import pdf_tool
from tools.web_search import web_search_tool
from tools.report_tool import generate_report


database_langchain_tool = StructuredTool.from_function(
	func = database_tool,
	name = "database",
	description =(
		"Search the student database for student records, "
		"enrollment information, and student counts."
		),
		)

pdf_langchain_tool = StructuredTool.from_function(
	func = pdf_tool,
	name = "pdf",
	description = (
		"Search the user's PDF documents and retrieve "
		"relevant information. Use this when the user "
		"asks about information contained in their PDFs."
		),
		)

web_langchain_tool = StructuredTool.from_function(
	func= web_search_tool,
	name= "web",
	description= (
		"Search the web for current or external information "
		"that is not available in the local database or PDFs."
		),
		)

report_langchain_tool = StructuredTool.from_function(
	func= generate_report,
	name = "report_generator",
	description = (
		"Create a PDF report from supplied content. "
		"Use this when the user explicitly asks to "
		"create or generate a report." 
		),
		)


LANGCHAIN_TOOLS= [
	database_langchain_tool,
	pdf_langchain_tool,
	web_langchain_tool,
	report_langchain_tool,
	]
