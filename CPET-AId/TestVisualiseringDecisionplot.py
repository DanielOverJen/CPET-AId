import Visualisering





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




from reportlab.lib.utils import ImageReader

#########################################Test af Decisionplot############################3

c = canvas.Canvas("Modultest Decisionplot.pdf") # opdatere så den stemmer overens med GUI fra Main
    
Max_width, Max_hight = A4 #dette vil svare til øverst højre hjørne af PDF'en, hvor 0,0 er nederst venstre hjørne
margin_x = Max_width*0.1
margin_y = Max_hight*0.1
x = margin_x
y = Max_hight - margin_y
x_centered = (Max_width-400)/2


c.setFillColor("black")
c.setTitle("Modultest Decisionplot.pdf")
c.setFont('Arial',26) #font for title 
c.drawString(x,y+5,"Modultest Decisionplot")



# Patient 5;
shap_values1 = [[
  [ 0.78798, -0.31402,  0.04011, -0.97073 ],
  [ 0.03237,  -0.46186,  0.57475,  -0.16537],
  [-0.04824, -0.10042,  0.01773,  0.12267],
  [-0.24123,  0.26461, -0.52461,  -0.79990 ],
  [ 0.47733, -0.83672,   0.35610, -1.01448 ],
  [ 0.66456,  -0.52069,  -0.23113, -1.29916 ]
  ]]


import numpy as np

# Fra (1,6,4) -> (4,1,6)
shap_values1 = np.transpose(shap_values1, (2, 0, 1))

# Konverter til liste af arrays
shap_values1 = [arr for arr in shap_values1]
base_values1 = [0.09750, -0.53867, -0.10174, 0.53747]




Proba1 = [("Kardielt", 82.5),("Pulmonalt", 1.1),("Muskulært", 16.0),("Rask", 0.4)]

pre_processed_data = [ 0.81416587, 48.3,         0.50944644,  3.03949345,  0.67707986,  0.07846154]


 # Array med ML-modellens feature-navne og de tilhørende værdier
feature_names_values1 = [
            f"Afvigelse fra forventet Peak VO2 \n = {round(pre_processed_data[0]*100,1)} %",
            f"Peak minutventilation (VE) \n = {round(pre_processed_data[1],1)} L/min",
            f"Hældningen af O2-pulsen i testens \n første halvdel = {round(pre_processed_data[2],3)}",
            f"Spredningen af VE/VCO2 \n = {round(pre_processed_data[3],2)}",
            f"Afvigelse fra forventet Peak O2-puls \n = {round(pre_processed_data[4]*100,1)} %",
            f"Hældningen af VO2 i testens \n første halvdel = {round(pre_processed_data[5],3)}"
        ]

pre_processed_data[0] = round(pre_processed_data[0]*100,1)
pre_processed_data[1] = round(pre_processed_data[1],1)
pre_processed_data[2] = round(pre_processed_data[2],3)
pre_processed_data[3] = round(pre_processed_data[3],2)
pre_processed_data[4] = round(pre_processed_data[4]*100,1)
pre_processed_data[5] = round(pre_processed_data[5],3)


Visualisering.decisionplot(Proba1, feature_names_values1, shap_values1, base_values1)

image1 = ImageReader("CPET-AId\\CPET-AId\\decisionplot.png")


c.setFont('Arial',12) #font for title 
c.drawString(x,y-20,"Beslutningsplot 1")

Imageheight = 280
Imagewidth = 500

c.drawImage(
    image1,
    50,
    450,
    height=Imageheight,
    width=Imagewidth,
)

inputstring = "SHAP værdier input: "
c.setFont('Arial',12) #font for title 
c.drawString(x_centered,430,inputstring)
c.drawString(x_centered,415,str(shap_values1[0]))
c.drawString(x_centered,400,str(shap_values1[1]))
c.drawString(x_centered,385,str(shap_values1[2]))
c.drawString(x_centered,370,str(shap_values1[3]))


baseinputstring = "Basis værdier input: "
c.setFont('Arial',12) #font for title 
c.drawString(x_centered,330,baseinputstring)
c.drawString(x_centered, 315, str(base_values1))


featureString = "Feature værdier input: "
c.drawString(x_centered,275,featureString)
c.drawString(x_centered,260, str(pre_processed_data))

