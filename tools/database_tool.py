


"""
Database tool for the AI Assistant.

This module provides a high-level interface
for interacting with the student database.
"""

from database.database import (add_student, get_all_students,)

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

	output = []

	for student in students:
		output.append(
		f"ID: {student[0]} | "
		f"Name: {student[1]} | "
		f"Course: {student[2]} | "
		f"Cgpa: {student[3]} | "
		f"Email: {student[4]} | "
		)
	return "\n".join(output)
