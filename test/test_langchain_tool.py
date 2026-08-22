from tools.langchain_tool import student_database

result =  student_database.invoke({
	"query" : " How many students are enrolled in the database?"
	})
print("Result:" ,result)
print("Name: ", student_database.name)
print("Description:", student_database.description)

print(student_database.args_schema)

