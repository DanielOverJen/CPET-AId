import shap
import matplotlib.pyplot as plt
from reportlab.lib import colors
from reportlab.graphics.charts.barcharts import VerticalBarChart
import numpy as np

def Barchart(data):
    """Skal modtage et datasæt bestående af tuple på formen ("navn",tal)"""

    bar_chart = VerticalBarChart()
    bar_chart.x = 0
    bar_chart.y = 0
    bar_chart.width = 400
    bar_chart.height = 200
    
    _ , values = zip(*data) #Deler input sandsynligheder op i 2 arrays
    
    bar_chart.data = [values]

    max_value = max(values)

    #Finder farver til søjlerne ud fra hvilken der er størst
    for i, v in enumerate(values):
        if v == max_value:
            bar_chart.bars[(0,i)].fillColor = colors.HexColor("#211a52")
        else:
            bar_chart.bars[(0,i)].fillColor = colors.HexColor("#D3D6D7")
    
    bar_chart.barLabels.nudge = 10
    bar_chart.barLabels.fontSize = 11
    bar_chart.barLabelFormat = '%.1f%%'
    bar_chart.barLabels.fontName = "Arial-Bold"
    bar_chart.barLabels.fillColor = colors.black

    bar_chart.categoryAxis.labels.fontName = "Arial"
    bar_chart.categoryAxis.categoryNames = [
        'Kardielt:',
        'Pulmonalt:',
        'Muskulært:',
        'Rask:'
    ]
    
    bar_chart.valueAxis.labels.fontName = "Arial"
    bar_chart.valueAxis.valueMin = 0
    bar_chart.valueAxis.valueMax = 100
    bar_chart.valueAxis.valueStep = 10
    bar_chart.valueAxis.visibleGrid = True
    bar_chart.valueAxis.gridStrokeColor = colors.HexColor("#dddddd")
    bar_chart.valueAxis.gridStrokeWidth = 0.5
    
    
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

