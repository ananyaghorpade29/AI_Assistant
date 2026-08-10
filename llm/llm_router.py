from google import genai
import os

from tools.tool_registry import TOOLS


client = genai.Client()


def build_tool_list() ->str:
#convert tool registry into prompt text

	lines = []
	for name, info in TOOLS.items():

		lines.append(
			f"{name}: {info['description']}"
			)
	return "\n".join(lines)


def build_prompt(question:str) -> str:
	tools = build_tool_list()

	prompt = f"""
	You are a tool-selection assistant.

	Your job is to select the most appropriate
	tool for the user's question.

	Available tools: 
	{tools}

	Return only the tool name.

	User question: {question}
	"""
	return prompt

def choose_tool(question):
	api_key=os.getenv("GEMINI_API_KEY")

	if not api_key:
		print("Error: API KEY not set")
		return "web"

	prompt = build_prompt(question)

	try:
		response = client.models.generate_content(
			model ="gemini-3.6-flash",
			contents = prompt,
			)
	except Exception as error:
		print(f"LLM request failed: {error}")
		return "web"

	tool_name = response.text.strip().lower()

	if tool_name not in TOOLS:
		print(f"Error: Unknown tool returned by LLM: {tool_name}")
		print("Falling back to web search")
		return "web"
	return tool_name



