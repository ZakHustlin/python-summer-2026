from fpdf import FPDF


name = input("What is your name: ")

pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", style="B", size=16)
pdf.cell(210, 10, "CS50 Shirtificate",  align="C")
pdf.image("shirtificate.png", 30, 50, w=150)
pdf.set_text_color(255, 255, 255)
pdf.set_xy(30, 120)  # adjust y until it sits on the shirt
pdf.cell(150, 2, f"{name}", align="C")
pdf.output("shirtificate.pdf")