mlmodelstring = "Ml model sandsynligheder input: "
c.drawString(x_centered,220,mlmodelstring)
c.drawString(x_centered,205, str(Proba1))



typestring = "Beslutningsplot 1 type: " 
c.drawString(x_centered,165,typestring)
c.drawString(x_centered,150, str(type(image1)))


parameterstring = "Højde: " + str(Imageheight) + ", Bredde: " + str(Imagewidth) + ", Skriftstørrelse: " + str(11) + ", Font: 'Arial'" 
c.drawString(x_centered,110,parameterstring)

# Ny side
c.showPage()



# Patient 5;
shap_values1 = [[
  [ 0.78798, -0.31402,  0.04011, -0.97073 ],
  [ 0.03237,  -0.46186,  0.57475,  -0.16537],
  [-0.04824, -0.10042,  0.01773,  0.12267],
  [-0.24123,  0.26461, -0.52461,  -0.79990 ],
  [ 0.47733, -0.83672,   0.35610, -1.01448 ],
  [ 0.66456,  -0.52069,  -0.23113, -1.29916 ]
  ]]




import numpy as np

# Fra (1,6,4) -> (4,1,6)
shap_values1 = np.transpose(shap_values1, (2, 0, 1))

# Konverter til liste af arrays
shap_values1 = [arr for arr in shap_values1]
base_values1 = [0.0, 0.0, 1.000174, 0.0]




Proba1 = [("Kardielt", 82.5),("Pulmonalt", 1.1),("Muskulært", 16.0),("Rask", 0.4)]

pre_processed_data = [ 0.81416587, 48.3,         0.50944644,  3.03949345,  0.67707986,  0.07846154]


 # Array med ML-modellens feature-navne og de tilhørende værdier
feature_names_values1 = [
            f"Afvigelse fra forventet Peak VO2 \n = {round(pre_processed_data[0]*100,1)} %",
            f"Peak minutventilation (VE) \n = {round(pre_processed_data[1],1)} L/min",
            f"Hældningen af O2-pulsen i testens \n første halvdel = {round(pre_processed_data[2],3)}",
            f"Spredningen af VE/VCO2 \n = {round(pre_processed_data[3],2)}",
            f"Afvigelse fra forventet Peak O2-puls \n = {round(pre_processed_data[4]*100,1)} %",
            f"Hældningen af VO2 i testens \n første halvdel = {round(pre_processed_data[5],3)}"
        ]

pre_processed_data[0] = round(pre_processed_data[0]*100,1)
pre_processed_data[1] = round(pre_processed_data[1],1)
pre_processed_data[2] = round(pre_processed_data[2],3)
pre_processed_data[3] = round(pre_processed_data[3],2)
pre_processed_data[4] = round(pre_processed_data[4]*100,1)
pre_processed_data[5] = round(pre_processed_data[5],3)


Visualisering.decisionplot(Proba1, feature_names_values1, shap_values1, base_values1)

image1 = ImageReader("CPET-AId\\CPET-AId\\decisionplot.png")


c.setFont('Arial',12) #font for title 
c.drawString(x,y-20,"Beslutningsplot 2")

Imageheight = 280
Imagewidth = 500

c.drawImage(
    image1,
    50,
    450,
    height=Imageheight,
    width=Imagewidth,
)

inputstring = "SHAP værdier input: "
c.setFont('Arial',12) #font for title 
c.drawString(x_centered,430,inputstring)
c.drawString(x_centered,415,str(shap_values1[0]))
c.drawString(x_centered,400,str(shap_values1[1]))
c.drawString(x_centered,385,str(shap_values1[2]))
c.drawString(x_centered,370,str(shap_values1[3]))


baseinputstring = "Basis værdier input: "
c.setFont('Arial',12) #font for title 
c.drawString(x_centered,330,baseinputstring)
c.drawString(x_centered, 315, str(base_values1))


featureString = "Feature værdier input: "
c.drawString(x_centered,275,featureString)
c.drawString(x_centered,260, str(pre_processed_data))

mlmodelstring = "Ml model sandsynligheder input: "
c.drawString(x_centered,220,mlmodelstring)
c.drawString(x_centered,205, str(Proba1))



