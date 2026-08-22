#final all-tool connect
from langchain.tools import tool

from tools.database_tool import database_tool
from tools.pdf_tool import pdf_tool
from tools.web_search import web_search_tool

@tool
def database_search(query:str) -> str:
	"""
	Search student dtaabase for student records enrollment
	courses, department, CGPA, grades, name, id and student count.
	Use for information stored in local database, not PDF or Web.
	"""
	return database_tool(query)

@tool
def pdf_search(query:str) ->str:
	"""
	Search the user's PDF documents for relevant information,
	explanations, concepts, facts, and topics contained in the PDFs.
 	Use when the user asks about information from their documents.
	"""
	return pdf_tool(query)

@tool
def web_search(quer:str) ->str:
	"""
	Search the web for current or external information, such as
	latest news, software versions, documentation, prices, or facts
	not available in the local database or PDF documents.
	"""
	return web_search_tool(query)

TOOLS = [
	database_search,
	pdf_search,
	web_search,
	]

