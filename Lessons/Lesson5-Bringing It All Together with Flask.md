# Bringing it all together 

**We will combine what we have learnt about variables, functions and loops, to create some things in the game**

-----
##### Make a tree
As the flatgrass script got rid of all the trees, let's build some!

Again we will use ```mc.setBlocks```. 

We can create a function with 2 values for trunk height and leaf height

Create a new script and save it as 'structures_tree'.

Write the following code:
```
def Tree (trunkHeight,leavesHeight):
    x,y,z=mc.player.getPos()
    wood=17
    leaves=18
    mc.setBlocks(x+1,y,z+1,x+1.y+trunkHeight,z+1,wood)  
    mc.setBlocks(x-1,y+trunkHeight,z-1,x+3,y+leavesHeight,z+3,leaves) 
```
Create a tree  with trunk height = 6 and leaves height = 4.

So add the code
```python
Tree(6,4)
```
![finished](http://s23.postimg.org/5kh0j3ttn/145889050226849.gif)
```
def Tree (trunkHeight,leavesHeight):
    x,y,z=mc.player.getPos()
    wood=17
    leaves=18
    mc.setBlocks(x+1,y,z+1,x+1.y+trunkHeight,z+1,wood)  
    mc.setBlocks(x-1,y+trunkHeight,z-1,x+3,y+leavesHeight,z+3,leaves) 
    
Tree(6,4)
```
Run your script, it should look like the image below:

![Tree](http://s11.postimg.org/opihb6ccz/T4y_OVpg.png)

Save the script. 

-----
### Make a house

This next section, we will write code to create a house. Lets split this into code for building walls and code for making a roof

**Make walls**

To create walls we will use ```mc.setBlocks```

Lets write our code using a function. The code will create 4 walls at once

Write the following code:
```
def Walls(length,width,height,block):
    x,y,z=mc.player.getPos()
    mc.setBlocks(x+1,y,z+1,x+length,y+height,z+1,block) 
    mc.setBlocks(x+length,y,z+1,x+length,y+height,z+width,block) 
    mc.setBlocks(x+length,y,z+width,x+1,y+height,z+width,block) 
    mc.setBlocks(x+1,y,z+1,x+1,y+height,z+width,block)
```

See the diagram below to help understand the code

![Walls](http://s10.postimg.org/vlocy0c7t/walldiagram.png)

To add a door on wall 4 add the following code to your function
```
mc.setBlocks(x+1,y,z+width/2,x+1,y+1,z+width/2+1,0)
```

The diagram below shows the addition of the door

![WallsDoor](http://s21.postimg.org/69tox6bvb/walldoordiagram.png)

Now run the function we have just created with length =6, width=4, height=4 and block = Wooden Planks. 

![finished](http://s23.postimg.org/5kh0j3ttn/145889050226849.gif)
```
from mcpi.minecraft import Minecraft
def Walls(length,width,height,block):
    x,y,z=mc.player.getPos() #find current position
    mc.setBlocks(x+1,y,z+1,x+length,y+height,z+1,block) 
    mc.setBlocks(x+length,y,z+1,x+length,y+height,z+width,block)
    mc.setBlocks(x+length,y,z+width,x+1,y+height,z+width,block) 
    mc.setBlocks(x+1,y,z+1,x+1,y+height,z+width,block) 
    mc.setBlocks(x+1,y,z+width/2,x+1,y+1,z+width/2+1,0)
    
Walls(6,4,4,5)
```

Run your script, it should look like the image below:

![WallsDoor](http://s23.postimg.org/slaeigziz/Capture.png)

We also need to add a floor to our house. Add the following code to the walls function
```
mc.setBlocks(x+1,y-1,z+1,x+length,y-1,z+width,block)
```
![finished](http://s23.postimg.org/5kh0j3ttn/145889050226849.gif)
```
from mcpi.minecraft import Minecraft
def Walls(length,width,height,block):
    x,y,z=mc.player.getPos() #find current position
    mc.setBlocks(x+1,y,z+1,x+length,y+height,z+1,block) 
    mc.setBlocks(x+length,y,z+1,x+length,y+height,z+width,block) 
    mc.setBlocks(x+length,y,z+width,x+1,y+height,z+width,block) 
    mc.setBlocks(x+1,y,z+1,x+1,y+height,z+width,block) 
    mc.setBlocks(x+1,y,z+width/2,x+1,y+1,z+width/2+1,0)
    mc.setBlocks(x+1,y-1,z+1,x+length,y-1,z+width,block)
    
Walls(6,4,4,5)
```
Now move to an empty space in the game and run the scro[t again. It should look like the image below:

![Floor](http://s17.postimg.org/rmhenoofj/XFa_YBni.png)

---
***Questions***

**Between questions run the flatgrass script so you have more space**

1) Run the script and create walls with length 4, width 4 and height 3 made from Cobblestone. **Create this as a new script and save it as 'walls_question1'**

2) Run the script again to create walls with length 5, width 4 and height 4 made from Glass. **Create this as a new script and save it as 'walls_question2'**

----


**Creating a roof**

We now need to create a new function to create a roof, add the following function to your script:
```

def Roof(length, startheight,width,block,total height):
    x,y,z=mc.player.getPos()
    for xheight in range(0,length/2):
       mc.setBlocks(x+1,startheight+xheight,z+1,x+length,startheight+xheight,z+
       width,block)
        x+=1
        length-=2
        z+=1
        width-=2
```
This code uses a loop to build the roof. It builds it layer by layer, gradually getting smaller.

We can use both the roof and wall functions to build a house
```
Wall(8,6,4,5)
Roof(8,4,6,1,3)
```
![finished](http://s23.postimg.org/5kh0j3ttn/145889050226849.gif)
```python
def Walls(length,width,height,block):
    x,y,z=mc.player.getPos() #find current position
    mc.setBlocks(x+1,y,z+1,x+length,y+height,z+1,block) 
    mc.setBlocks(x+length,y,z+1,x+length,y+height,z+width,block)
    mc.setBlocks(x+length,y,z+width,x+1,y+height,z+width,block)
    mc.setBlocks(x+1,y,z+1,x+1,y+height,z+width,block) 
    mc.setBlocks(x+1,y,z+width/2,x+1,y+1,z+width/2+1,0)
    mc.setBlocks(x+1,y-1,z+1,x+length,y-1,z+width,block)

def Roof(length, startheight,width,block,total height):
    x,y,z=mc.player.getPos()
    for xheight in range(0,length/2):
       mc.setBlocks(x+1,startheight+xheight,z+1,x+length,startheight+xheight,z+
       width,block)
        x+=1
        length-=2
        z+=1
        width-=2

Wall(8,6,4,5)
Roof(8,4,6,1,3)
```

With these functions, it's important to specify the same length, width and height/start height.

When it runs it should look like the image below:

![House](http://s22.postimg.org/3phqz8jkh/house.png)



**Adding a moat**

Let's build upon our code to build a house, by adding a moat around the outside.

Add the following function to your script:
```
def Moat(length,width):
water=8
    mc.setBlocks(x-1,y-1,z-1,x+length+2,y-1,z+width+2,water)
```
Remember to use the same length and width as the walls and roof function. 

```
Moat(8,4)
Wall(8,6,4,5)
Roof(8,4,6,1,3)
```
![finished](http://s23.postimg.org/5kh0j3ttn/145889050226849.gif)
```python
from mcpi.minecraft import Minecraft
def Walls(length,width,height,block):
    x,y,z=mc.player.getPos() #find current position
    mc.setBlocks(x+1,y,z+1,x+length,y+height,z+1,block) 
    mc.setBlocks(x+length,y,z+1,x+length,y+height,z+width,block)
    mc.setBlocks(x+length,y,z+width,x+1,y+height,z+width,block) 
    mc.setBlocks(x+1,y,z+1,x+1,y+height,z+width,block) 
    mc.setBlocks(x+1,y,z+width/2,x+1,y+1,z+width/2+1,0)
    mc.setBlocks(x+1,y-1,z+1,x+length,y-1,z+width,block)

def Roof(length, startheight,width,block,total height):
    x,y,z=mc.player.getPos()
    for xheight in range(0,length/2):
       mc.setBlocks(x+1,startheight+xheight,z+1,x+length,startheight+xheight,z+
       width,block)
        x+=1
        length-=2
        z+=1
        width-=2

def Moat(length,width):
water=8
    mc.setBlocks(x-1,y-1,z-1,x+length+2,y-1,z+width+2,water)

Moat(8,4)
Wall(8,6,4,5)
Roof(8,4,6,1,3)
```

Now run this and it should look like the image below 
![Moat](http://i.imgur.com/748gwAb.png)

-----
***Connecting to Flask***

Flask is a simple Python framework for interacting with web sites and HTTP requests. 

Open "minecraft_controller.py" which is located inside the "Flask_Starter_Code" file. 

Look for the block of code that looks like this: 
```python
@app.route('/tree/', methods=['GET'])
def tree():
    return render_template('index.html')
 ```
 
 This an example of how Flask connects Python to a web page. ```@app.route('/tree/', methods=['GET'])``` defines the URL that triggers your Python code to do something. For example, once we run Flask, if you navigate to ```127.0.0.1/tree/```, you will trigger your script to create a tree. 
 
```def tree()``` defines our Tree function within our Flask application. ```return render_template('index.html')``` defines our response. In Flask, rendering a template is how we show a website. 

Let's make ```tree()``` actually do something. At the top of the script, add ```from structures_tree import Tree```

Add the following code below ```def tree()```

```
Tree(6,4)
```

![finished](http://s23.postimg.org/5kh0j3ttn/145889050226849.gif)
```
@app.route('/tree/', methods=['GET'])
def tree():
    Tree(6,4)
    return render_template('index.html')
```

Save your script and run it. Navigate to 127.0.0.1:5000 in your browser. 

You should see this: 

![screenshot](https://github.com/Jflick58/TeachPythonWithMinecraft/blob/master/Images/controller_screenshot.PNG)

Click the tree button. You should see a tree appear in front of you in the game!


***Questions***

**Between questions, run your 'flatgrass' script so you have more space**.


1) Build the following structure:


![house1](http://i.imgur.com/7kuhTgL.gif?1)


**Create in a new script and save as 'structures_question1'**

2) Build the following structure:

![house2](http://i.imgur.com/CSDaOYx.gif?)

**Create in a new script and save as 'structures_question2'**

3) Build the following structure:

![house3](http://i.imgur.com/L2OKrlP.gif?1)

**Create in a new script and save as 'structures_question3'**


4) Add the following:

Write an ```app.route(url, method)``` that creates a house.

**Save in mincecraft_controller.py**

5) Add the following:

Write an ```app.route(url, method)``` that creates a moat.

**Save in mincecraft_controller.py**

6) Add the following:

Write an ```app.route(url, method)``` that creates a custom structure of your choosing!

**Save in mincecraft_controller.py**
