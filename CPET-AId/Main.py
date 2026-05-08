import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
# from reportlab.platypus import SimpleDocTemplate, Paragraph
# from reportlab.lib.styles import getSampleStyleSheet
import sys
import os
import numpy as np

sys.path.append(os.path.dirname(os.path.dirname(__file__))) # Til at kunne eksportere fra en anden mappe (Model_selection)
from Model_selection import HentCSV
import CPET_AId

# --- Henter testdatasættet fra HentCSV --- #

Model_features = [14, 11, 17, 42, 7, 35, 36] # Peak R og derefter de 6 features til modellen
Vyntus_data = HentCSV.X_test[:,Model_features]

new_row = np.array([[1.08, 0.668, 104.5, 1.416, 2.03, 0.755, None]]) #En falsk patient som har en null værdi
Vyntus_data = np.vstack([new_row, Vyntus_data])

# --- Vælg mappe at gemme rapporten i --- #
def choose_directory():
    """A function for the user to choose the directory in which the CPET AId report should be saved.
    This function is also the one, that calls CPET_AId.py after the directory is chosen"""
    # Henter den valgte patient fra dropdownm menuen
    chosen_patient = dropdown_options.index(selected_patient.get())

    file_path = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf")],
        initialfile=f"CPET_AId_Patient_{chosen_patient}.pdf",  # default navn
        title="Hvilken mappe vil du gemme rapporten i?"
    )
    

    if file_path:
        patient_data = Vyntus_data[chosen_patient]
        
        # print("Valgt patient:", chosen_patient) # Til debug
        # print(patient_data) # Til debug

        CPET_AId.CPET_AId(patient_data, file_path) # Kalder CPET AId med den valgte patients data

# --- GUI til eksport knap og valg af patient --- #
root = tk.Tk()
root.title("Eksportér CPET AId rapport")
root.geometry("400x150")

# Tekst om at man skal vælge patient:
choose_patient_label = tk.Label(root,text="Vælg hvilken patient, der ønskes analyseret via CPET AId:")
choose_patient_label.pack()

# Definerer valgmuligheder mm. til dropdownmenuen:
dropdown_options = [f"Patient {i}" for i in range(len(Vyntus_data))] # En liste med patientID'er i testdatasættet
selected_patient = tk.StringVar() # Variabel til at gemme valg
selected_patient.set(dropdown_options[0])  # default værdi
# Selve dropdown menuen:
combo = ttk.Combobox(root, textvariable=selected_patient, state="readonly")
combo['values'] = dropdown_options
combo.current(0)  # sætter default værdi
combo.pack()

# Knap til eksportering:
btn = tk.Button(root, text="Eksportér", command=choose_directory, height=2, width=15)
btn.pack(expand=True)

# Kører hele GUI'en:
root.mainloop()