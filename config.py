"""
Configuration settings for the AI Assistant project.
"""

from pathlib import Path

PROJECT_ROOT = Path(__file__).parent


#DB
DATABASE_DIR = PROJECT_ROOT/"database"
DATABASE_PATH = DATABASE_DIR/"students.db"

#DOCS
DOCUMENTS_DIR = PROJECT_ROOT/"documents"

#PDF
PDF_PATH = DOCUMENTS_DIR/"nlp_o.pdf"

#REPORTS
REPORTS_DIR = PROJECT_ROOT/"reports"

#VEC STORE
VECTORSTORE_DIR = PROJECT_ROOT/"vectorstore"
FAISS_INDEX_DIR = PROJECT_ROOT/"faiss_index"

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