typestring = "Beslutningsplot 2 type: " 
c.drawString(x_centered,165,typestring)
c.drawString(x_centered,150, str(type(image1)))


parameterstring = "Højde: " + str(Imageheight) + ", Bredde: " + str(Imagewidth) + ", Skriftstørrelse: " + str(11) + ", Font: 'Arial'" 
c.drawString(x_centered,110,parameterstring)







# Ny side
c.showPage()



# Patient 5;
shap_values1 = [[
  [ 10.78798, -0.31402,  0.04011, -0.97073 ],
  [ 100.03237,  -0.46186,  0.57475,  -0.16537],
  [-40.04824, -0.10042,  0.01773,  0.12267],
  [-2.24123,  0.26461, -0.52461,  -0.79990 ],
  [ 0.47733, -0.83672,   0.35610, -1.01448 ],
  [ -50.66456,  -0.52069,  -0.23113, -1.29916 ]
  ]]




import numpy as np

# Fra (1,6,4) -> (4,1,6)
shap_values1 = np.transpose(shap_values1, (2, 0, 1))

# Konverter til liste af arrays
shap_values1 = [arr for arr in shap_values1]
base_values1 = [0.09750, -0.53867, -0.10174, 0.53747]





Proba1 = [("Kardielt", 8200.5),("Pulmonalt", 0.00001),("Muskulært", 16.0),("Rask", 0.4)]

pre_processed_data = [ 0.81416587, 48.3,         0.50944644,  3.03949345,  0.67707986,  0.07846154]


 # Array med ML-modellens feature-navne og de tilhørende værdier
feature_names_values1 = [
            f"Afvigelse fra forventet Peak VO2 \n = {round(pre_processed_data[0]*100,1)} %",
            f"Peak minutventilation (VE) \n = {round(pre_processed_data[1],1)} L/min",
            f"Hældningen af O2-pulsen i testens \n første halvdel = {round(pre_processed_data[2],3)}",
            f"Spredningen af VE/VCO2 \n = {round(pre_processed_data[3],2)}",
            f"Afvigelse fra forventet Peak O2-puls \n = {round(pre_processed_data[4]*100,1)} %",
            f"Hældningen af VO2 i testens \n første halvdel = {round(pre_processed_data[5],3)}"
        ]

pre_processed_data[0] = round(pre_processed_data[0]*100,1)
pre_processed_data[1] = round(pre_processed_data[1],1)
pre_processed_data[2] = round(pre_processed_data[2],3)
pre_processed_data[3] = round(pre_processed_data[3],2)
pre_processed_data[4] = round(pre_processed_data[4]*100,1)
pre_processed_data[5] = round(pre_processed_data[5],3)


Visualisering.decisionplot(Proba1, feature_names_values1, shap_values1, base_values1)

image1 = ImageReader("CPET-AId\\CPET-AId\\decisionplot.png")


c.setFont('Arial',12) #font for title 
c.drawString(x,y-20,"Beslutningsplot 3")

Imageheight = 280
Imagewidth = 500

c.drawImage(
    image1,
    50,
    450,
    height=Imageheight,
    width=Imagewidth,
)

inputstring = "SHAP værdier input: "
c.setFont('Arial',12) #font for title 
c.drawString(x_centered,430,inputstring)
c.drawString(x_centered,415,str(shap_values1[0]))
c.drawString(x_centered,400,str(shap_values1[1]))
c.drawString(x_centered,385,str(shap_values1[2]))
c.drawString(x_centered,370,str(shap_values1[3]))


baseinputstring = "Basis værdier input: "
c.setFont('Arial',12) #font for title 
c.drawString(x_centered,330,baseinputstring)
c.drawString(x_centered, 315, str(base_values1))


featureString = "Feature værdier input: "
c.drawString(x_centered,275,featureString)
c.drawString(x_centered,260, str(pre_processed_data))

mlmodelstring = "Ml model sandsynligheder input: "
c.drawString(x_centered,220,mlmodelstring)
c.drawString(x_centered,205, str(Proba1))



typestring = "Beslutningsplot 3 type: " 
c.drawString(x_centered,165,typestring)
c.drawString(x_centered,150, str(type(image1)))


