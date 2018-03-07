# If-Statements
----


# Example 1 

To show how we can use if-statements, we will write code so that something will happen when your character is at a certain position.

Write the following code:
```python
from mcpi.minecraft import Minecraft
positionX,positionY,positionY=mc.player.getPos()
if positionX>20
    mc.player.setPos(0,64,0)
```
In this code, an if-statement has been made. Firstly you find your position, then if the x co-ordinate is more than 20, the code in the if-statement will run. In this example that code will change your position to the middle of the map. 

![test](http://s27.postimg.org/tlmcimpgz/145889192934902.gif)

----
***Questions***

1) Create an if-statement that will teleport your character to (20,64,0) when your z co-ordinate is greater than 23. **Create this in a new script and save it as 'ifstatement_question1'**

2) Create an if-statement that will display a message saying 'you've gone too far' when your x co-ordinate is greater than 50. **Create this as a new script and save it as 'ifstatement_question2'**










