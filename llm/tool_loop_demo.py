from langchain_core.messages import ToolMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from config import GEMINI_MODEL


@tool
def student_database(query: str) -> str:
	"""
	Search the student database for information
	about students, enrollment, counts, and records.
	"""
	return "There are 18 students enrolled."


model = ChatGoogleGenerativeAI(model=GEMINI_MODEL,)
model_with_tools = model.bind_tools([student_database])


query = "How many students are enrolled?"

#ask gemini
response = model_with_tools.invoke(query)
print("First Response:")
print(response)

#check if gemini requested a tool
if response.tool_calls:
	tool_call = response.tool_calls[0]

	print("\nTool Selected:")
	print(tool_call["name"])

	print("\nArguments:")
	print(tool_call["args"])

#execute tool
	tool_result = student_database.invoke(tool_call["args"])

	print("\nTool Result:")
	print(tool_result)

#create tool message
	tool_message = ToolMessage(
		content = tool_result,
		tool_call_id = tool_call["id"],
		)

#send conversation + tool result back
	messages = [
		("human",query),
		response,
		tool_message,
		]

#ask gemini for final answer
	final_response = model_with_tools.invoke(messages)

	print("Final Answer:")
	print(final_response.content)

else:
	print("Gemini answered directly:")
	print(response.content)



