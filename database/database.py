import sqlite3
from pathlib import Path

DATABASE_PATH = Path(__file__).parent/"students.db"


def create_database():
	with sqlite3.connect(DATABASE_PATH) as connection:

		cursor = connection.cursor()
		cursor.execute("DROP TABLE IF EXISTS students")

		cursor.execute(
        		""" 
			CREATE TABLE IF NOT EXISTS students(
				id INTEGER PRIMARY KEY,
				name TEXT NOT NULL,
				course TEXT NOT NULL,
				cgpa REAL NOT NULL,
				email TEXT UNIQUE
			)
			"""
		)
	print("Database created successfully!")

def add_student(name:str, course:str,cgpa:float, email:str):
	try:

		with sqlite3.connect(DATABASE_PATH) as connection:
			cursor = connection.cursor()
			cursor.execute(
				"""
				INSERT INTO students(name, course, cgpa, email)
				VALUES(?,?,?,?)
				""",
				(name, course, cgpa, email),
			)
		return True
		print(f"ADDED student:{name}")

	except sqlite3.Error:
		return False


def get_all_students():
	with sqlite3.connect(DATABASE_PATH) as connection:
		connection.row_factory =  sqlite3.Row
		cursor = connection.cursor()
		cursor.execute("SELECT * FROM students")
		students = cursor.fetchall()
	return students


def update_student_info(
			student_id:int,
			new_name:str =None,
			new_course:str=None,
			new_cgpa:float=None,
			new_email:str=None
			):
	with sqlite3.connect(DATABASE_PATH) as connection:

		cursor = connection.cursor()
		update= []
		values= []

		if name is not None:
			update.append("name= ?")
			values.append(name)

		if course is not None:
			update.append("course= ?")
			values.append(course)

		if cgpa is not None:
			update.append("cgpa= ?")
			values.append(cgpa)

		if email is not None:
			update.append("email =?")
			values.append(email)

		if not updates:
			return "no fields to update"

		values.append(student_id)

		query = f"""
			UPDATE students 
			SET {",".join(update)}
			WHERE id = ?
			"""
		cursor.execute(query,values)
		cursor.commit()

	print("Student updated.")

def delete_student(student_id:int):
	with sqlite3.connect(DATABASE_PATH) as connection:

		cursor = connection.cursor()
		cursor.execute(
			"""
			DELETE FROM students 
			WHERE id = ?
			""",
			(student_id,),
		)
	print("Student deleted.")



