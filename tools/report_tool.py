from pathlib import Path
from fpdf import FPDF


REPORTS_DIR = Path("reports")

def generate_report(content:str) -> str:
	"""
	Generate a PDF report from the supplied content.


	The report is saved inside the project's reports directory.
	"""
	if not content.strip():
		return "Error: Report content is empty"

	try:

		REPORTS_DIR.mkdir(exist_ok=True)

		report_path = REPORTS_DIR/"ai_generated_report.pdf"
		pdf = FPDF()
		pdf.add_page()
		pdf.set_font(
			"Arial",
			size=12,
			)
		pdf.multi_cell(
			0,
			12,
			content,
			)
		pdf.output(
			str(report_path)
			)
		return f"Report created successfully: {report_path}"

	except Exception as error:

		return f"Error while generating report: \n{error}"


