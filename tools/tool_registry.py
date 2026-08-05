

from tools.database_tool import database_tool
from tools.pdf_tool import pdf_tool


TOOLS= {
	"database" : {
		"description" : "Work with Student Database.",
		"function" : database_tool,
		},

	"pdf" :{
		"description" : "Search PDF documents.",
		"function": pdf_tool,
		},
	}
