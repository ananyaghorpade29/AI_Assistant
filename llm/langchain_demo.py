from langchain_google_genai import ChatGoogleGenerativeAI
from google import genai
from config import GEMINI_MODEL

model = ChatGoogleGenerativeAI(
	model = GEMINI_MODEL
	)
response = model.invoke(
	"Explain what a transformer is in one sentence"
	)
print(response.content[0]["text"])

