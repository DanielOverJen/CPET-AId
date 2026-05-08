import HentCSV 
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, log_loss
import pandas as pd
import numpy as np 


patientindex = 196 #Patient 154 er på plads 196 efter shuffle
test_index = patientindex-HentCSV.split

X_train = HentCSV.X_train
y_train = HentCSV.y_train
X_test = HentCSV.X_test
y_test = HentCSV.y_test
feature_names = HentCSV.feature_names


antalestimators = 203
maksdybde = 3
learningrate = 0.08
evaluering = "mlogloss"


CPETAIdModel = XGBClassifier(
    n_estimators=antalestimators,
    random_state=42,
    max_depth=maksdybde,
    learning_rate = learningrate,
    objective="multi:softprob",
    eval_metric=evaluering
)

ChosenFeatures = [11, 17, 42, 7, 35, 36]


CPETAIdModel.fit(X_train[:,ChosenFeatures], y_train)


y_pred = CPETAIdModel.predict(X_test[:,ChosenFeatures])
acc = accuracy_score(y_test, y_pred)

print("Nøjatighed:", acc)

y_proba = CPETAIdModel.predict_proba(X_test[:,ChosenFeatures])
loss = log_loss(y_test, y_proba)

print("Logloss:", loss)
patientX_test = X_test[:, ChosenFeatures]

sample = pd.DataFrame([patientX_test[test_index]], columns=feature_names[ChosenFeatures])

print("\nPatient 154's data:")
print(CPETAIdModel.predict_proba([patientX_test[test_index]]))
print(sample.T)

np.set_printoptions(suppress=True) #Sørger lige for at printet ikke printes med videnskabelig notation e-01 f.eks.

from sklearn.metrics import classification_report

cr = classification_report(y_test, y_pred, target_names=HentCSV.classification_names)

print(cr)

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

cm = confusion_matrix(y_test, y_pred)

classification_names = ["Kardielt", "Pulmonalt", "Muskulært", "Rask"]
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=classification_names)
disp.plot()

# plt.savefig("ForvirringsmatrixModulTest.png", bbox_inches="tight")
plt.show()

