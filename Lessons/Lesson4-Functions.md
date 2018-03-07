# Functions
----


To make our code easier to use, let's look at functions. These work by first making our code in a function , and then by calling it. 

When making a function we need to use the ```def``` keyword.

Let's turn our flat grass code into a function. 

Open your flatgrass script and change the code to:

```
from mcpi.minecraft import Minecraft 
def reset():
    grass=2
    air=0
    mc.setBlocks(-128,-64,-128,128,0,128,grass)
    mc.setBlocks(-128,0,-128,128,64,128,air)
```
When we run this, the code will not execute because we need to call the function, so below type:
```
reset()
```
![finished](http://s23.postimg.org/5kh0j3ttn/145889050226849.gif)
```
from mcpi.minecraft import Minecraft 
def reset():
    grass=2
    air=0
    mc.setBlocks(-128,-64,-128,128,0,128,grass)
    mc.setBlocks(-128,0,-128,128,64,128,air)

reset()
```
When this runs, the code will execute and your world will reset. Save and close this script.

Lets take a look at a more advanced function. This time we will create a function using our code that places a block. 

Create a new script and save it as functions_placeblock. 

Write the following code:
```
from mcpi.minecraft import Minecraft 
def placeBlock (x,y,z,block) :
    mc.setBlock(x,y,z,block)
```
Now, for this function we need to give 4 values when we run it. So to run the function that creates a glass block at position x=20,y=64,z=13, on a new line write:
```
placeBlock(20,64,13,20)
```
![finished](http://s23.postimg.org/5kh0j3ttn/145889050226849.gif)
```
from mcpi.minecraft import Minecraft 
def placeBlock (x,y,z,block) :
    mc.setBlock(x,y,z,block)

placeBlock(20,64,13,20)
```
Now run your script and notice that at this position, a glass block has been created (use your teleport script if you can't see it).

----
***Questions***

1) Using your 'variables_message' script, create a function to disply a message. The function should be called 'displayMessage' and require one value called 'message'. **Create this as a new script and save it as 'functions_question1'.** 

2) Usig your 'variables_teleport' script, create a function called 'teleport', that requires 3 values (x,y and z co-ordinates). **Create this as a new script, and save it as 'functions_question2'**.
