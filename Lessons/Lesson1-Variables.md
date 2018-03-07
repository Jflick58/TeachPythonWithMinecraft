# Variables 

-----


##### Example 1 - Display a message

Our first example of using variables will be to display a mesage in the game. Create a new script and save it as 'variables_message'.

When starting a new script always remember to add the import, without this your script will not work.
```python
from mcpi.minecraft import Minecraft 
```
On a new line, write the following code:


```python
mc.postToChat("Hello World")
```

This code will output the message within the brackets. 

![finished](http://s23.postimg.org/5kh0j3ttn/145889050226849.gif)
```python
from mcpi.minecraft import Minecraft 
mc.postToChat("Hello World")
```
Now run your script and you should see your message appear. It should look similar to the image below.

![message](http://s21.postimg.org/jjt8va6vr/unspecified_1_2.png)

Instead of writing the message directly into the code, let's use a variable. 

Edit your code so it looks like:

```
from mcpi.minecraft import Minecraft 
message="Hello World"
mc.postToChat(message)
```
This makes a variable called message. This variable has the text "Hello World".

Now run your script and you will see the message appear in the game.

When finished, save and close this script.

-------
***Questions***

1) Create a new variable called myName that contains your name as a string and output it in the game. **Create this is a new script and save it as 'variables_question1'**

![piggy](http://i.imgur.com/cZ4tibd.gif)


2) Create a new variable called myMessage and create your own message. Display your message in the game. **Create this as a new script and save it as 'variables_question2'**

------
#### Example 2- Finding Your Position 
For our next example you will find your position in the game. 

Notice you can see your position in the top left corner of the screen. We want to find the positon using code rather than this.
![pos](http://s11.postimg.org/lpi683ytv/poscorner_1.png)

Create a new script and save it as 'variables_findposition'

In the game your position uses co-ordinates. In minecraft there are x,y and z co-ordinates. 

When you move left or right this will change the x co-ordinate. 

When you move higher or lower this will change the y co-ordinate. 

When you move forward or backwards this will change the z co-ordinate.

![graph](http://s23.postimg.org/acdqigk23/new_graph.png)

So to find your position you need to find these 3 co-ordinates.

We can create a variable to hold all 3 co-ordinates or create 3 seperate variables that will each hold one co-ordinate.

First we will write code to store all co-ordinates in one variable. 

Write the following code :

```python
from mcpi.minecraft import Minecraft 
position=mc.player.getPos()
```
Now you have created a variable called 'position' that stores all 3 co-ordinates. These are found by the code 'mc.player.getPos()'.

Next we will create 3 variables each storing one co-ordinate. Edit your code to it looks like:


```python
from mcpi.minecraft import Minecraft 
positionX,positionY,positionZ=mc.player.getPos()
```
Now three variables have been created, holding their corresponding co-ordinate

Save and close the script

-----
**Questions**

3) Using mc.postToChat(), display each co-ordinate in the game.
**Create this in a new script and save it as 'variables_question3'**

After you have done this save and close the script

-----
#### Example 3- Changing Position (Teleport)

As well as knowing our position, we can also change it.

Create a new script and save it as 'variables_teleport'.

Look at the code below:
```python
mc.player.setPos(x,y,z)
```
With this you need to supply the x,y and z co-ordinate to change position in the game. Lets create these as variables. On a new line write the following:

```python
x=20
y=64
z=30
```
You have now made the co-ordinates that you want to teleport to. 

Now to use these to change position, on a new line write
```
mc.playerSetPos(x,y,z)
```



![finished](http://s23.postimg.org/5kh0j3ttn/145889050226849.gif)
```python
from mcpi.minecraft import Minecraft 
x=20
y=64
z=30
mc.playerSetPos(x,y,z)
```

Now run your script and see your character move !

Save and close the script.

-----
**Questions**

4) Try moving your character by choosing your own co-ordinates (be careful with the y co-ordinate, if it’s too low you may teleport underground. **Create this in a new script and save it as 'variables_question4'**

![pig2](http://s23.postimg.org/ndtwrtl6z/pig2fin.gif)

------

#### Example 4- Placing A Block 



We will create a block in front of our character, to do this we need to use what we learnt earlier to find our position.

Create a new script and save it as 'variables_placeblock'.

On a new line create three variables called 'positionX','positionY' and 'positionZ', with their co-ordinates. So type:
```python
from mcpi.minecraft import Minecraft 
positionX,positionY,positionZ=mc.player.getPos()
```

Now we know our position within the game, you can write some code to place a block in front of your character. 

Look at the following code:
```python
mc.setBlock(x,y,z,block)
```
For the code above, we need to supply four differne values. The first three are an x,y and z co-ordinate (this is to choose where to place a block). 

The final value that we need is a block ID  (see the blockID reference page).

Let's choose a stone block to use. This has an ID of 1. We can make this a variable.

On a new line write:

```python
stone=1
```
You have now created a variable called stone with the ID

You now have everything you need to place a block in front of your character. To do this we need to increase the z co-ordinate by one (so it appears in front). 

On a new line write:
```python
mc.setBlock(x,y,z+1,stone)
```
![finished](http://s23.postimg.org/5kh0j3ttn/145889050226849.gif)

```python
from mcpi.minecraft import Minecraft 
positionX,positionY,positionZ=mc.player.getPos()
stone=1
mc.setBlock(x,y,z+1,stone)
```

Run your script and a block should appear in front of your character, looking similar to the image below

![Map](http://s7.postimg.org/doa0kfewr/placeblock.png)

-----
**Questions**

5) Place a cobblestone block 6 spaces in front of your character.**Create this as a new script and save it as 'variables_question5'**.

6) Choose a block and place it 3 spaces behind your character. **Create this as a new script and save it as 'variables_question6'**.

7) Choose a block and place it 2 spaces to the left of your character. **Create this as a new script and save it as 'variables_question7'**

![pig3](http://i.imgur.com/hz2JDgj.gif)


#### Example 5- Place many blocks

Before we go further we will write some code that will replace everything with a flat level of grass blocks.

Create a new script and save it as 'flatgrass'.

Everything above this flat level will be removed. To do this and place more than one block we will use the code:
```python
mc.setBlocks(xstart,ystart,zstart,xend,yend,zend,block)
```
This code needs 7 values. 

The variables 'xstart','ystart','zstart' are co-ordinates where we will start placing blocks. 

The values 'xend','yend','zend' are co-ordinates where we will stop placing blocks (blocks will be placed inbetween here). 

As we have seen before, the final value is a block ID.

Write the following code:
```python
from mcpi.minecraft import Minecraft 
grass=2
air=0
mc.setBlocks(-128,-64,-128,128,0,128,grass)
mc.setBlocks(-128,0,-128,64,128,air)
```
![Map](http://s14.postimg.org/ekyny1ehd/map.png)

Now run your script, it should look like the image below (it may take a minute):

![Grass](http://s2.postimg.org/xht62kkzd/grass.png)

Save and close the script.

![pig7](http://s28.postimg.org/5ideiwkcd/piggyhintfin.gif)
