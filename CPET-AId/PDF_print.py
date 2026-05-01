

def repport(filename, title=None, barchart = None, filepath_for_png = None, R_validation=False):
    """Function to generate PDF, 1.input: name of the file, 2.input the title,
      3.input data for the barchart, 4.input data for the filepath for .png, 5.input is the R-value"""
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4
    from reportlab.graphics import renderPDF
    from reportlab.lib import colors
    from reportlab.graphics.shapes import Drawing
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.pdfbase import pdfmetrics


    pdfmetrics.registerFont(TTFont('Arial','C:/Windows/Fonts/arial.ttf'))
    
    pdfmetrics.registerFont(TTFont('Arial-Bold','C:/Windows/Fonts/arialbd.ttf'))

    c = canvas.Canvas(filename) # opdatere så den stemmer overens med GUI fra Main

    if title is None:
        title=filename
        
    Max_width, Max_hight = A4 #dette vil svare til øverst højre hjørne af PDF'en, hvor 0,0 er nederst venstre hjørne
    margin_x = Max_width*0.1
    margin_y = Max_hight*0.1
    x = margin_x
    y = Max_hight - margin_y

    c.setFillColor(colors.HexColor("#48474e"))
    c.drawString(225,810,"CPET AId kan tage fejl")
    c.drawString(225,790,"Nøjagtighed: X%")
    
    
    c.setFillColor("black")
    c.setTitle(title)
    c.setFont('Arial',26) #font for title 
    c.drawString(x,y,title)
    

    c.setStrokeColor(colors.HexColor("#211a52"))
    c.setLineWidth(2)
    c.line(x, y - 12, Max_width - margin_x, y - 12)

    if R_validation is not True:
        R_text = "Maksimal ydeevne muligvis ikke opnået: R < 1,1"
        x = 200
        y_text = y - 30
        padding_x = 4
        padding_y = 2
        text_width = c.stringWidth(R_text, "Arial-Bold", 10)
        c.setFillColor(colors.red)
        c.rect(
            x,
            y_text - padding_y,
            text_width + 2 * padding_x,
            10 + 4,
            stroke=0,
            fill=1
        )
        c.setFillColor(colors.black)
        c.setFont("Arial-Bold", 10)
        c.drawString(
            x + padding_x,
            y_text,
            R_text)

    drawing = Drawing(350, 200)
    drawing.add(barchart)
    renderPDF.draw(drawing,c,100,525) #placering af barchart
    
    c.drawImage(
        filepath_for_png,
        50,
        50,
        height=500,
        width=500,
        preserveAspectRatio=True
    )
    c.setFontSize(7)
    c.setFillColor(colors.HexColor("#48474e"))
    c.drawString(100,margin_y+10,"De ovennævnte parametre er vægtet på baggrund af deres similaritet med tilsvarende patienter med de fire indikationer,")
    c.drawString(100,margin_y,"og relaterer sig dermed ikke til de fysiologiske normalområder.")

    c.save()


def PDF_error(filepath):
    from reportlab.pdfgen import canvas
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4

    Max_width, Max_hight = A4
    margin_x = Max_width*0.1
    margin_y = Max_hight*0.1
    x = margin_x
    y = Max_hight - margin_y

    c = canvas.Canvas(filepath)
    c.setFillColor(colors.HexColor("#48474e"))
    c.drawString(225,810,"CPET AId kan tage fejl")
    c.drawString(225,790,"Nøjagtighed: X%")

    title="CPET AId error"
    c.setFillColor("black")
    c.setTitle(title)
    c.setFont("Arial",26) #font for title 
    c.drawString(x,y,title)
    c.setStrokeColor(colors.HexColor("#211a52"))
    c.setLineWidth(2)
    c.line(x, y - 12, Max_width - margin_x, y - 12)

    error_messagge = c.beginText()
    error_messagge.setTextOrigin(margin_x+75,475)
    error_messagge.setFont("Arial-Bold",15)
    error_messagge.textLines("CPET AId kunne ikke udregne en sandsynlighed,\n grundt manglende værdier.")
    
    c.drawText(error_messagge)
    c.save()


