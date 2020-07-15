![](https://github.com/alifele/Python/raw/master/PyGic/logo.png) 


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
Sine wave, 

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

Now suppose that we want to simulate the following circuit in the package:


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

myCiruit = Circuit();
```





## III) Costuming package based on your needs



#### 1. Adding New Standard Parts

#### 2. costum signals 


Ali Fele Paranj
Physics student at sharif university of tech.
2020