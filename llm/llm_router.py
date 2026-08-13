
import os
from google import genai
from tools.tool_registry import TOOLS
from google.genai import types
from llm.memory import (
	add_user_message,
	add_assistant_message,
	get_history,
	clear_history,)



def create_client():
#GEMINI API client
	api_key = os.getenv("GEMINI_API_KEY")

	if not api_key:
		raise ValueError("GEMINI_API_KEY is not set.")

	return genai.Client(api_key=api_key)
client = create_client()




def build_function_declarations():
#convert tool registry into gemini tool declaration
	declarations = []
	for name, info in TOOLS.items():
		declaration = types.FunctionDeclaration(
			name= name,
			description = info["description"],
			parameters = types.Schema(
				type = info["parameters"]["type"],
				properties = {
					key : types.Schema(
						type= value["type"],
						description = value["description"]
						)
					for key, value
					in info["parameters"]["properties"].items()
					},
					required=info["parameters"].get("required",[]),
				),
			)
		declarations.append(declaration)
	return declarations




def build_gemini_tools():
#create gemini tool object
	declarations = build_function_declarations()
	return types.Tool( function_declarations= declarations)




def build_tool_list() ->str:
#convert tool registry into prompt text

	lines = []
	for name, info in TOOLS.items():

		lines.append(
			f"{name}: {info['description']}"
			)
	return "\n".join(lines)




def choose_tool(query):
#ask GEMINI to select appropriate tool
	gemini_tool = build_gemini_tools()
	context = build_conversation_context(query)

	print("\n=======MEMORY========")
	print(context)
	print("========================")

	try:
		response = client.models.generate_content(
			model ="gemini-3.6-flash",
			contents = context,
			config = types.GenerateContentConfig(
				tools = [gemini_tool]
				),
			)
		add_user_message(query)

	except Exception as error:
		print(f"LLM request failed: {error}")
		return None, {}

	if not response.function_calls:
		print("Gemini did not select a tool.")
		return None, {}

	function_calls = response.function_calls[0]

	tool_name =  function_calls.name
	arguments =  dict(function_calls.args or {})

	print(f"Tool name: {tool_name}")
	print(f"Arguments: {arguments}")

	if tool_name not in TOOLS:
		print("Unknown tool:" , tool_name)
		return None, {}

	tool = TOOLS[tool_name]


	return tool_name,arguments


def build_conversation_context(question:str) -> str:
#build a prompt containing conversation history.

	history = get_history()
	lines= []

	for message in history:
		role = message["role"]
		content = message["content"]

		lines.append(f"{role}:{content}")
	lines.append(f"user:{question}")
	return "\n".join(lines)
