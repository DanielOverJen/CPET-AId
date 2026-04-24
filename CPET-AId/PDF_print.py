from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import Table
from reportlab.graphics.shapes import Drawing
from reportlab.graphics import renderPDF


CPET_data = {
    "Kardial":45,
    "Pulmonal":45,
    "Muskulært": 27,
    "Rask":5
    }
table_data = [
    ["Fysiologisk system","Sandsynlighed [%]"],
    ["Kardial", CPET_data["Kardial"]],
    ["Pulmonal", CPET_data["Pulmonal"]],
    ["Muskulært", CPET_data["Muskulært"]],
    ["Rask", CPET_data["Rask"]]
    ]

def Barchart(data):
    """Skal modtage et datasæt bestående af tuple på formen ["navn":tal]"""
    from reportlab.lib import colors
    from reportlab.graphics.charts.barcharts import VerticalBarChart

    bar_chart = VerticalBarChart()
    bar_chart.x = 50
    bar_chart.y = 50
    bar_chart.width = 300
    bar_chart.height = 125

    values = [
        data["Kardial"],
        data["Pulmonal"],
        data["Muskulært"],
        data["Rask"]
    ]

    bar_chart.data = [values]

    max_value = max(values)

    for i, v in enumerate(values):
        if v == max_value:
            bar_chart.bars[(0,i)].fillColor = colors.HexColor("#211a52")
        else:
            bar_chart.bars[(0,i)].fillColor = colors.HexColor("#D3D6D7")
    
    bar_chart.barLabels.nudge = 10
    bar_chart.barLabels.fontSize = 12
    bar_chart.barLabelFormat = '%.1f%%'
    bar_chart.barLabels.fillColor = colors.black

    bar_chart.categoryAxis.categoryNames = [
        'Kardiel:',
        'Pulmonal:',
        'Muskulært:',
        'Rask:'
    ]
    bar_chart.valueAxis.valueMin = 0
    bar_chart.valueAxis.valueMax = 100
    bar_chart.valueAxis.valueStep = 10
    bar_chart.valueAxis.visibleGrid = True
    bar_chart.valueAxis.valueStep = 20
    bar_chart.valueAxis.gridStrokeColor = colors.HexColor("#dddddd")
    bar_chart.valueAxis.gridStrokeWidth = 0.5
    
    return bar_chart

def Draw_table(data):
    from reportlab.lib import colors
    table = Table(
    data,
    style=[
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('FONTNAME', (0, 0), (-1, 0), 'Times-Bold'),
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey)
    ]
    )
    return table

# def Draw_boxs()
    

def PDF_form(filename, title=None, table_data=None, barchart_data = None):
    """Function to generate PDF, 1.input: name of the file, 2.input the title,
      3.input data for the table, 4.input data for the barchart"""
    from reportlab.graphics.shapes import Line
    from reportlab.lib import colors
    Max_width, Max_hight = A4 #dette vil svare til øverst højre hjørne af PDF'en, hvor 0,0 er nederst venstre hjørne
    c = canvas.Canvas(filename +".pdf")
 
    if title is None:
        title=filename
        
    margin_x = Max_width*0.1
    margin_y = Max_hight*0.1
    x = margin_x
    y = Max_hight - margin_y

    c.setTitle(title)
    c.setFont("Times-Roman",14)
    c.drawString(x,y,title)
    line = Line(50, 750, 550, 750)
    line.strokeColor = colors.HexColor('#211a52')
    line.strokeWidth = 10


    # table = Draw_table(table_data)
    # table_width, table_hight =table.wrap(0,0)
    # table.drawOn(c,x,y-80-table_hight)
    
    drawing = Drawing(400, 220)
    drawing.add(Barchart(barchart_data))
    renderPDF.draw(drawing,c,x+50,y-200)

    
    c.save()

PDF_form("CPET AId","CPET AId Resultat", table_data, CPET_data)#kun til debugging