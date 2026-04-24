from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_selection import SelectFromModel
import pandas as pd
from sklearn.metrics import accuracy_score, log_loss
import numpy as np
import HentCSV

# ---- Step 1: Definér base model ----
base_estimator = DecisionTreeClassifier(max_depth=2,random_state=42)

ada = AdaBoostClassifier(
    estimator=base_estimator,
    n_estimators=100,
    learning_rate=0.1,
    random_state=42
)

# ---- Step 2: Træn AdaBoost på alle features ----
ada.fit(HentCSV.X_train, HentCSV.y_train)

# ---- Step 3: Feature selection baseret på feature importance ----
selector = SelectFromModel(ada, prefit=True, threshold="median",max_features=21)  
# "median" = behold features med importance over medianen

# Transform data til kun de valgte features
X_train_selected = selector.transform(HentCSV.X_train)
X_test_selected = selector.transform(HentCSV.X_test)

# Boolean mask: True hvis feature er valgt
selected_features_mask = selector.get_support()
# Navne på valgte features (til analyse og rapport)
selected_feature_names = HentCSV.feature_names[selected_features_mask]
# Gem importance værdier fra original model
importances = ada.feature_importances_


# ---- Step 4: Træn ny AdaBoost model på valgte features ----
ada_selected = AdaBoostClassifier(
    estimator=base_estimator,
    n_estimators=100,
    learning_rate=0.5,
    random_state=42
)

ada_selected.fit(X_train_selected, HentCSV.y_train)


y_proba = ada_selected.predict_proba(X_test_selected)

# ------------------------------------------------------------
# Evaluering af modellen:
# ------------------------------------------------------------

# Klassisk prediction (højeste sandsynlighed)
y_pred = np.argmax(y_proba, axis=1)

accuracy = accuracy_score(HentCSV.y_test, y_pred)

# Log loss (MEGET vigtig for probabilistisk kvalitet)
loss = log_loss(HentCSV.y_test, y_proba)

# Confidence (model sikkerhed)
confidence = np.max(y_proba, axis=1)

mean_confidence = np.mean(confidence)

# Confidence threshold (valgfrit men stærkt)
threshold = 0.70

mask = confidence >= threshold

if np.sum(mask) > 0:
    thresholded_accuracy = accuracy_score(
        HentCSV.y_test[mask],
        y_pred[mask]
    )
    coverage = np.mean(mask)
else:
    thresholded_accuracy = None
    coverage = 0

# ------------------------------------------------------------
# OUTPUT
# ------------------------------------------------------------
print("\n--- MODEL EVALUATION ---")
print("Accuracy:", accuracy)
print("Log Loss:", loss)
print("Mean Confidence:", mean_confidence)

print("\n--- CONFIDENCE THRESHOLD ---")
print("Threshold:", threshold)
print("Coverage:", coverage)

if thresholded_accuracy is not None:
    print("Accuracy (kun sikre predictioner):", thresholded_accuracy)
else:
    print("Ingen predictions over threshold")

print("\n--- FEATURE EVALUATION ---")
print("Number of used features:", len(selected_feature_names))
print("Mean feature importance:", sum(importances)/len(selected_feature_names))










# # ---- Output ----
# print("\nValgte features med importance:")
# for name, imp, selected in zip(HentCSV.feature_names, importances, selected_features_mask):
#     if selected:
#         print(name, imp)

# print("\nAccuracy:", accuracy)

# print("\nAntal valgte features:", len(selected_feature_names))



# ---- Afprøvning af én patient ----

# patient_idx = 4  # vælg hvilken patient du vil teste
# X_patient = X_test_selected[patient_idx].reshape(1, -1)
# proba = ada_selected.predict_proba(X_patient)

# print("Afprøver modellen på patient nr: ", patient_idx)
# print(HentCSV.classification_names)
# print(proba)

# print("Patientens værdier:")
# sample = pd.DataFrame([HentCSV.X_test[patient_idx]],columns=HentCSV.feature_names)
# print(sample.T)