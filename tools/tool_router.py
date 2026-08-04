

def choose_tool(question: str) ->str:
	#decide which tool to handle
	question = question.lower()
	db_words = ["database", "student","enrolled","record", "count", "db","entries"]
	pdf_words = ["pdf", "document","file", "chapter","page", "AI","llm","ml","transformers"]

	if any(w in question for w in pdf_words):
		return  "pdf"

	if any (w in question for w in db_words):
		return "database"

	return "unknown"


questions  = [
	"show all student",
	"read pdf database of all the students from the document database or the pdf",
	"count students",
	"search the PDF",
	"Read the document",
	"whats todays weather",
	]
for q in questions:
	print(q)
	print("->", choose_tool(q))
	print()
