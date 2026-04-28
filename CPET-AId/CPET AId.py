def CPET_AId(data):
    R = data[0]
    pre_processed_data = data[1:]
    
    if data_validation(pre_processed_data):
        CPET_AId_proba[] = ML_model(pre_processed_data)
        # eksempel på CPET_AId_proba["fys_name", probaility]
        
        cardiac_post_processed, pulmo_post_processed, musco_post_processed, healthy_post_processed, R_validation = post_processing(ML_model) 
        # eksempel på et af disse array: cardiac_post_processed = {["Kardielt:", 50%, parameters[], Highest_value]}
        # parameters[(VO2_name,VO2_value),("PVO2",10%)]
                
        barchart = visualization(CPET_AId_proba[])
        
        PDF_print(barchart, cardiac_post_processed, pulmo_post_processed, musco_post_processed, healthy_post_processed, R_validation)
    else:
        PDF_print_error()
