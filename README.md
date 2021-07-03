# logic-gate-factory
Returns logic gates (as a lambda), to fulfill any truth table with binary inputs.

# Some examples:
AND gate truth table: 

|a|b|out|
|-|-|---|
|0|0|0|
|0|1|0|
|1|0|0|
|1|1|1|

So, the input would be "0001".
	
	x = get("0001")

`x` is now a lambda that acts the same as an AND gate.

	print(x(0,0))
	print(x(0,1))
	print(x(1,0))
	print(x(1,1))

```
0
0
0
1
```

----

We can also do different amounts of inputs. Here is the truth table of a NOT gate, which has one input:

|a|out|
|-|---|
|0|1|
|1|0|

	y = get("10")

`y` is now a NOT gate!

	print(y(0))
	print(y(1))

```
1
0
```

----

Here is something that has 3 inputs:

|a|b|c|out|
|-|-|-|---|
|0|0|0|1|
|0|0|1|0|
|0|1|0|0|
|0|1|1|0|
|1|0|0|0|
|1|0|1|0|
|1|1|0|0|
|1|1|1|1|

	z = get("10000001")

`z` now is a set of logic gates, which fulfills the truth table above.

