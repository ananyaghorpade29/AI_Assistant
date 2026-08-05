

def choose_tool(question: str) ->str:
	#decide which tool to handle
	question = question.lower()
	db_words = ["total","number","count", "how many","database", "students","list","how","who","enrolled","record", "db","entries","show","list","all","everyone","who","student","students","records",]
	pdf_words = ["pdf", "document","file", "chapter","page", "ai","page","transformer","transformers","llm","ml","transformers"]

	has_pdf = any(w in question for w in pdf_words)
	has_db  =  any (w in question for w in db_words)

	if has_pdf and has_db:
		return "ambigious"
	if has_pdf:
		return "pdf"
	if has_db:
		return "database"
	return "web"


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
