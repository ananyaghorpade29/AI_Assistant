from pypdf import  PdfReader
from database.database import (create_database,
				add_student,
				get_all_students,
				update_student_cgpa,
				delete_student)
from tools.database_tool import (add_student_tool, list_students_tool)


def main():
	#add the AI Assistant.
	print("Starting AI Assistant...")
	create_database()

	print(add_student_tool("Ananya", "BscDs", 8.4," ananya@gmail.com" ))
	print(add_student_tool('Tishya', 'BscTech', 6.4, 'ananya@gmail.com'))
	print(add_student_tool('Nikita', 'LLM', 7.5, 'nikita@gmail.com'))
	print(add_student_tool('Mac', 'BTech', 8.7, 'mac@gmail.com'))
	print(add_student_tool('Aditya', 'BscDS', 6.4, 'aditya@gmail.com'))
	print(add_student_tool('Arya','BscDs', 7.5, 'arya@gmail.com'))
	print(add_student_tool('Parth', 'BPharm', 7.9, 'parth@gmail.com'))
	print(add_student_tool('Prachi', 'MBA', 8.0, 'prachi@gmail.com'))
	print(add_student_tool('Arinjay', 'BBS', 7.4, 'arinjay@gmail.com'))
	print(add_student_tool('Asmi', 'CBSE', 6.0, 'asmi@gmail.com'))
	print(add_student_tool('Arnev', 'CBSE', 7.0, 'arnev@gmail.com'))
	print(add_student_tool('Dwij', 'BCom', 6.6, 'dwij@gmail.com'))
	print(add_student_tool('Arnav', 'BTech', 8.2, 'arnav@gmail.com'))
	print(add_student_tool('Jayshree', 'BCom', 6.7, 'jayshree@gmail.com'))
	print(add_student_tool('Gucci', 'BBS', 9.0, 'gucci@gmail.com'))
	print(add_student_tool('Prisha', 'BscDs', 8.7, 'prisha@gmail.com'))
	print(add_student_tool('Dhruv', 'BTech', 5.0, 'dhruv@gmail.com'))
	print(add_student_tool('Sonali', 'BTech',8.3,'sonali@gmail.com'))
	print("\nCurrent STudents\n")
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


if __name__ =="__main__":
	main()
