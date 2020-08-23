import numpy as np
import MFFunctions
import matplotlib.pyplot as plt


class InOut:

    def __init__(self, type_,MF_Function_type, params):
        self.type_ = type_
        self.MF_Function_type = MF_Function_type
        self.params = params

    def MF_Function(self, val):
        return MFFunctions.MFFunction.__dict__[self.MF_Function_type](val, **self.params)



if __name__ == "__main__":
    x = np.arange(-5,10,0.1)
    params = {
        "a":0,
        "b":1,
        "b1":2,
        "c":5
        }

    IN = InOut('input', 'trapMF',params)
    #print(IN.MF_Function([0]))
    plt.plot(x,IN.MF_Function(x))
    plt.show()
