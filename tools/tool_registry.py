

from tools.database_tool import database_tool
from tools.pdf_tool import pdf_tool
from tools.web_search import web_search_tool

TOOLS= {
	"database" : {
		"description" : (
			"Work with Student Database."
			"Use this student records"
			"student counts, enrolled learners"
			"and database information"
			),
		"function" : database_tool,
		"parameters" : {
			"type" : "OBJECT",
			"properties": {
				"query": {
					"type":"STRING",
					"description":(
						"The student related information to search from student database"
						),
					},
				},
				"required":["query"],
			},
		},

	"pdf" :{
		"description" : (
			"Search PDF documents for information"
			"about AI, Machine Learning, NLP, transformers"
			"embeddings, RAG, and Related topics."
			),
		"function": pdf_tool,
		"parameters" : {
			"type" : "OBJECT",
			"properties" : {
				"query" : {
					"type":"STRING",
					"description":("The topic to search inside PDF documents"
						),
					},
				},
				"required":["query"],
			},
		},

	"web" : {
		"description" : (
			"Search web for current or up to date"
			"information that is not available in the"
			"local database or PDF documents."
			),
		"function" : web_search_tool,
		"parameters" : {
			"type": "OBJECT",
			"properties": {
				"query": {
					"type":"STRING",
					"description": (
						"The search query to use on the web"
						),
					},
				},
				"required":["query"],
			},
		},
	}

