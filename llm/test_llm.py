import ollama

respone = ollama.chat(
	model = "llama3.2:3b",
	messages=[{
	"role":"user",
	"content": "what is python",
	}],)
print(response["message"]["content"])

