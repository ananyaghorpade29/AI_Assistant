"""
PDF Reader Tool for the AI Assistant.

This module extracts text from PDF files.
"""

from pathlib import Path

from pypdf import PdfReader

"""
Read a PDF file and return all extracted text.
Args:
pdf_path: Path to the PDF file.
Returns:
A single string containing all extracted text.
"""

def read_pdf(pdf_path: Path) -> str:

	if not pdf.path.exists():
		return "Error: PDF not found at {pdf_path}"

	try:
		reader = PdfReader(pdf_path)
		text =""
		for page in reader.pages:
			page_text = page.extract_text()

			if page_text:
				text += page_text +"\n"
		return text

	except Exception as error:
		return f"Failed to read PDF: {error}"
