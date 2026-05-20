import Visualisering



#Test af modulet



data1 = [("Kardielt", 82.5),("Pulmonalt", 1.1),("Muskulært", 16.0),("Rask", 0.4)]
barchart = Visualisering.Barchart(data1)

data2 = [("Kardielt", 12.5),("Pulmonalt", 105.1),("Muskulært", -5.0),("Rask", 0.4)]
barchart2 = Visualisering.Barchart(data2)

data3 = [("Kardielt", 0.5),("Pulmonalt", 0.1),("Muskulært", 0.01),("Rask", 95.4)]
barchart3 = Visualisering.Barchart(data3)

data4 = [("Kardielt", 40.0),("Pulmonalt", 20.5),("Muskulært", 40.0),("Rask", 20.5)]
barchart4 = Visualisering.Barchart(data4)




from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.graphics import renderPDF
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.styles import getSampleStyleSheet

styles = getSampleStyleSheet()

pdfmetrics.registerFont(TTFont('Arial','C:/Windows/Fonts/arial.ttf'))    
pdfmetrics.registerFont(TTFont('Arial-Bold','C:/Windows/Fonts/arialbd.ttf'))

c = canvas.Canvas("Modultest Barchart.pdf") # opdatere så den stemmer overens med GUI fra Main
    
Max_width, Max_hight = A4 #dette vil svare til øverst højre hjørne af PDF'en, hvor 0,0 er nederst venstre hjørne
margin_x = Max_width*0.1
margin_y = Max_hight*0.1
x = margin_x
y = Max_hight - margin_y


c.setFillColor("black")
c.setTitle("Modultest Barchart.pdf")
c.setFont('Arial',26) #font for title 
c.drawString(x,y,"Modultest Barchart")


c.setFont('Arial',12) #font for title 
c.drawString(x,y-50,"Søjlediagram 1")

drawing = Drawing(400, 200)
drawing.add(barchart)
x_centered = (Max_width-400)/2
renderPDF.draw(drawing,c,x_centered,500) #placering af barchart

inputstring = "Input: "+str(data1)
c.setFont('Arial',12) #font for title 
c.drawString(x_centered,465,inputstring)


typestring = "Søjlediagram 1 type: " + str(type(barchart))
c.drawString(x_centered,445,typestring)

parameterstring = "Højde: " + str(barchart.height) + ", Bredde: " + str(barchart.width) + ", Skriftstørrelse: " + str(barchart.barLabels.fontSize) + ", Font: " + str(barchart.valueAxis.labels.fontName) + " og " + str(barchart.barLabels.fontName)
c.drawString(x_centered,425,parameterstring)


c.setFont('Arial',12) #font for title 
c.drawString(x,372,"Søjlediagram 2")

drawing = Drawing(400, 200)
drawing.add(barchart2)
x_centered = (Max_width-400)/2
renderPDF.draw(drawing,c,x_centered,165) #placering af barchart

inputstring = "Input: "+str(data2)
c.setFont('Arial',12) #font for title 
c.drawString(x_centered,120,inputstring)

typestring = "Søjlediagram 2 type: " + str(type(barchart2))
c.drawString(x_centered,100,typestring)

parameterstring = "Højde: " + str(barchart2.height) + ", Bredde: " + str(barchart2.width) + ", Skriftstørrelse: " + str(barchart2.barLabels.fontSize) + ", Font: " + str(barchart2.valueAxis.labels.fontName) + " og " + str(barchart2.barLabels.fontName)
c.drawString(x_centered,80,parameterstring)



# Ny side
c.showPage()



c.setFont('Arial',12) #font for title 
c.drawString(x,y-50,"Søjlediagram 3")

drawing = Drawing(400, 200)
drawing.add(barchart3)
x_centered = (Max_width-400)/2
renderPDF.draw(drawing,c,x_centered,500) #placering af barchart

inputstring = "Input: "+str(data3)
c.setFont('Arial',12) #font for title 
c.drawString(x_centered,465,inputstring)


typestring = "Søjlediagram 3 type: " + str(type(barchart3))
c.drawString(x_centered,445,typestring)

parameterstring = "Højde: " + str(barchart3.height) + ", Bredde: " + str(barchart3.width) + ", Skriftstørrelse: " + str(barchart3.barLabels.fontSize) + ", Font: " + str(barchart3.valueAxis.labels.fontName) + " og " + str(barchart3.barLabels.fontName)
c.drawString(x_centered,425,parameterstring)



c.setFont('Arial',12) #font for title 
c.drawString(x,372,"Søjlediagram 4")

drawing = Drawing(400, 200)
drawing.add(barchart4)
x_centered = (Max_width-400)/2
renderPDF.draw(drawing,c,x_centered,165) #placering af barchart

inputstring = "Input: "+str(data4)
c.setFont('Arial',12) #font for title 
c.drawString(x_centered,130,inputstring)


typestring = "Søjlediagram 4 type: " + str(type(barchart4))
c.drawString(x_centered,100,typestring)

parameterstring = "Højde: " + str(barchart4.height) + ", Bredde: " + str(barchart4.width) + ", Skriftstørrelse: " + str(barchart4.barLabels.fontSize) + ", Font: " + str(barchart4.valueAxis.labels.fontName) + " og " + str(barchart4.barLabels.fontName)
c.drawString(x_centered,80,parameterstring)


c.save()
