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

x is a lambda that acts the same as an AND gate.

----

We can also do different amounts of inputs. Here is the truth table of a NOT gate, which has one input:

|a|out|
|-|---|
|0|1|
|1|0|

	x = get("10")

x is now a NOT gate!

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

	x = get("10000001")

x now is a set of logic gates, which fulfills the truth table above.

