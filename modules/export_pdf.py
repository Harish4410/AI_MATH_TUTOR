from reportlab.pdfgen import canvas

def export_solution(equation, solution, explanation):

    file = "outputs/solution.pdf"

    c = canvas.Canvas(file)

    c.drawString(50,800,"AI Math Tutor Solution")

    c.drawString(50,760,f"Equation: {equation}")

    c.drawString(50,720,f"Answer: {solution}")

    text = c.beginText(50,680)

    for line in explanation.split("\n"):
        text.textLine(line)

    c.drawText(text)

    c.save()

    return file