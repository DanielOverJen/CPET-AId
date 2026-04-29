from xgboost import XGBClassifier
import os

CPETAIdModel = XGBClassifier()
# CPETAIdModel.load_model("CPET-AId/CPET-AId/CPETAId_model.json")

current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "CPETAId_model.json")

CPETAIdModel.load_model(model_path)

def classify(data):
    """Function to calculate probabilities for the four classes. The data input should be:
    data = [DiffPercentPeakVO2, PeakVE, first_half_O2Slope, StdVEVCO2, O2PulsePercent, first_half_VO2Slope]
    """
    proba = CPETAIdModel.predict_proba([data])
    
    classification_names = ["Kardielt", "Pulmonalt", "Muskulært", "Rask"]

    proba = proba[0]*100

    result = [(name, round(float(p), 1)) for name, p in zip(classification_names, proba)]

    return result    