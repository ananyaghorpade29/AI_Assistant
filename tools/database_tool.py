"""
Database tool for the AI Assistant.

This module provides a high-level interface
for interacting with the student database.
"""

from database.database import (add_student, get_all_students,search_students,)

def database_tool(query: str):
#handle db queries
	query = query.lower()
	db_count = ["total","number", "database","count", "how many",]
	db_all = ["list", "who", "all","database","everyone","show", "student", "students", "records",]

	if any(word in query for word in db_count):
		return count_students_tool()

	elif any(word in query for word in db_all):
		students = get_all_students()

		result = []
		for student in students:
			result.append(str(dict(student)))
		return "\n".join(result)

	return search_students_tool(query)



def add_student_tool(name:str, course:str, cgpa:float, email:str):
	#add a student using the database module.
	success = add_student(name, course, cgpa, email)
	if success:
		return f"Student '{name}' added successfully."
	return "Failed to add student."

def list_students_tool():
	#Retrieve all students in readable format.
	students = get_all_students()
	if not students:
		return "no students found."
	return students

def count_students_tool():
	#count all students in db
	students =  get_all_students()
	count= len(students)
	return f"Total students:{count}"

def search_students_tool(search_term:str):
	students = search_students(search_term)
	if not students:
		return "No matching students found"

	result =[]
	for student in students:
		result.append(str(dict(student)))
	return "\n".join(result)


