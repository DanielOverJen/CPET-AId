import Datavalidering
import ML_model
import Post_processering
import Visualisering
import PDF_print

def CPET_AId(data, filepath):
    peak_R = data[0]
    pre_processed_data = data[1:]
    
    if Datavalidering.Datavalidation(pre_processed_data):
        CPET_AId_proba = ML_model.classify(pre_processed_data)
        # eksempel på CPET_AId_proba[("fys_name", probability),x4]
        
        R_validation, feature_names_values, shap_values, base_values = Post_processering.post_processing(peak_R, pre_processed_data) 

        barchart = Visualisering.Barchart(CPET_AId_proba)
        Visualisering.decisionplot(CPET_AId_proba, feature_names_values, shap_values, base_values)

        
        PDF_print.report(title="CPET AId resultat",
                          filename=filepath,
                          barchart= barchart,
                          R_valid= R_validation,
                          filepath_for_png="CPET-AId/CPET-AId/decisionplot.png")
    else:
        PDF_print.PDF_error(filepath)