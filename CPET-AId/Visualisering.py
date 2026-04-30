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
        data["Kardiel"],
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
    bar_chart.barLabels.fontName = "Helvetica-Bold"
    bar_chart.barLabels.fillColor = colors.black

    bar_chart.categoryAxis.labels.fontName = "Helvetica"
    bar_chart.categoryAxis.categoryNames = [
        'Kardiel:',
        'Pulmonal:',
        'Muskulært:',
        'Rask:'
    ]
    bar_chart.valueAxis.labels.fontName = "Helvetica"
    bar_chart.valueAxis.valueMin = 0
    bar_chart.valueAxis.valueMax = 100
    bar_chart.valueAxis.valueStep = 10
    bar_chart.valueAxis.visibleGrid = True
    bar_chart.valueAxis.valueStep = 20
    bar_chart.valueAxis.gridStrokeColor = colors.HexColor("#dddddd")
    bar_chart.valueAxis.gridStrokeWidth = 0.5
    
    bar_chart.x=0
    bar_chart.y=0
    bar_chart.width=350
    bar_chart.height=200
    
    return bar_chart

def Draw_table(data):
    from reportlab.lib import colors
    from reportlab.platypus import Table
    table = Table(
    data,
    style=[
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('FONTNAME', (0, 0), (-1, 0), 'Times-Bold'),
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey)
    ]
    )
    return table