from pypdf import  PdfReader
from database.database import (create_database,
				add_student,
				get_all_students,
				update_student_info,
				delete_student)
from tools.database_tool import (add_student_tool,
				 list_students_tool,
				 count_students_tool)
from config  import PDF_PATH
from tools.pdf_reader import read_pdf
from vectorstore.build_vectorstore import split_text


def main():
	#add the AI Assistant.
	print("Starting AI Assistant...")
	create_database()

#add students.
#print all students
	print("\nCurrent Students\n")
	print(list_students_tool())

	students = get_all_students()

#print students according to their info
	print("\nStudents in Database: ")
	for student in students:
		print(f"ID: {student['id']}")
		print(f"Name: {student['name']}")
		print(f"Course: {student['course']}")
		print(f"CGPA: {student['cgpa']}")
		print(f"Email: {student['email']}")
		print("-" * 50)

#count total students
	print(count_students_tool())
	print("-" * 50)

#print pdf as a single string
	print(f"\nReading pdf...\n")
	text = read_pdf(PDF_PATH)
	print(text)
	print("-"*50)

#print pdf in chunks
	pdf_text = read_pdf(PDF_PATH)
	chunks =split_text(
			pdf_text,
			chunk_size=500,
			chunk_overlap=100,)

	print(f"Number of chunks:{len(chunks)}\n")
	for number, chunk in enumerate(chunks,start=1):
		print(f"---chunk{number}---")
		print(chunk)
		print()

if __name__ =="__main__":
	main()
