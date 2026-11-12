from docx import Document


def save_report_to_word(filename: str, text_content: str):
    doc = Document()
    doc.add_heading('Отчет о расчете материалов', 0)
    lines = text_content.strip().split('\n')

    for line in lines:
        if line.strip():
            doc.add_paragraph(line)
    doc.save(filename)