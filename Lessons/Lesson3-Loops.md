# Loops
-----


# Example 1- Keep placing blocks in front

Lets take a look at an example of a 'for-loop'. This loop will keep placing blocks in front of your character.

Each block will be one space further when the loop runs. 

Create a new script and save it as 'loops_blocksinfront'.

Write the following code:

```python
from mcpi.minecraft import Minecraft
positionX,positionY,positionZ=mc.player.getPos()
stone=1
for x in range(0, 5):
 mc.setBlock(positionZ,positionY,positionZ+x,stone)
```
In the above code ```for x in range(0,5)``` makes the loop. 

To choose the length of a loop, a variable is created to count how many times it has run. 

For this, it is variable 'x'. This variable starts with a value of zero and when it has a value of 5, the loop will stop (the value of 'x' increases by 1, everytime the loop runs). 

In total, this loop will run six times, as the value starts at zero and ends at five. 

We can use the loop variable in our code. Notice it has been used with the z co-ordinate. Everytime the loop runs the variable will be added to the z co-ordinate so it becomes further infront of your character.


Run your script and it should look like the image below:

![front](http://s27.postimg.org/be5velxgz/infront_2.png)

The same thing can be done with a 'while loop'. Edit your code to use a 'while loop'.

![finished](http://s23.postimg.org/5kh0j3ttn/145889050226849.gif)
```python
from mcpi.minecraft import Minecraft
positionX,positionY,positionZ=mc.player.getPos()
stone=1
x=0
while (x<5):
 mc.setBlock(positionZ,positionY,positionZ+x,stone)
 x++
 
 ````````
 
 This while loop will run as long as x is less than 5. Once it is 5 or more the loop will stop. At the end of each loop x is increased by 1.
 
 Save and close your script
 
 -----
***Questions***

**After each question run the flatgrass script so there is more space in the game**


1) Write code using a for loop to place 10 Gravel blocks in front of your character. **Create this in a new script and save it as 'loops_question1'**


2) Write code using a while loop to place 7 Sand blocks to the right of your chacter. **Create this is a new script and save it as 'loops_question2'**.

![pig3](http://i.imgur.com/hz2JDgj.gif)
-----
# Example 2- Create a cube

In this section we will create a cube using `mc.setblocks` and a for-loop. 
We will create the first layer of a cube in front of our character, then repeat this with a loop.

Create a new script and save it as 'loops_cube'.
Write the following code:
```python
from mcpi.minecraft import Minecraft
positionX,positionY,positionZ=mc.player.getPos()
length=5
width=5
stone=1
mc.setBlocks(xposition,yposition,zposition+1,x+length,y,z+width,stone)
```
This will create the first layer of a cube in front of your character. As you can see, we have chosen the length and width.

Run your script and it should look like the image below:

![Cube](http://s22.postimg.org/7clngq8dt/firstlayer_2.png
)
We want to add more layers so it becomes taller and looks like a proper cube. To do this, we can use a 'for-loop' to repeat the code.

![finished](http://s23.postimg.org/5kh0j3ttn/145889050226849.gif)
```python
from mcpi.minecraft import Minecraft
xposition,yposition,zposition=mc.player.getPos()
length=6
height=5
width=6
stone=1
for x in range(0, height):
    mc.setBlocks(xposition,yposition,zposition+1,xposition+length,yposition+x,zposi    
    tion+width,stone
```
This loop will run 6 times  making a cube with length=6, width=6 and height=6.

 Everytime it runs, the cube will become one block taller(as the loop variable is added to the y co-ordinate). 

Run your script. It should produce a 6x6x6 cube and should look like the image below:
![Cube](http://s13.postimg.org/5udnadj6v/cubeloop2.png
)


------
***Questions***

**After each question run the flatgrass script so there is more space in the game**

3) Using a 'for-loop', create a cube 1 space in front of your character made of brick with: length=3, height=3, width=3. 
**Create this in a new script and save it as 'loops_question3'**

4) Using a 'for-loop', create a cube 3 spaces in front of your character made of glass with: length=4,height=7,width=4. **Create this in a new script and save it as 'loops_question4'**

5) Using a 'while loop', create a cube 2 spaces behind your characrer made of grass, make your own length, width and height. **Create this in a new script and save it as 'loops_question5'**
