from xgboost import XGBClassifier

CPETAIdModel = XGBClassifier()
CPETAIdModel.load_model("CPET-AId/CPET-AId/CPETAId_model.json")

data = [0.668427, 104.5, 1.416444, 2.031264, 0.754807, 0.177091]

classification_names = ["Kardiel", "Pulmonalt", "Muskulært", "Rask"]

proba = CPETAIdModel.predict_proba([data])

print(proba)