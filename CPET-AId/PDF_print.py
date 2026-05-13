def report(filename, R_valid=False, title=None, barchart = None, filepath_for_png = None):
    """Function to generate PDF, 1.input: name of the file, 2.input the title,
      3.input data for the barchart, 4.input data for the filepath for .png, 5.input is the R-value"""
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4
    from reportlab.graphics import renderPDF
    from reportlab.lib import colors
    from reportlab.graphics.shapes import Drawing
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.pdfbase import pdfmetrics
    from reportlab.platypus import Paragraph
    from reportlab.lib.styles import getSampleStyleSheet

    styles = getSampleStyleSheet()

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
    c.drawString(225,790,"Nøjagtighed: 75%")
    
    
    c.setFillColor("black")
    c.setTitle(title)
    c.setFont('Arial',26) #font for title 
    c.drawString(x,y,title)
    

    c.setStrokeColor(colors.HexColor("#211a52"))
    c.setLineWidth(2)
    c.line(x-10, y - 12, Max_width - margin_x + 10, y - 12)

    if R_valid is not True:
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

    drawing = Drawing(400, 200)
    drawing.add(barchart)
    x_centered = (Max_width-400)/2
    renderPDF.draw(drawing,c,x_centered,505) #placering af barchart
    
    c.drawImage(
        filepath_for_png,
        50,
        50,
        height=500,
        width=500,
        preserveAspectRatio=True,
    )

    text = """Et søjlediagram hvor sandsynlighederne for det pågældende fysiologiske system er det begrænsende for patienten."""
    
    p = Paragraph(text, styles["Normal"])
    p.wrap(400,200)
    p.drawOn(c,100,margin_y+375)

    text2 = """Et beslutningsplot, der viser udviklingen af CPET AIds beslutning i takt med hver parametre har sin indvirkning.
      Disse parametre bør sammenholdes med det tilhørende 9-panel plot. 
     De ovennævnte parametre er vægtet på baggrund af deres similaritet med tilsvarende patienter med de fire indikationer,
       og relaterer sig dermed ikke til de fysiologiske normalområder."""
    
    p2 = Paragraph(text2, styles["Normal"])
    p2.wrap(500, 200)
    p2.drawOn(c, 50, margin_y+20) #tegner figurtekst til beslutningsplot. Er blevet rykket lidt ned fra tidligere layout

    c.save()

def PDF_error(filepath):
    from reportlab.pdfgen import canvas
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    
    pdfmetrics.registerFont(TTFont('Arial','C:/Windows/Fonts/arial.ttf'))    
    pdfmetrics.registerFont(TTFont('Arial-Bold','C:/Windows/Fonts/arialbd.ttf'))

    Max_width, Max_hight = A4
    margin_x = Max_width*0.1
    margin_y = Max_hight*0.1
    x = margin_x
    y = Max_hight - margin_y

    c = canvas.Canvas(filepath)
    # c.setFillColor(colors.HexColor("#48474e"))
    # c.drawString(225,810,"CPET AId kan tage fejl")
    # c.drawString(225,790,"Nøjagtighed: 75%")

    title="CPET AId resultater"
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
    error_messagge.textLines("CPET AId kunne ikke klassificere patienten,\n grundet manglende værdier.")
    
    c.drawText(error_messagge)
    c.save()


