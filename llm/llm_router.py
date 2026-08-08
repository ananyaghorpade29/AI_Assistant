
import os

from tools.tool_registry import TOOLS
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


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

	Available tools: 
	{tools}
	Return only the tool name.

	Question: {question}
	"""
	return prompt

def choose_tool(question):
	api_key=os.getenv("OPENAI_API_KEY")

	if not api_key:
		print("Error: API KEY not set")
		return "web"

	prompt = build_prompt(question)

	try:
		response = client.responses.create(
			model ="gpt-4.1-mini",
			input=prompt,
			)
	except Exception as error:
		print(f"LLM request failed: {error}")
		return "web"

	tool_name = response.output_text.strip().lower()

	if tool_name not in TOOLS:
		print(f"Error: Unknown tool returned by LLM: {tool_name}")
		print("Falling back to web search")
		return "web"
	return tool_name









