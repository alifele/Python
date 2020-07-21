from main import Circuit

inout = {
    'inputs': ['a','b','c','d'],
    'outputs': ['out', 'out1']
}

myCirc = Circuit(inout)
myCirc.addANDgate('node1', ['a','b'])
myCirc.addANDgate('node2', ['c','d'])
myCirc.addORgate('out1', ['node1', 'node2'])
myCirc.addANDgate('out2', ['node1', 'node2'])


inputs = [[1,1,1,1],[1,0,0,1],[0,0,1,1],[1,0,1,0],[1,0,0,0]]

result = myCirc.Run(inputs, ['out1','out2'], time_step = 5, order=['a','b','c','d'])
#print(result)
#print(myCirc.result)
myCirc.plot()
