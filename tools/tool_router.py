

def choose_tool(question: str) ->str:
	#decide which tool to handle
	question = question.lower()

	if (
		"student" in question
		or "database" in question
		):
		return "database"

	if (
		"pdf" in question
		or "document" in question
		):
		return "pdf"

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
