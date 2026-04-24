from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

width, height = A4

def draw_coordinate_grid(c, step=50):
    c.setFont("Helvetica", 6)
    c.setStrokeColor(colors.lightgrey)
    c.setFillColor(colors.grey)

    # Vertikale linjer
    x = 0
    while x <= width:
        c.line(x, 0, x, height)
        c.drawString(x + 2, 5, str(int(x)))
        x += step

    # Horisontale linjer
    y = 0
    while y <= height:
        c.line(0, y, width, y)
        c.drawString(2, y + 2, str(int(y)))
        y += step

    # Marker centrum
    c.setStrokeColor(colors.red)
    c.line(width / 2, 0, width / 2, height)
    c.line(0, height / 2, width, height / 2)

    c.setFillColor(colors.red)
    c.drawString(width / 2 + 5, height / 2 + 5, "CENTER")


def make_grid_pdf(filename="A4_koordinat_grid.pdf"):
    c = canvas.Canvas(filename, pagesize=A4)

    draw_coordinate_grid(c, step=50)

    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(colors.black)
    c.drawString(50, height - 40, "A4 koordinat-guide")

    c.save()


make_grid_pdf()