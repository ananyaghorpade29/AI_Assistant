from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI

from config import GEMINI_MODEL
from tools.langchain_registry import LANGCHAIN_TOOLS


model = ChatGoogleGenerativeAI(
	model = GEMINI_MODEL,)

agent = create_agent(
	model = model,
	tools = LANGCHAIN_TOOLS,
	)
query = (
	"Search my PDF documents for information about "
	"transformer architecture. Then create a PDF report "
	"using the information you found. After creating the "
	"report, tell me where it was saved."
	)

result = agent.invoke(
	{
	"messages":[
		{
		"role": "user",
		"content": query,
		}
		]
	}
)

final_message = result["message"][-1]

print("\n===== AGENT TRACE =====")

for message in result["messages"]:
	print("\n",type(message).__name__)
	print(message)

