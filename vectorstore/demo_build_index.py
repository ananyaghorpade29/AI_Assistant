
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
        all_chunks =[]
        for pdf_path in PDF_FILES:
                print(f"Readinf {pdf_path.name}...")
                pdf_text = read_pdf(pdf_path)
                chunks =split_text(pdf_text)
                all_chunks.extend(chunks)
        index, model = build_faiss_index(all_chunks)

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
