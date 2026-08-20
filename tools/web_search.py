from ddgs import DDGS

def web_search_tool(query:str) -> str:
#search the web and return result

	if not query.strip():
		return "Error: Search query is empty."

	try:

		with DDGS() as ddgs:
			results = list(ddgs.text(query, max_results=3,))

		if not results:
			return "\n\nNo results found.\n\n"

		output = []
		for i , result  in enumerate(results,start=1):
			output.append(
				f"Result {i}\n\n"
				f"Title: {result['title']}\n\n"
				f"Summary: {result['body']}\n\n"
				f"URL: {result['href']}\n"
				)
		return ("-" * 50 +"\n" + "-" * 50 + "\n").join(output)

	except Exception as error:
		return "Error: Search query is empty."


