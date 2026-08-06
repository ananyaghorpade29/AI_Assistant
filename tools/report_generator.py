

from pathlib import Path
from fpdf  import FPDF
from datetime import datetime


REPORTS_DIR = Path("reports")
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

def generate_report(title:str, content:str) -> Path:
#Generate PDF report and return its file path
	REPORTS_DIR.mkdir(exist_ok =True)
	pdf = FPDF()
	pdf.add_page()
	pdf.set_font("Helvetica",size=14,)
	pdf.cell(
		w=0,
		h=10,
		text=title,
		new_x = "LMARGIN",
		new_y =  "NEXT",
		)
	pdf.set_font(
		"Helvetica",
		size=11,
		)
	pdf.multi_cell(
		w=0,
		h=7,
		text=(f"{content}\n\n Generated on: {timestamp}"),
		)
	filename = REPORTS_DIR/"report.pdf"
	pdf.output(filename)
	pdf.output(str(filename))
	return filename

path = generate_report("studentReport","ID: 1 | Name: Ananya\nID:2 | Name: Nikita",)
print(path)
