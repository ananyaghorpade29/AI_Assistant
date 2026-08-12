import re

def choose_tool(query: str) ->str:
	#decide which tool to handle

	query = query.lower()

	db_words = [
	"total", "number", "count", "database", "students",
	"list", "enrolled", "record", "db", "entries",
 	"everyone", "records"
	]

	pdf_words = ["pdf","document","chapter","page","ai","llm","ml","transformer",
	"transformers","attention","self-attention","embedding","embeddings","token",
	"tokens","decoder","encoder","prompt","prompting","fine-tuning","pretraining",
	"pre-training", "rag",
	]

	print("Query:",query)

	words = set(re.findall(r"\b\w+\b", query))

	has_db = any(word in words for word in db_words)
	has_pdf = any(word in words for word in pdf_words)


	if has_db and has_pdf:
		return "ambigious"

	if has_pdf:
		return "pdf"

	if has_db:
		return "database"

	return "web"


