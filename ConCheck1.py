def ConCheck():
    import numpy as np
    AcceptedValue = float(6.63e-34)
    AcceptedError = float(0)
    
    ExperimentalValue = float(4.29e-34)
    ExperimentalError = float(6.71e-35)
    
    if np.absolute(AcceptedValue-ExperimentalValue) < 3*np.sqrt((AcceptedError**2)-(ExperimentalError**2)):
        print("The Values are consistent")
    else:
        print("The Values are not-consistent")
ConCheck()