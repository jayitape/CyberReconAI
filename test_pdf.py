from modules.pdf_generator import generate_pdf_report


pdf = generate_pdf_report(
    "reports/google_com_report.html",
    "reports/google_com_report.pdf",
)


print(pdf)