def Datavalidation(DiffPercentPeakVO2, PeakVE, first_half_O2Slope, StdVEVCO2, O2PulsePercent, first_half_VO2Slope):
    
    if (DiffPercentPeakVO2 is None 
        or PeakVE is None 
        or first_half_O2Slope is None 
        or StdVEVCO2 is None 
        or O2PulsePercent is None 
        or first_half_VO2Slope is None):
        return False
    else:
        return True
 
# Afprøvning med fiktivt data:
# result = Datavalidation(2, 2, 2, 3, 2, None)
# print(result)