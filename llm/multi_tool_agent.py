from langchain_google_genai import ChatGoogleGenerativeAI
from config import GEMINI_MODEL
from tools.langchain_registry import LANGCHAIN_TOOLS
from langchain_core.messages import ToolMessage

#create gemini model
model = ChatGoogleGenerativeAI(
	model = GEMINI_MODEL)

#give access to gemini
model_with_tools = model.bind_tools(LANGCHAIN_TOOLS)

#lookup dict
tool_map = {
	tool.name: tool
	for tool in LANGCHAIN_TOOLS}

#user question
query = "Explain transformers from my PDF."
messages= [("human",query)]


#agent loop
while True:
	#Ask gemini what to do
	response = model_with_tools.invoke(messages)
	messages.append(response)


#if gemini does not req a tool , it has produced final answer
	if not response.tool_calls:
		break

#execute reqd tools
	for tool_call in response.tool_calls:
		tool_name = tool_call["name"]
		tool = tool_map[tool_name]

		print("\nTool selected: ",tool_name)
		print("Arguments: ",tool_call["args"])

#execute tool
		tool_result = tool.invoke(
			tool_call["args"]
			)
		print("Tool result: ",tool_result)

#send result back to gemini
		tool_message = ToolMessage(
			content = str(tool_result),
			tool_call_id = tool_call["id"]
			)
		messages.append(tool_message)
#final response
print("\nfinal Anwer: ")
print(response.content)

