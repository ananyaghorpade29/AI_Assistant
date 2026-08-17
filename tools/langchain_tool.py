from langchain_core.tools import tool
from database.database import count_students 
@tool
def student_database(query:str) -> str:
	"""
	Search the student database for info about
	students, enrollment, counts and records.
	"""

	query = query.lower()
	if (
		"how many" in query
		or "count" in query
		or "total" in query
		or "enrolled" in query
		):
		result = count_students()
		return str(result)


	return ("Database tool could not determine."
		"what database was requested"
		)



