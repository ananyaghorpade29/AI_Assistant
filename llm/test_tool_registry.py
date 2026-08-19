from tools.langchain_registry import LANGCHAIN_TOOLS

for tool in LANGCHAIN_TOOLS:
	print("Name: ", tool.name)
	print("Description: ",tool.description)
	print()

