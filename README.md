# TeachPythonWithMinecraft
Teaching Python programming and concepts using the Python Minecraft API for the Raspberry Pi version of Minecraft. 

![alt text](https://www.evcomputing.com/wp-content/uploads/2016/05/minecraft-python.png)

## Background
This is the repo for the Florin High School (Sacramento, CA) Python workshop at KPMG. In this workshop, you'll learn Python programming and programming concepts by writing methods to control in-game Minecraft activites, and then you will connect those actions to a Flask-based website to act as a controller. We distributed Rapsberry Pi to the students for them to take with them after the workshop. If you don't have a rapsberry pi, you can emulate one on any Mac, Windows or Linux computer by following the instructions in [this link.](https://azeria-labs.com/emulate-raspberry-pi-with-qemu/)

You'll learn: 

- Basic version control with Github
- Python Virtual Environments 
- Dependency Management 
- Variables
- If Statements
- Loops
- Functions
- Backend Web Development concepts 

__All this culimnating in a Flask-based Web controller for Minecraft Pi!__

## How to use this repo 
1. Login to github with your account 

2. Click the "Star" button in the upper right hand corner.

3. Click the "Fork" button

4. Wait while Github copies the repo to your account 

5. Click the "Clone/Download" button and download the repo as a zip file to your machine 

6. Unzip the repo. Open a command prompt and `CD` to the location you extracted the repo to. 

7. Type `virtualenv venv` and hit enter. 

8. Wait while the virtual environment is activated. Then, type `source venv/bin/activate` and hit enter. 

9. You should see (venv) on the left side of your command prompt. Type `pip3 install -r requirements.txt` and hit enter 

10. You are ready to start learning Python with Minecraft! Bonus: You finished your first lesson on version control, virtual environments, and dependency management! __Good Job!__

11. Follow the lessons in the Lessons Folder.

## Useful Information

##### Create a script

Once the Pi has loaded and you are at the desktop screen, click on 
Menu then Programming and choose Python IDE3

Click file and select click script. To save, go to file then click save as.

We need to add an import for our script that will allow us to control Minecraft, type this code into the first line of your script

```python
from mcpi.minecraft import Minecraft 
```
**This import will need to be entered for every script you create**

You can move to a new line in a script by pressing enter

A script can be run by pressing f5 or going to the run option on the top menu bar

##### Load Minecraft 
Go to menu, go to games and click Minecraft. Bring this window alongside your Python script window so it is easier to use. You can move between the game and scripts by pressing the tab button.

In Minecraft click 'Create new world'. When this loads it will look something like the image below. Everyone’s will look different when it first loads. 
![Start](http://s8.postimg.org/8prlw8b1h/start.png)

##### Moving around the game

To move around the game, you can use the arrow keys and use the space button to jump. 

##### Hints

Look out for Pete the pig. For some questions he'll give hints on how to do them.

![pig](http://i.imgur.com/de99x5z.gif)

##### What if something goes wrong ?

If you get an error saying 'Syntax error' double check you have typed everything correctly and try running your script again.

### Targeted Curriculum
##### Key Stage 2

•   Design, write and debug programs that accomplish specific goals, including controlling or simulating physical systems; solve problems by decomposing them into smaller parts.

•   Use sequence, selection, and repetition in programs; work with variables and various forms of input and output.

##### Key Stage 3

•	Use 2 or more programming languages, at least one of which is textual, to solve a variety of computational problems; make appropriate use of data structures, design and develop modular programs that use procedures or functions.

### Useful Block ID's

|Block      |ID         | Picture  | Block  |ID | Picture
| ------------- |:-------------:|:-----:|:--------:|:---------:|------:|
| Air   | 0 |  |Wood Planks|5|![Woodplank](http://s2.postimg.org/5jw81562d/Oak_Wood_Planks.png)
| Stone      | 1      |   ![Stone](http://s16.postimg.org/8dg24cetd/Stone.png) |Bedrock|7|![Bedrock](http://s11.postimg.org/lkdwx47gf/Bedrock.png)
| Grass | 2      |  ![Grass](http://s23.postimg.org/ubtw3m0nb/Grass.png) |Sand|12|![Sand](http://s21.postimg.org/tkun3jj03/Sand.png)
|Dirt | 3| ![Dirt](http://s24.postimg.org/deit4k2ht/dirt.png)|Gravel|13|![Gravel](http://s17.postimg.org/fj8gcdvp7/Gravel_Pre_12w21a.png)
|Cobblestone| 4| ![Cobble](http://s13.postimg.org/uey7u78s3/Cobblestone.png)|Glass|20|![Glass](http://s14.postimg.org/ig3w5w3m5/Glass.png)
|Leaves|18|![Leaves](https://github.com/Jflick58/TeachPythonWithMinecraft/blob/master/Images/leaves.png)|Lava|11|![Lava](https://github.com/Jflick58/TeachPythonWithMinecraft/blob/master/Images/lava.jpg)
|Water|9|![Water](https://github.com/Jflick58/TeachPythonWithMinecraft/blob/master/Images/water.png)

## Credits

- Github user [jeremycook94](https://github.com/jeremycook94/Project) for creating most of the lesson plans.
- [EV Computing](https://www.evcomputing.com/classdescriptions/minecraft-programming-with-python) for the readme image.
- [The Raspberry Pi Foundation](https://projects.raspberrypi.org/en/projects/getting-started-with-minecraft-pi) for their work on     Rapsberry Pi, and the Raspbian image that contains the Python and Minecraft distributions used in this workshop.
- KPMG cowowrkers Matt Kwong, Andrew Suarez-Lopez, and Frank Wright

