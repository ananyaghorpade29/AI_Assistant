# read and extract text from PDF
"""
PDF Reader Tool for the AI Assistant.

This module extracts text from PDF files.
"""

from pathlib import Path

from pypdf import PdfReader
from config import PDF_FILES

"""
Read a PDF file and return all extracted text.
Args:
pdf_path: Path to the PDF file.
Returns:
A single string containing all extracted text.
"""

def read_pdf(pdf_paths:list[ Path]) -> str:

	text = ""
	for pdf_path in pdf_paths:

		if not pdf_path.exists():
			return f"Error: PDF not found at {pdf_path}"
			continue

		try:
			reader = PdfReader(pdf_path)
			for page_number, page in enumerate(reader.pages, start=1):
				print(f"Reading {pdf_path.name} - page {page_number}...")
				page_text = page.extract_text()
				if page_text:
					text += page_text + "\n"
		except Exception as error:
			print(f"Failed to read PDF {pdf_path}: {error}")
	return text
