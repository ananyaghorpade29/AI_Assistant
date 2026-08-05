

from tools.database_tool import database_tool
from tools.pdf_tool import pdf_tool
from tools.web_search import web_search_tool

TOOLS= {
	"database" : {
		"description" : "Work with Student Database.",
		"function" : database_tool,
		},

	"pdf" :{
		"description" : "Search PDF documents.",
		"function": pdf_tool,
		},

	"web" : {
		"description" : "Search web.",
		"function" : web_search_tool,
		},

	}
