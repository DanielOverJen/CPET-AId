import shap
import matplotlib.pyplot as plt
from reportlab.lib import colors
from reportlab.graphics.charts.barcharts import VerticalBarChart

def Barchart(data):
    """Skal modtage et datasæt bestående af tuple på formen ["navn":tal]"""

    bar_chart = VerticalBarChart()
    bar_chart.x = 0
    bar_chart.y = 0
    bar_chart.width = 400
    bar_chart.height = 200
    
    _ , values = zip(*data) #Deler input sandsynligheder op i 2 arrays
    
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
        auto_size_plot= False
        # new_base_value = global_base_values
        # link="logit"
    )
    # fjern label
    plt.gca().set_xlabel("")
    ax = plt.gca()
    plt.rcParams["font.family"] = "Arial"

    xmin, xmax = ax.get_xlim()

    ax.set_xticks([xmin, xmax])
    ax.set_xticklabels(["Lavere sandsynlighed", "Højere sandsynlighed"])

    BaseValueLine = ax.lines[0] #Grå lodret basevalue linje 
    BaseValueLine.set_visible(False)
    
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

    ax.legend([CardiacLine,PulmoLine,MuscoLine, HealthyLine], classification_names, loc = 'lower right')
    
    plt.savefig("CPET-AId/CPET-AId/decisionplot.png", bbox_inches="tight")
    # plt.show()


# #Test af kode 

# peak_R = 1.081632653

# pre_processed_data = [0.668427, 1004.5, 1.416444, 2.031264, 0.754807, 0.177091]


# R_validation, feature_names_values, shap_values, base_values = Post_processering.post_processing(peak_R, pre_processed_data)

# Class_proba = ML_model.classify(pre_processed_data)

# decisionplot(Class_proba, feature_names_values, shap_values, base_values)

