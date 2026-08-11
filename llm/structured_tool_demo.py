from google.genai import types
from llm.gemini_client import create_gemini_client

client= create_gemini_client()

def search_pdf(query:str):
	return f"Searching PDF for:{query}"

search_pdf_declaration = types.FunctionDeclaration(
	name = "search_pdf",
	description = "Search the PDF documents for information",
	parameters = types.Schema(
		type= "OBJECT",
		properties ={
			"query":types.Schema(
				type="STRING",
				description = "The topic or question to search for",
				),
			},
			required=["query"],
		),
	)
tool= types.Tool(
	function_declarations=[search_pdf_declaration]
	)
response= client.models.generate_content(
	model = "gemini-3.6-flash",
	contents="Explain what is ai in brief.",
	config = types.GenerateContentConfig(
		tools= [tool]
	),
)
if response.function_calls:
	function_call = response.function_calls[0]

	print("Function:", function_call.name)
	print("Arguments:", function_call.args)
	result = search_pdf(**function_call.args)
	print(f"RESULT:{result}")
else:
	print("Gemini Returned:")
	print(response.text)


