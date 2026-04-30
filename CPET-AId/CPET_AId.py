import Datavalidering
import ML_model
import Post_processering

def CPET_AId(data):
    peak_R = data[0]
    pre_processed_data = data[1:]
    
    if Datavalidering.Data_validation(pre_processed_data):
        CPET_AId_proba = ML_model.classify(pre_processed_data)
        # eksempel på CPET_AId_proba[("fys_name", probability),x4]
        
        R_validation, feature_names_values, shap_values, base_values, global_base_values = Post_processering.post_processing(peak_R, pre_processed_data) 
        # eksempel på et af disse array: cardiac_post_processed = {["Kardielt:", 50%, parameters[], Highest_value]}
        # parameters[(VO2_name,VO2_value),("PVO2",10%)]
                
        barchart = Visualization(CPET_AId_proba)
        
        PDF_print(barchart, cardiac_post_processed, pulmo_post_processed, musco_post_processed, healthy_post_processed, R_validation)
    else:
        PDF_print_error()
