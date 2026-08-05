

from duckduckgo_search import DDGS

def web_search_tool(question:str) -> str:
#search the web and return result

	with DDGS as ddgs:
		results = list(
			ddgs.text(question, max_results=3,)
			)
	if not results:
		return "No results found."

	result = result[0]

	return (
		f"Title: {result['title']}\n\n"
		f"Summary: {result['body'}}\n\n"
		f"URL: {result['href']}"
		)

