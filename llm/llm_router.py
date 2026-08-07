
from tools.tool_registry import TOOLS

def buils_tool_list() ->str:
#convert tool registry into prompt text

	lines = []
	for name, info in TOOLS.items():

		lines.append(
			f"{name}: {info[''description']}"
			)
	return "\n".join(lines)

def build_prompt(question:str) -> str:
	tools = built_tool_list()

	prompt = f"""
	You are a tool-selection assistant.

	Available tools: 
	{tools}
	Return only the tool name.

	Question: {question}
	"""
	return prompt
