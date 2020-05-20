# Neural Netwrok Plotter


A simple package that can plot sequential graphs. On of the well-known example of such graphs is the sequential neural networks.

Using this package you can draw your network.


***Requairment***

 - matplotlib
 - numpy


### Simple Exmaple

```
total_shape = [8,5,3,2,3,5,8]
edge = []

for i, layer_shape in enumerate(total_shape[:-1]):
    for k in range(layer_shape):
        edge += [[(i+1,k),(i+2,k_)] for k_ in range(total_shape[i+1])]

G = Graph()
for i, layer_shape in enumerate(total_shape):
    G.add_layer(i+1, layer_shape)
for elem in edge:
    G.add_edge(*elem[0], *elem[1])
G.draw()

```

![neural network](https://github.com/alifele/Python/blob/master/MyPackages/Neural%20Network%20Plotter/neuralnetwork.png  "Neural Network")



