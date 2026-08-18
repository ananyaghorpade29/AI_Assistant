from tools.langchain_tools import LANGCHAIN_TOOLS

for tool in LANGCHAIN_TOOLSL:
	print("Name: ", tool.name)
	print("Description: ",tool.description)
	print()

