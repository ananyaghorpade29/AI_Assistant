

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
		},

	"pdf" :{
		"description" : (
			"Search PDF documents for information"
			"about AI, Machine Learning, NLP, transformers"
			"embeddings, RAG, and Related topics."
			),
		"function": pdf_tool,
		},

	"web" : {
		"description" : (
			"Search web for current or up to date"
			"information that is not available in the"
			"local database or PDF documents."
			),
		"function" : web_search_tool,
		},
	}