def decisionplot(Class_proba, feature_names_values, shap_values, base_values):
    """Gemmer et png af et decisionplot med det højest sandsynlige fysiologisk system markeret"""
    name, proba = zip(*Class_proba) #Deler input sandsynligheder op i 2 arrays
    
    max_index = proba.index(max(proba))

    Cardiacpercent = str(proba[0]) 
    CardiacLabelname = "K: "+ name[0]+"("+Cardiacpercent+"%)"

    Pulmopercent = str(proba[1])
    PulmoLabelname = "P: "+ name[1]+" ("+Pulmopercent+"%)"
    
    Muscopercent = str(proba[2])
    MuscoLabelname = "M: "+ name[2]+"("+Muscopercent+"%)"
    
    Healthypercent = str(proba[3])
    HealthyLabelname = "R: "+ name[3]+"("+Healthypercent+"%)"
    

    classification_names = [CardiacLabelname, PulmoLabelname,MuscoLabelname,HealthyLabelname]

    shap.multioutput_decision_plot(
        base_values,
        shap_values,
        row_index=0,
        feature_names=feature_names_values,   # dine 6 features
        # features = PatientData,
        # highlight=[np.argmax(proba[row_index])],
        # legend_labels=classification_names,
        # legend_location="lower right",
        show=False,
        # plot_color = "gist_rainbow",
        feature_order = [1, 3, 2, 4, 0, 5],
        title = "CPET AId beslutningsudvikling",
        auto_size_plot= False,
        # new_base_value = global_base_values
        link="logit"
    )
    # fjern label
    plt.gca().set_xlabel("")
    ax = plt.gca()
    plt.rcParams["font.family"] = "Arial"

    xmin, xmax = ax.get_xlim()

    # ax.set_xticks([xmin, xmax])
    # ax.set_xticklabels(["Lavere sandsynlighed", "Højere sandsynlighed"])

    ax.set_xticks(np.arange(0, 1.01, 0.1))
    # ax.set_xticklabels(["0%", "10%","20%","30%","40%","50%","60%","70%","80%","90%","100%"])
    ax.set_xticklabels(["0%", "","20%","","40%","","60%","","80%","","100%"])

    #Sætter standard gæt til at være ved 25%
    BaseValueLine = ax.lines[0] #Grå lodret basevalue linje 
    BaseValueLineX = BaseValueLine.get_xdata()
    BaseValueLineX[0] = 0.25
    BaseValueLineX[-1] = 0.25

    BaseValueLine.set_xdata(BaseValueLineX)


    # BaseValueLine.set_visible(False) #Indkommenter hvis standardgæt linjen skal slettes.
    
    #Vandrette feature linjer
    width = 1
    ax.lines[1].set_linewidth(width)
    ax.lines[2].set_linewidth(width)
    ax.lines[3].set_linewidth(width)
    ax.lines[4].set_linewidth(width)
    ax.lines[5].set_linewidth(width)

    #Klassifikationslinjer
    CardiacLine = ax.lines[6]
    CardiacLine.set_linestyle('dashdot')
    CardiacLine.set_linewidth(2)
    CardiacX = CardiacLine.get_xdata()
    CardiacY = CardiacLine.get_ydata()


    # slutpunktet af linjen
    x_end = CardiacX[-1]-0.03
    y_end = CardiacY[-1]+0.01

    ax.text(
        x_end,
        y_end,
        "K",   # 1, 2, 3, 4...
        fontsize=12,
        verticalalignment='baseline',
        fontweight='bold',
        zorder = 10
    )

    PulmoLine = ax.lines[7]
    PulmoLine.set_linestyle('dashed')
    PulmoLine.set_linewidth(2)
    
    PulmoX = PulmoLine.get_xdata()
    PulmoY = PulmoLine.get_ydata()

    # slutpunktet af linjen
    x_end = PulmoX[-1]-0.03
    y_end = PulmoY[-1]+0.01
    ax.text(
        x_end,
        y_end,
        "P",   # 1, 2, 3, 4...
        fontsize=12,
        verticalalignment='baseline',
        fontweight='bold',
        zorder = 10
    )

    MuscoLine = ax.lines[8]
    MuscoLine.set_linestyle('dotted')    
    MuscoLine.set_linewidth(2)
    MuscoX = MuscoLine.get_xdata()
    MuscoY = MuscoLine.get_ydata()

    # slutpunktet af linjen
    x_end = MuscoX[-1]-0.03
    y_end = MuscoY[-1]+0.01

    ax.text(
        x_end,
        y_end,
        "M",   # 1, 2, 3, 4...
        fontsize=12,
        verticalalignment='baseline',
        fontweight='bold',
        zorder = 10
    )


    HealthyLine = ax.lines[9]
    HealthyLine.set_linestyle('solid')
    HealthyLine.set_linewidth(2)
    HealthyX = HealthyLine.get_xdata()
    HealthyY = HealthyLine.get_ydata()
    

    # slutpunktet af linjen
    x_end = HealthyX[-1]-0.03
    y_end = HealthyY[-1]+0.01

    ax.text(
        x_end,
        y_end,
        "R",   # 1, 2, 3, 4...
        fontsize=12,
        verticalalignment='baseline',
        fontweight='bold',
        zorder = 10
    )


    #Sætter alles startpunkt til at være ved 25%
    CardiacX[0] = 0.25
    CardiacLine.set_xdata(CardiacX)
    
    PulmoX[0] = 0.25
    PulmoLine.set_xdata(PulmoX)
    
    MuscoX[0] = 0.25
    MuscoLine.set_xdata(MuscoX)
    
    HealthyX[0] = 0.25
    HealthyLine.set_xdata(HealthyX)



    # mid = (xmin + xmax) / 2

    # # definér områder (justér hvis du vil)
    # left_limit = xmin + 0.65 * (mid - xmin)
    # right_limit = mid + 0.15 * (xmax - mid)

    # count_left = 0
    # count_right = 0

    # lines = ax.lines[6:9]
    # for line in lines:
    #     x = line.get_xdata()
    #     if len(x) > 1:
    #         # brug punkt efter første feature
    #         x_val = x[1]

    #         if x_val <= left_limit:
    #             count_left += 1
    #         elif x_val >= right_limit:
    #             count_right += 1

    # threshold = 1
    # # vælg side med mindst "trafik"
    # if count_left > count_right and count_left >= threshold:
    #     loc = "lower right"
    # elif count_right > count_left and count_right >= threshold:
    #     loc = "lower left"
    # else:
    #     # hvis det er tæt → fallback
    #     loc = "lower right"

    location = "lower right"

    ax.legend([CardiacLine,PulmoLine,MuscoLine, HealthyLine], classification_names, loc = location)
    
    plt.savefig("CPET-AId/CPET-AId/decisionplot.png", bbox_inches="tight")
    # plt.show()





#Test af modulet



data1 = [("Kardielt", 82.5),("Pulmonalt", 1.1),("Muskulært", 16.0),("Rask", 0.4)]
barchart = Barchart(data1)

data2 = [("Kardielt", 12.5),("Pulmonalt", 105.1),("Muskulært", -5.0),("Rask", 0.4)]
barchart2 = Barchart(data2)

data3 = [("Kardielt", 0.5),("Pulmonalt", 0.1),("Muskulært", 0.01),("Rask", 95.4)]
barchart3 = Barchart(data3)

