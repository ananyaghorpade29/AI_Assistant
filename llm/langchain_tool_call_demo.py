from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool

from config import GEMINI_MODEL


@tool
def student_database(query:str) ->str:
	"""
	Search for student databse for info about students, count, enrollment, and records
	"""
	return f"Database recieved the question: {query}"

model = ChatGoogleGenerativeAI(
	model = GEMINI_MODEL,
	)
model_with_tools = model.bind_tools(
	[student_database])

response = model_with_tools.invoke("How many students are enrolled?")

print("Content")
print(response.content)
print("\nTool Call")
print(response.tool_calls)

if response.tool_calls:
	tool_call = response.tool_calls[0]
	tool_result = student_database.invoke(tool_call["args"])

	print("Tool Result: ",tool_result)
	print("Tool name: ", tool_call["name"])
	print("Arguments: ", tool_call["args"])