parameterstring = "Højde: " + str(Imageheight) + ", Bredde: " + str(Imagewidth) + ", Skriftstørrelse: " + str(11) + ", Font: 'Arial'" 
c.drawString(x_centered,110,parameterstring)





# Ny side
c.showPage()



# Patient 5;
shap_values1 = [[
  [ 0.0, -0.31402,  0.04011, -0.97073 ],
  [ 0.0,  -0.46186,  0.57475,  -0.16537],
  [0.0, -0.10042,  0.01773,  0.12267],
  [0.0,  0.26461, -0.52461,  -0.79990 ],
  [ 0.0, -0.83672,   0.35610, -1.01448 ],
  [ -0.0,  -0.52069,  -0.23113, -1.29916 ]
  ]]




import numpy as np

# Fra (1,6,4) -> (4,1,6)
shap_values1 = np.transpose(shap_values1, (2, 0, 1))

# Konverter til liste af arrays
shap_values1 = [arr for arr in shap_values1]
base_values1 = [0.0, -0.0, -0.0, 0.0]
# base_values1 = [0.09750, -0.53867, -0.10174, 0.53747]




Proba1 = [("Kardielt", 8200.5),("Pulmonalt", 0.00001),("Muskulært", 16.0),("Rask", 0.4)]

pre_processed_data = [ 0.81416587, 48.3,         0.50944644,  3.03949345,  0.67707986,  0.07846154]


 # Array med ML-modellens feature-navne og de tilhørende værdier
feature_names_values1 = [
            f"Afvigelse fra forventet Peak VO2 \n = {round(pre_processed_data[0]*100,1)} %",
            f"Peak minutventilation (VE) \n = {round(pre_processed_data[1],1)} L/min",
            f"Hældningen af O2-pulsen i testens \n første halvdel = {round(pre_processed_data[2],3)}",
            f"Spredningen af VE/VCO2 \n = {round(pre_processed_data[3],2)}",
            f"Afvigelse fra forventet Peak O2-puls \n = {round(pre_processed_data[4]*100,1)} %",
            f"Hældningen af VO2 i testens \n første halvdel = {round(pre_processed_data[5],3)}"
        ]

pre_processed_data[0] = round(pre_processed_data[0]*100,1)
pre_processed_data[1] = round(pre_processed_data[1],1)
pre_processed_data[2] = round(pre_processed_data[2],3)
pre_processed_data[3] = round(pre_processed_data[3],2)
pre_processed_data[4] = round(pre_processed_data[4]*100,1)
pre_processed_data[5] = round(pre_processed_data[5],3)


Visualisering.decisionplot(Proba1, feature_names_values1, shap_values1, base_values1)

image1 = ImageReader("CPET-AId\\CPET-AId\\decisionplot.png")


c.setFont('Arial',12) #font for title 
c.drawString(x,y-20,"Beslutningsplot 4")

Imageheight = 280
Imagewidth = 500

c.drawImage(
    image1,
    50,
    450,
    height=Imageheight,
    width=Imagewidth,
)

inputstring = "SHAP værdier input: "
c.setFont('Arial',12) #font for title 
c.drawString(x_centered,430,inputstring)
c.drawString(x_centered,415,str(shap_values1[0]))
c.drawString(x_centered,400,str(shap_values1[1]))
c.drawString(x_centered,385,str(shap_values1[2]))
c.drawString(x_centered,370,str(shap_values1[3]))


baseinputstring = "Basis værdier input: "
c.setFont('Arial',12) #font for title 
c.drawString(x_centered,330,baseinputstring)
c.drawString(x_centered, 315, str(base_values1))


featureString = "Feature værdier input: "
c.drawString(x_centered,275,featureString)
c.drawString(x_centered,260, str(pre_processed_data))

mlmodelstring = "Ml model sandsynligheder input: "
c.drawString(x_centered,220,mlmodelstring)
c.drawString(x_centered,205, str(Proba1))



typestring = "Beslutningsplot 4 type: " 
c.drawString(x_centered,165,typestring)
c.drawString(x_centered,150, str(type(image1)))


parameterstring = "Højde: " + str(Imageheight) + ", Bredde: " + str(Imagewidth) + ", Skriftstørrelse: " + str(11) + ", Font: 'Arial'" 
c.drawString(x_centered,110,parameterstring)

c.save()
