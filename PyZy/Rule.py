import numpy as np

class Rule:
    def __init__(self, inputs, outputs):
        self.inputs = inputs ## [ [InOut input,isnot] ]
        self.outputs = outputs ## [ [InOutoutput, isnot] ]

    def ruleResult(self, val, sweep):
        #import pdb; pdb.set_trace()
        minOfInputs = 10.0
        ## Finding the minimum
        for input_ in self.inputs:
            if input_[1] == "True":
                MF_value = 1 - input_[0].MF_Function(val)
            else:
                MF_value = input_[0].MF_Function(val)
            if MF_value < minOfInputs:
                minOfInputs = MF_value


        results = []
        for output_ in self.outputs:
            if output_[1] == "True":
                MF_value = output_[0].MF_Function(sweep)
            else:
                MF_value = output_[0].MF_Function(sweep)
            results.append(np.min([minOfInputs, MF_value]))

        return results
