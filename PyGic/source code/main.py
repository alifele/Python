import numpy as np
import matplotlib.pyplot as plt
import copy
import pdb

##

class Circuit:

    def __init__(self, inout):
        self.gates = {} # the name of each gate is the output node of that gate
        self.node_dic_template = {
            'val':[],
            'in':[],
            'func':[], # this indicates the value of the node
            'probe_state':[] # idicates the presence of the probe
        }
        possible_keys = ['inputs', 'outputs', 'inputs_vector', 'outputs_vector']

        for KEY in possible_keys:
            try:

                if KEY == ('inputs_vector' or 'outputs_vector'):
                    #pdb.set_trace()
                    self.gates[inout[KEY][0]] = copy.deepcopy(self.node_dic_template)
                    for bus_elem in range(inout[KEY][1]):
                        self.gates[inout[KEY][0]]['val'].append('x')
                        #self.gates[inout[KEY][0]]['in'].append(inout[KEY][0])
                        self.gates[inout[KEY][0]]['in'].append(inout[KEY][0])
                        self.gates[inout[KEY][0]]['func'] = self.buffgate

                else:
                    for elem in inout[KEY]:
                        #pdb.set_trace()
                        self.gates[elem] = copy.deepcopy(self.node_dic_template)
                        self.gates[elem]['val'].append('x')
                        #self.gates[elem]['in'].append(elem)
                        self.gates[elem]['in'].append(elem)
                        self.gates[elem]['func'] = self.buffgate



            except:
                pass

    def addNode(self, name):
        if name not in self.gates.keys():
            self.gates[name] = copy.deepcopy(self.node_dic_template)

    def addBuffer(self, out):
        self.gates[out]['func'] = lambda x: x



    def addANDgate(self, out, in_list):
        self.addNode(out)
        self.gates[out]['func'] = self.ANDgate
        self.gates[out]['in'] = in_list

    def addORgate(self, out, in_list):
        self.addNode(out)
        self.gates[out]['func'] = self.ORgate
        self.gates[out]['in'] = in_list

    def addXORgate(self, out, in_list):
        self.addNode(out)
        self.gates[out]['func'] = self.XORgate
        self.gates[out]['in'] = in_list

    def addNANDgate(self, out, in_list):
        self.addNode(out)
        self.gates[out]['func'] = self.NANDgate
        self.gates[out]['in'] = in_list

    def addNORgate(self, out, in_list):
        self.addNode(out)
        self.gates[out]['func'] = self.NORgate
        self.gates[out]['in'] = in_list

    def addXNORgate(self, out, in_list):
        self.addNode(out)
        self.gates[out]['func'] = self.XNORgate
        self.gates[out]['in'] = in_list


    def addNOTgate(self, out, in1):
        self.addNode(out)
        self.gates[out]['func'] = self.NotGate()
        self.gates[out]['in'] = in1


    def buffgate(self, in_):
        return in_

    def ANDgate(self, in_):
        result = 1
        for elem in in_:
            result *= self.gates[elem]['func'](self.gates[elem]['in'])
        if result ==0:
            return 0
        else:
            return 1


    def ORgate(self, in_):
        result = 0
        for elem in in_:
            result += self.gates[elem]['func'](self.gates[elem]['in'])
        if result == 0:
            return 0
        else:
            return 1

    def XORgate(self, in_):
        result = 0
        for elem in in_:
            result += self.gates[elem]['func'](self.gates[elem]['in'])

        if result%2 ==0:
            return 0
        else:
            return 1

    def NANDgate(self, in_):
        return self.NotGate(self.ANDgate(in_))

    def NORgate(self, in_):
        return self.NotGate(self.ORgate(in_))

    def XNORgate(self, in_):
        return self.NotGate(self.XORgate(in_))

    def NotGate(self,in_):
        return int(not(in_))

    def addBit(self, input_node, logic):
        self.gates[input_node]['in'] = logic

    def addBits(self, input_nodes, logics):
        for L,I in zip(logics, input_nodes):
            self.gates[I]['in'] = L

    def run_simulation(self, out):
        return self.gates[out]['func'](self.gates[out]['in'])






## Test Bench

inout = {
    'inputs': ['a','b','c','d'],
    'outputs': ['out']
}

myCirc = Circuit(inout)
myCirc.addXORgate('node1', ['a','b'])
myCirc.addANDgate('node2', ['c','d'])
myCirc.addORgate('out', ['node1', 'node2'])
myCirc.addBit('a',1)
myCirc.addBits(['b','c','d'],[1,0,0])
out = myCirc.run_simulation('out')
print(out)

#
