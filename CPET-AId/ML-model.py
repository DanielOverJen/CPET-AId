from xgboost import XGBClassifier

CPETAIdModel = XGBClassifier()
CPETAIdModel.load_model("CPET-AId/CPET-AId/CPETAId_model.json")


def classify(data):
    """Function to calculate probabilities for the four classes. The data input should be:
    data = [DiffPercentPeakVO2, PeakVE, first_half_O2Slope, StdVEVCO2, O2PulsePercent, first_half_VO2Slope]
    """
    proba = CPETAIdModel.predict_proba([data])
    
    classification_names = ["Kardielt", "Pulmonalt", "Muskulært", "Rask"]

    proba = proba[0]*100

    result = [(name, round(float(p), 1)) for name, p in zip(classification_names, proba)]

    return result    