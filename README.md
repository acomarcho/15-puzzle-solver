# 15-puzzle-solver
15 puzzle solver made in Python, made by applying branch and bound algorithm.

# About
This program is wrote using Python for it's main logic calculations and HTML/CSS/JavaScript for it's graphical user interface. In connecting Python code to HTML/CSS/JavaScript code, the library Eel is used (https://github.com/ChrisKnott/Eel). 

The branch and bound algorithm uses a heuristic where the computed cost is the sum of the node's current depth and the amount of tiles (excluding the empty tile) that are out of place.

The user interface is based on Silicon Design System, where you can access it here https://www.figma.com/community/file/1082210150893947691.

# Demo
![chrome_3dRuyyYSBG](https://user-images.githubusercontent.com/29671825/161415316-a39089aa-b165-47d4-8a9f-c8e88ebf36ca.gif)

# How to run
Make sure you have Python (https://www.python.org/) and these following packages:
1. numpy
2. eel

You can install both packages by first installing pip (https://pypi.org/project/pip/) and running these commands:
```
pip install numpy
pip install eel
```

After making sure you have both, you can just go to the /bin folder and run this inside the command prompt:
```
python solver.py
```

# Editing testcases
Inside the /bin folder, you can change the testcases located in the /test folder. Please note that 16 corresponds to an empty tile inside the matrix.

# Author
Marchotridyo/13520119
