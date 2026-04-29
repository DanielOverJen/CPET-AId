import shap
import os
import numpy as np
from xgboost import XGBClassifier

def post_processing(pre_processed_data):

    # Loader ML-modellen
    CPETAIdModel = XGBClassifier()
    # CPETAIdModel.load_model("CPET-AId/CPET-AId/CPETAId_model.json")

    current_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(current_dir, "CPETAId_model.json")

    CPETAIdModel.load_model(model_path)

    # Array med ML-modellens feature-navne
    feature_names = [
            "DiffPercentPeakVO2",
            "PeakVE",
            "first_half_O2Slope",
            "StdVEVCO2",
            "O2PulsePercent",
            "first_half_VO2Slope"
        ]
    
    # Sørg for korrekt shape (2D)
    reshaped_data = np.array(pre_processed_data).reshape(1, -1)

    # Laver SHAP explainer
    explainer = shap.TreeExplainer(CPETAIdModel)

    # Beregner SHAP værdier
    shap_values = explainer.shap_values(reshaped_data)

    return shap_values

data = [85.0, 60.0, 1.2, 0.15, 90.0, 1.8]
print(post_processing(data))