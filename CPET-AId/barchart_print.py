from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics import renderPDF
from reportlab.pdfgen import canvas

c = canvas.Canvas("Barchart" +".pdf")

drawing = Drawing(400, 220)

bar_chart = VerticalBarChart()
bar_chart.x = 50
bar_chart.y = 50
bar_chart.width = 300
bar_chart.height = 125

bar_chart.data = [
    [100, 120, 140, 120],
    [70, 60, 60, 50],
    [200, 200, 200, 340]
]

bar_chart.categoryAxis.categoryNames = ['Q1', 'Q2', 'Q3', 'Q4']
bar_chart.valueAxis.valueMin = 0
bar_chart.valueAxis.valueMax = 400
bar_chart.valueAxis.valueStep = 50

drawing.add(bar_chart)

renderPDF.draw(drawing, c, 100, 300)
c.save()