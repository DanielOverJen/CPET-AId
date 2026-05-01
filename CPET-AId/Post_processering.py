import shap
import os
import sys
import numpy as np
from xgboost import XGBClassifier

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from Model_selection import HentCSV

# HUSK at lave CPET AId.py om, så den har rigtige in og outputs (kan gøres i main branch)

def post_processing(Peak_R, pre_processed_data):
    """A function to validate whether the patient was at maximal capacity during exercise (R>=1,1), 
    and calculates, shap- and baseline values for the decisionplot in Visualisation.
    Returns: R-validation, feature_names_values, shap_values, base_values (in that order) """

    # --- R-VALIDERING --- #

    R_validation = Peak_R >= 1.1

    # --- SHAP ---#

    # Loader ML-modellen
    CPETAIdModel = XGBClassifier()
    # CPETAIdModel.load_model("CPET-AId/CPET-AId/CPETAId_model.json")

    current_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(current_dir, "CPETAId_model.json")

    CPETAIdModel.load_model(model_path)

    # Array med ML-modellens feature-navne og de tilhørende værdier
    feature_names_values = [
            f"Afvigelse fra forventet Peak VO2 \n = {pre_processed_data[0]} %",
            f"Peak minutventilation (VE) \n = {pre_processed_data[1]} L/min",
            f"Hældningen af O2-pulsen i testens \n første halvdel = {pre_processed_data[2]}",
            f"Spredningen af VE/VCO2 \n = {pre_processed_data[3]}",
            f"Afvigelse fra forventet Peak O2-puls \n = {pre_processed_data[4]} %",
            f"Hældningen af VO2 i testens \n første halvdel = {pre_processed_data[5]}"
        ]
    
    # Sørg for korrekt shape (2D)
    reshaped_data = np.array(pre_processed_data).reshape(1, -1)

    #Vi henter lige halvdelen af træningsdataet for at kunne få nogle globale basevalues
    idx = np.random.choice(HentCSV.X_train.shape[0], 88, replace=False)
    ChosenFeatures = [11, 17, 42, 7, 35, 36]
    X_background = HentCSV.X_train[idx][:, ChosenFeatures]


    # Laver SHAP explainer
    explainer = shap.TreeExplainer(CPETAIdModel, X_background) 
    #Laver global base shap value
    global_base_value = np.mean(explainer.expected_value)

    # Beregner SHAP værdier
    shap_values = explainer.shap_values(reshaped_data)

    # Laver SHAP værdierne på den rigtige form, så decision plot kan bruge det
    if isinstance(shap_values, np.ndarray) and shap_values.ndim == 3:
        shap_values = [
            shap_values[:, :, i]
            for i in range(shap_values.shape[2])
        ]

    # Beregner base values, som skal bruges i decision-plottet
    base_values = [float(x) for x in explainer.expected_value]

    return R_validation, feature_names_values, shap_values, base_values, global_base_value

#Test af funktionen:
# data = [85.0, 60.0, 1.2, 0.15, 90.0, 1.8]
# R = 0.9
# R_validation, feature_names_values, shap_values, base_values = post_processing(R, data)

# print(R_validation)
# print("\n")
# print(feature_names_values)
# print("\n")
# print(shap_values)
# print("\n")
# print(base_values)
      
      
