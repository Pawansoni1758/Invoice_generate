from pathlib import Path
from fpdf import FPDF
import glob
import pandas as pd

filepaths = glob.glob("txt/*.txt")
pdf = FPDF(orientation="P", unit="mm", format="A4")
for filepath in filepaths:
    filename = Path(filepath).stem
    file_name = filename.split(".")[0]
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=15)
    pdf.cell(w=50, h=12, txt=f"{file_name.title()}", align="L", ln=1)

    with open(filepath)as file:
        content = file.read()
    pdf.set_font(family="Times", size=12)
    pdf.multi_cell(w=0, h=6, txt=content)

pdf.output("txt/output.pdf")

