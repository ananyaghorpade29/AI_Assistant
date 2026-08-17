
"""
Configuration settings for the AI Assistant project.
"""
import os
from pathlib import Path

GEMINI_MODEL = "gemini-3.6-flash"
PROJECT_ROOT = Path(__file__).parent

def get_gemini_api_key():
#get gemini key
	api_key = os.getenv("GEMINI_API_KEY")

	if not api_key:
		raise ValueError(
			"GEMINI_API_KEY environment variable is not set"
			)
	return api_key

#DB
DATABASE_DIR = PROJECT_ROOT/"database"
DATABASE_PATH = DATABASE_DIR/"students.db"

#DOCS
DOCUMENTS_DIR = PROJECT_ROOT/"documents"

#PDF
PDF_FILES = [
	DOCUMENTS_DIR /"nlp_o.pdf",
	DOCUMENTS_DIR /"aiengineering.pdf",
	DOCUMENTS_DIR /"buildingML.pdf",
	DOCUMENTS_DIR /"nlpwtransformers.pdf",
	]


#REPORTS
REPORTS_DIR = PROJECT_ROOT/"reports"

#VEC STORE
VECTORSTORE_DIR = PROJECT_ROOT/"vectorstore"
FAISS_INDEX_DIR = VECTORSTORE_DIR/"faiss_index"
INDEX_PATH = FAISS_INDEX_DIR/"index.faiss"

for directory in (
	DATABASE_DIR,
	DOCUMENTS_DIR,
	REPORTS_DIR,
	VECTORSTORE_DIR,
	FAISS_INDEX_DIR,
):
	directory.mkdir(parents=True, exist_ok=True)

#parents=True creates any missing parent directories.
#exist_ok=True prevents an error if the directory already exists.

