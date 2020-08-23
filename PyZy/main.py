import json
from RuleBase import RuleBase
from inout import InOut
import matplotlib.pyplot as plt
import numpy as np

class Main:
    def __init__(self, path):
        self.rules_path = path

        with open(self.rules_path) as json_file:
            self.Rules = json.load(json_file)
            print('Data is loaded\n')


    def createRuleBase(self):
        self.ruleBase = RuleBase()
        for key in self.Rules.keys():  ## self.Rule consists from input/outputs
            rule = self.Rules[key]
            inputs = []
            outputs = []
            for elem in rule:
                #print(elem[0]['type_'])
                if elem[0]['type_'] == "input":
                    inputs.append([InOut(**elem[0]),elem[1]])
                else:
                    outputs.append([InOut(**elem[0]),elem[1]])
            self.ruleBase.addRule(inputs, outputs)






if __name__ == "__main__":
    x = np.arange(-5,10,0.1)
    main = Main("./sample.json")
    #print(main.Rules['Rule1'][0])
    main.createRuleBase()
    result = []
    for elem in x:
        result.append(main.ruleBase.rulesList[0].ruleResult(2.5,elem))
    plt.plot(result);plt.show()
    #plt.plot(x,main.ruleBase.rulesList[0].inputs[0][0].MF_Function(x))
    #plt.show()



######### JSON Sample ############3
"""
{
  "Rule1": [
    [
      {
        "type_": "input",
        "MF_Function_type": "trapMF",
        "params": {
          "a": 1,
          "b": 2,
          "b1": 5,
          "c": 8
        }
      },
      "False"
    ],
    [
      {
        "type_": "input",
        "MF_Function_type": "triMF",
        "params": {
          "a": 1,
          "b": 2,
          "c": 5
        }
      },
      "False"
    ],
    [
      {
        "type_": "output",
        "MF_Function_type": "triMF",
        "params": {
          "a": 1,
          "b": 2,
          "c": 5
        }
      },
      "False"
    ]
  ],

  "Rule2": [
    [
      {
        "type_": "input",
        "MF_Function_type": "trapMF",
        "params": {
          "a": 1,
          "b": 2,
          "b1": 5,
          "c": 8
        }
      },
      "False"
    ],
    [
      {
        "type_": "input",
        "MF_Function_type": "triMF",
        "params": {
          "a": 1,
          "b": 2,
          "c": 5
        }
      },
      "False"
    ],
    [
      {
        "type_": "output",
        "MF_Function_type": "triMF",
        "params": {
          "a": 1,
          "b": 2,
          "c": 5
        }
      },
      "False"
    ]
  ]

}

"""
