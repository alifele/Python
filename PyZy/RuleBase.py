from Rule import Rule

class RuleBase:
    def __init__(self):
        self.rulesList = []

    def addRule(self, inputs, outputs):
        self.rulesList.append(Rule(inputs, outputs))
