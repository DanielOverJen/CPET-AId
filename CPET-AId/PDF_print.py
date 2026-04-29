from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.graphics.shapes import Drawing
from reportlab.graphics import renderPDF
from Visualisering import Barchart
# from reportlab.lib import colors


CPET_data = {
    "Kardiel":45,
    "Pulmonal":45,
    "Muskulært": 27,
    "Rask":5
    }
table_data = [
    ["Fysiologisk system","Sandsynlighed [%]"],
    ["Kardiel", CPET_data["Kardiel"]],
    ["Pulmonal", CPET_data["Pulmonal"]],
    ["Muskulært", CPET_data["Muskulært"]],
    ["Rask", CPET_data["Rask"]]
    ]

text = [("Dette er en længere tekst som automatisk bliver wrapped inde i boksen." \
" Det er meget nemmere end textobject." \
"Og dette er en ny linje",50 ,parametre ,1),("tekst2",45, parametre,0),("tekst3",40,parametre,0),("tekst4",35,parametre,0)] 


def PDF_print(filename, title=None, barchart = None, text = None):
    """Function to generate PDF, 1.input: name of the file, 2.input the title,
      3.input data for the table, 4.input data for the barchart"""
    # from reportlab.graphics.shapes import Line
    from reportlab.lib import colors
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.platypus import Paragraph
    from reportlab.graphics.shapes import Drawing

    Max_width, Max_hight = A4 #dette vil svare til øverst højre hjørne af PDF'en, hvor 0,0 er nederst venstre hjørne
    c = canvas.Canvas(filename +".pdf")

    if title is None:
        title=filename
        
    margin_x = Max_width*0.1
    margin_y = Max_hight*0.1
    x = margin_x
    y = Max_hight - margin_y

    c.setTitle(title)
    c.setFont("Times-Roman",26)
    c.drawString(x,y,title)
    
    c.setStrokeColor(colors.HexColor("#211a52"))
    c.setLineWidth(2)
    c.line(x, y - 12, Max_width - margin_x, y - 12)

    highest_proba = [t[3] for t in text]
    max_index = highest_proba.index(1)
    
    boxes = [
            (50,300),
            (50,50),
            (350,300),
            (350,50)
            ]

    for i, (x, y) in enumerate(boxes):
        if i == max_index:
        c.setFillColor(colors.HexColor("#211A52"))
    else:
        c.setFillColor(colors.lightgrey)
    
    c.setStrokeColor(colors.black)
    
    c.rect(50,300,200,200,stroke=1,fill=1)
    c.rect(50,50,200,200,stroke=1,fill=1)
    c.rect(350,300,200,200,stroke=1,fill=1)
    c.rect(350,50,200,200,stroke=1,fill=1)

    styles = getSampleStyleSheet()
    style = styles["Normal"]
    
    p = Paragraph(text[0], style)

    p.wrapOn(c,250-2*10,120-2*10)
    p.drawOn(c, 50+10,250+10)
    #alle elementer om rect kan godt laves om til en funktion

    drawing = Drawing(400, 220)
    drawing.add(barchart)
    renderPDF.draw(drawing,c,x+50,y-200)
    
    c.save()

barchart = Barchart(CPET_data)#kun til debugging 

PDF_print("CPET AId","CPET AId Resultat",barchart,text_1)#kun til debugging