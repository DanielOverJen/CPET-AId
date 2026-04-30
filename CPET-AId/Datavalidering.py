
def Datavalidation(data):
    """Function for checking all the input data for null values. Input should be:
    data = [DiffPercentPeakVO2, PeakVE, first_half_O2Slope, StdVEVCO2, O2PulsePercent, first_half_VO2Slope]"""

    if any(x is None for x in data) :
        return False
    else:
        return True