data4 = [("Kardielt", 40.0),("Pulmonalt", 20.5),("Muskulært", 40.0),("Rask", 20.5)]
barchart4 = Barchart(data4)














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

c.save()











#########################################Test af Decisionplot############################3

c = canvas.Canvas("Modultest Decisionplot.pdf") # opdatere så den stemmer overens med GUI fra Main
    
Max_width, Max_hight = A4 #dette vil svare til øverst højre hjørne af PDF'en, hvor 0,0 er nederst venstre hjørne
margin_x = Max_width*0.1
margin_y = Max_hight*0.1
x = margin_x
y = Max_hight - margin_y


c.setFillColor("black")
c.setTitle("Modultest Decisionplot.pdf")
c.setFont('Arial',26) #font for title 
c.drawString(x,y,"Modultest Decisionplot")


c.setFont('Arial',12) #font for title 
c.drawString(x,y-50,"Beslutningsplot 1")

# Patient 5;
Shap_values1 = [[
  [ 0.78798157, -0.31402695,  0.04011863, -0.9707369 ],
  [ 0.0323705,  -0.46186036,  0.5747566,  -0.16537623],
  [-0.04824072, -0.10042012,  0.01773896,  0.12267144],
  [-0.24123555,  0.26461136, -0.5246118,  -0.7999075 ],
  [ 0.47733706, -0.8367276,   0.35610256, -1.0144894 ],
  [ 0.6645622,  -0.5206991,  -0.23113263, -1.2991651 ]
  ]]
Base_values1 =[0.09750652313232422, -0.538670003414154, -0.10174283385276794, 0.537470281124115]

Proba1 = [("Kardielt", 82.5),("Pulmonalt", 1.1),("Muskulært", 16.0),("Rask", 0.4)]

# Feature Values
# [[ 0.81416587 48.3         0.50944644  3.03949345  0.67707986  0.07846154]]

decisionplot(Proba1, feature_names_values, Shap_values1, Base_values1)

c.drawImage(
    "CPET-AId\CPET-AId\Beslutningsplot.png",
    50,
    50,
    height=500,
    width=500,
    preserveAspectRatio=True,
)

c.save()





#Patient 6:
Shap_values2 =[[
  [ 0.6356973,  -0.31540003, -0.30324632, -1.1946781 ]
  [ 0.33193555, -0.29285127, -0.81566703, -0.10770864]
  [ 0.5091625,  -0.63144016, -0.2364658,  -0.2761005 ]
  [ 0.48417282,  0.07912832, -0.9779154,   0.3928914 ]
  [ 0.00981862, -0.42130688, -0.3593603,  -0.40897375]
  [-0.6991844,  -1.3953285,   0.21650329,  1.4198644 ]
  ]]
Base_values2 = [0.09750652313232422, -0.538670003414154, -0.10174283385276794, 0.537470281124115]

Proba2 = [("Kardielt", 71.8),("Pulmonalt", 0.5),("Muskulært", 1.4),("Rask", 26.3)]

# Feature Values
# [[ 0.68685807 56.58333333  1.63155849  0.90499717  0.95303932  0.20733263]]


#Patient 7
# Shap
# [[[ 0.7987291  -0.06454745 -0.4584995  -1.2239481 ]
#   [ 0.5826505  -0.24001962 -1.2383113  -0.17743333]
#   [-0.06576226 -0.08508807  0.02363913  0.02176452]
#   [-0.17207584 -0.63507736 -0.639844   -0.42397532]
#   [ 0.06812508 -1.3545815   0.13933516  1.4791169 ]
#   [ 0.29278153  0.4100879  -0.12919219 -1.5965527 ]]]
# Base
# [0.09750652313232422, -0.538670003414154, -0.10174283385276794, 0.537470281124115]
# Proba
# [[0.9215575  0.01512295 0.01676839 0.04655121]]

# Feature Values
# [[ 0.52874674 44.5         0.63700928  3.24105505  1.13179898  0.04692308]]

#Patient 8
# Shap
# [[[ 0.11258955  1.051198   -0.5635411  -1.2800114 ]
#   [-0.28415054 -0.30050775  2.0221314  -0.15833502]
#   [ 0.0879013  -0.5826975   0.23717901  0.22464146]
#   [-0.3051583   0.07932777 -0.50418776 -0.6664305 ]
#   [ 0.279542   -0.5562634   0.7758268  -0.85830903]
#   [ 0.38363904  0.37783703 -0.00377895 -1.1497225 ]]]
# Base
# [0.09750652313232422, -0.538670003414154, -0.10174283385276794, 0.537470281124115]
# Proba
# [[0.1697116  0.07314587 0.75304025 0.00410225]]

# Feature Values
# [[ 0.41714702 31.13586712 -0.6975135   2.98406829  0.72725989 -0.04048736]]