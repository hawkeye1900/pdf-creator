from fpdf import FPDF
import pandas as pd


df = pd.read_csv("topics.csv")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=False)
line_height = 20
a4_height = 297

# Master page of each category
for index, row in df.iterrows():
    pdf.add_page()

    # Set the header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row['Topic'], align="L", ln=1, border=0)
    pdf.line(10, 21, 200, 21)  # (x, y, x, y)

    for i in range(21, a4_height, line_height):
        pdf.line(10, i, 200, i)

    # Set the footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row['Topic'], align="R")

    # additional pages for each category
    for i in range(1, row["Pages"]):
        pdf.add_page()
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row['Topic'], align="R")

        for j in range(21, a4_height, line_height):
            pdf.line(10, j, 200, j)


pdf.output("output.pdf")