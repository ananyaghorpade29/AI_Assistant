from tools.langchain_tool import student_database

result =  student_database.invoke({
	"question" : " How many students are enrolled in the database?"
	})
print(result)
print(student_database.name)
print(student_database.description)

print(student_database.args_schema)

