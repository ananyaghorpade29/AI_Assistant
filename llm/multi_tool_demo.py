from langchain_google_genai import ChatGoogleGenerativeAI
from config import GEMINI_MODEL
from tools.langchain_registry import LANGCHAIN_TOOLS

model = ChatGoogleGenerativeAI(
	model = GEMINI_MODEL)

model_with_tools = model.bind_tools(LANGCHAIN_TOOLS)

query = [
	"how many students are enrolled?",
	"Explain transformers from my pdf",
	"what is the latest Python version?",
	]

for que in query:
	print("\n" + "=" *70)
	print("Question", query)

	response = model_with_tools.invoke(query)

	print("\nTool calls")
	print(response.tool_calls)
	print("\nDirect response")
	print(response.content)

