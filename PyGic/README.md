![](https://github.com/alifele/Python/raw/master/PyGic/Pic/logo.png) 


Documentation for PyGic Simulator.


# Discription
PyGic (stands for Python Logic) is a simple and lightweight Simulator, Written in python. using this software, you will be able to simulate digital circuits and  monitor its outputs.


This project is an open source project, and more features will be added to it. Like Graphical User Interface, Website based version, more complete real world electronics parts, a genetic programinc core to design circuits with AI and so on. So if you want to contribute to this open source project, contact me at ali.fele@gmail.com.


### Ideal Parts
* Ideal AND, OR, NOT, XOR, NAND, NOR, XNOR Gates
* FlipFlops (RS, JK, T, D)
* Signals ( sin wave, triangle, clock, pulse, pwm) 
* Probes ( to find the wave forms at the nodes)
* Flow table, Transition table, characteristics tables, etc. for circuits
* Some of the well-known circuits (like adder, shift register, decoder, encoder, SevenSegements decoders, counters, )
* Examples (pattern detector, ...)


### Parts Library
This elemts will have a propagation dely




***
# Tutorial 

## I) What is in this package?

### 1. Ideal Gates
This simulator has 7 built in Ideal gates (which has no propagation error).
These gates are : AND, OR, XOR, NAND, NOR, XNOR, NOT.

### 2. Standard Parts
Ideal gates and components are only useful when you want to learn the basics of logical circuits. But to design a real world circuit, you will use real world electronic components which are not Ideal any more. they have propagatoin delay, input and output limits and etc.
This package also has some of the well-known ICs. If you are using a component that there is no library for it in the software, you can easily add new ones (based on its chrachteristics discussed on the datasheet). we will get to that soon.

### 3. Signals
every circuit board is designed in order to manipulate the inputs and generate desierd outputs. the inputs can be as simple as the logical 0 and 1 or as complicate as a audio signal. In this package there are built in signals that you can use to examine your circuite. Also you can add your own costum signal, which we will descuss it later.
Here is the list of the built in signals:
Sine wave, square wave, trianagle wave, saw tooth wave, digital clock, logical 0 and 1 and last but not least a custom sequence.


### 4. Probes

to figure out what is going on in your circuit (for evaluating and debugging purposes) you need a tool that can monitor the output of a specific node of your circuite. This is easily done 
			
			
			
## II) Getting started


Using this package is very strait forward. As the first Step, you need to draw the sketch of your circuite. This is required, because you need the nodes of your circuite, in order to use this package.
Now, to define the circuite in the software, you need to make an instace of the Circuit class.
This class gets the inputs and outputs of the circut in its input. you need to 
simply use the python built in dictionary for this purpose. This Dictionary must have only the following keys :

| key            | Value     | Description                             |
|----------------|-----------|-----------------------------------------|
| inputs         | ['a','b'] | 'a' and 'b' are the binary inputs           |
| outputs        | ['out']   | 'out' is the  binary output             |
| inputs_vector  | ['A', 4]  | 'A' is the input bus which has 4 bits   |
| outputs vector | ['OUT' 5] | 'OUT' is the input bus which has 5 bits |

when you are creating the new instance of the Circuit class, you need to pass this dictionary as its input. You can check out the source code to figure out what is happening inside this class.



Now suppose that we want to simulate the following circuit in the package^1^:

![](https://raw.githubusercontent.com/alifele/Python/master/PyGic/Pic/sim_circuit.png) 

```python

# The first way to define the inputs and outputs
inout1 = {
	'inputs' : ['a','b','c','d'] ,
	'outputs' : ['out']
}

# The second way to define the inputs and outputs
inout2 = {
	'inputs_vector' : ['A', 4] ,
	'outputs' : ['out']
}

myCircuit = Circuit( inout1 );
```

#### Architecture Design

Now you have to desing the architecture of the circuit.
All of the built in gates are the methods of the Circuit class.
So to put a gate to the desing of your circuit, you need just simply call the appropirate method. the GATE methods will accept three argumets, in which the first argument is the output and the others are the inputs (exaclty like Verilog). Here is the possible gates:

| Gate | Method   |
|------|----------|
| AND  | ANDgate  |
| OR   | ORgate   |
| XOR  | XORgate  |
| NAND | NANDgate |
| NOR  | NORgate  |
| XNOR | XNORgate |
| NOT  | NOTgate  |

for example, to desing the sample circuit you should write

```python
myCircuit.ANDgate('node1', 'a', 'b')
myCircuit.ANDgate('node2', 'c', 'd')
myCircuit.NORgate('out', 'node1', 'node2')
```
#### applying signal stimulus

Now we need to add stimulus to the circuit. as we disscused earlier, there are 7 different built in signals that you can apply to your circiut.
Here is the table that contains all of the options you have:

| Signal           | Method        |
|------------------|---------------|
| Sine wave        | applySine     |
| Square wave      | applySquare   |
| Triangle wave    | applyTriange  |
| Sawtooth wave    | applySawtooth |
| digital clock    | applyClk      |
| logical 0 1      | applyLogic    |
| custom Sequence | applySeq      |


Every signal needs a config input as its argument (written in the form of a python dictionary). You can find more information about the configuration of each signals in the documentation of the source code.
The other input that you need to pass to the method is the node that you want to apply the stimulus in. Note that you can not apply the stimulus to the output of any gates.

For example, suppose that we want to apply logical binary inputs to the inputs of the circuit.

#### Monitoring the nodes using probes
Probes are built in tools in the Circuit class that you can use them to monitor the outputs in different nodes of your ciruit. These are something like osciloscope or logic analyzer. To put the probe at any node of your circuit, you need just simply write 


```python
myCircuit.putProbe(['node1', 'output'])
```
so now, you have two probes attached to node1 and output node. We will see later how you can see the results of your probes.

#### Starting the Simulation

So far we have designed the circuit and now computer knows where each gate is located and knows how every element is connected to each other. Now we need to run the simulation in order to see how the circuit behaves under applyed stimulus. To do this you need to call the "startSimulation" method of the Circuit object. This method needs a configuration dictionary to passed as its arguments. This dictionary has the required information that the method needs to run the simulation. among those configuration information, "time scale" and "simulation time" are mandatory.
 For example if you have any clk input, the period of clk will be the "time scale".  Time scale refers to the duration of your clock pulse (if you have any) or the lowest duration of the alternating input. On the other hand, simulation time is the duration that you want to evaluate the behavior of your system at.


## III) Costumizing package based on your needs



#### 1. Adding New Standard Parts

#### 2. costum signals 


Notes:
1. I have used https://logic.ly/demo website for the drawings.

Ali Fele Paranj
Physics student at sharif university of tech.
2020