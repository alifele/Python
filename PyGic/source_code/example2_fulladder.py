from main import Circuit

inout = {
    'inputs': ['a','b', 'c_in'],
    'outputs': ['s', 'c_out']
}

myCirc = Circuit(inout)
myCirc.addXORgate('node1', ['a','b'])
myCirc.addXORgate('s', ['node1','c_in'])
myCirc.addANDgate('node2', ['node1','c_in'])
myCirc.addANDgate('node3', ['a','b'])
myCirc.addORgate('c_out', ['node2', 'node3'])


inputs = [[1,1,1],[1,0,0],[0,0,1],[1,0,1],[1,0,0]]

result = myCirc.Run(inputs, ['s','c_out'], time_step = 5, order=['a','b','c_in'])
#print(result)
#print(myCirc.result)
myCirc.plot()
