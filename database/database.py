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


def update_student_cgpa(student_id:int,new_cgpa:float):
	with sqlite3.connect(DATABASE_PATH) as connection:

		cursor = connection.cursor()
		cursor.execute(
			"""
			UPDATE students 
			SET  cgpa = ?
			WHERE id = ?
			""",
			(new_cgpa, student_id),
		)
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



