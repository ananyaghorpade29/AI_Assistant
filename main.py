from pypdf import  PdfReader
from database.database import (create_database,
				add_student,
				get_all_students,
				update_student_info,
				delete_student)
from tools.database_tool import (add_student_tool,
				 list_students_tool,				 count_students_tool)


def main():
	#add the AI Assistant.
	print("Starting AI Assistant...")
	create_database()

	print("\nCurrent Students\n")
	print(list_students_tool())

	students = get_all_students()
	print("\nStudents in Database: ")
	for student in students:
		print(f"ID: {student['id']}")
		print(f"Name: {student['name']}")
		print(f"Course: {student['course']}")
		print(f"CGPA: {student['cgpa']}")
		print(f"Email: {student['email']}")
		print("-" * 50)

	print(count_students_tool())

if __name__ =="__main__":
	main()
