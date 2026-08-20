import sqlite3
from pathlib import Path

MEMORY_DB = Path("database/memory.db")

def initialize_memory_database() -> None:
#create long term memory

	connection = sqlite3.connect(MEMORY_DB)
	cursor = connection.cursor()
	cursor.execute(
		"""
		CREATE TABLE IF NOT EXISTS memories(
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			category TEXT NOT NULL,
			content TEXT NOT NULL,
			created_at TIMESTAMP DEFAULT CURRENT_TIME
			)
		"""
		)
	connection.commit()
	connection.close()

def add_memory(
	category:str,
	content:str,
	) -> None:
#store impotant info for long term

	connection = sqlite3.connect(MEMORY_DB)
	cursor = connection.cursor()
	cursor.execute(
		"""
		INSERT INTO memories (category, content)
		VALUES (?,?)
		""",
		(category, content),
	)

	connection.commit()
	connection.close()

def get_memories() -> list:
#retrieve all long-term memories

	connection = sqlite3.connect(MEMORY_DB)
	cursor = connection.cursor()
	cursor.execute(
		"""
		SELECT id, category, content, created_at
		FROM memories
		ORDER BY id
		"""
	)

	rows = cursor.fetchall()
	connection.close()
	return rows


if __name__ == "__main__":
	initialize_memory_database()

	add_memory(
		"project",
		"The AI Assistant use SQLite.",
	)
	memories = get_memories()
	for memory in memories:
		print(memory)


