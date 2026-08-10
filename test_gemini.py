from google import genai

client=  genai.Client()

response = client.models.generate_content(
	model = "gemini-3.6-flash",
	contents = "Explain what an AI Agent is in one sentence"
	)
print(response.text)
