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
from vectorstore.embeddings import (create_embedding, load_embedding_model,)
from vectorstore.semantic_search import semantic_search


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

#print pdf in chunks
	pdf_text = read_pdf(PDF_PATH)
	chunks =split_text(
			pdf_text,
			chunk_size=500,
			chunk_overlap=50,)

	print(f"Number of chunks:{len(chunks)}\n")
	for number, chunk in enumerate(chunks,start=1):
		print(f"---chunk{number}---")
		print(chunk)
		print()

#creating embeddings
	print("Loading Embedding model...")
	model = load_embedding_model()
	sentence1 = "Python is a widely used in data science and linux in software developer and IT operations"
	sentence2= "I am working on AI Assistant porject"
	embedding1 =  create_embedding(sentence1,model)
	embedding2 = create_embedding(sentence2,model)

	print("-"*50)
	print("\nOriginal text: ")
	print(f"{sentence1}\n{sentence2}")

	print("-"*50)
	print("\nEmbedding value:")
	print(f"{embedding1}\n{embedding2}")

	print("-"*50)
	print("\nEmbedding type:")
	print(f"{type(embedding1)}\n{type(embedding2)}")

	print("-"*50)
	print("\nEmbedding Shape:")
	print(f"{embedding1.shape}\n{embedding2.shape}")

#semnatic search
	chunks = [
		"Python is a programming language.",
		"Machine learning allows computers to learn from data.",
		"SQLite is a lightweight database.",
		"Artificial intelligence uses neural networks.",
		"Deep learning is a subset of machine learning.",
		]
	question =("what is deep learning??")
	chunk,  score = semantic_search(question,chunks,)
	print("Question:")
	print(question)

	print("\nBest match:")
	print(chunk)

	print("\nSimilarity:")
	print(score)


if __name__ =="__main__":
	main()
