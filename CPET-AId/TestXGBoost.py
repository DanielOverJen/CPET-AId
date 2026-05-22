from xgboost import XGBClassifier
import os
import sys
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

sys.path.append(os.path.dirname(os.path.dirname(__file__))) # Til at kunne eksportere fra en anden mappe (Model_selection)
from Model_selection import HentCSV

current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "CPETAId_model.json")

CPETAIdModel = XGBClassifier()

CPETAIdModel.load_model(model_path)


ChosenFeatures = [11, 17, 42, 7, 35, 36] # Peak R og derefter de 6 features til modellen

y_pred = CPETAIdModel.predict(HentCSV.X_test[:,ChosenFeatures]) #Træningsdata forvirringsmatrice

cm = confusion_matrix(HentCSV.y_test, y_pred)

classification_names = ["Kardielt", "Pulmonalt", "Muskulært", "Rask"]
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=classification_names)
disp.plot()

# plt.savefig("ForvirringsmatrixModulTest.png", bbox_inches="tight")
plt.show()
