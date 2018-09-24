# FPS Packet Analytics

## General description

Making an analytical program to judge Future Problem Solvers competition packets.
[FPSPI](https://www.fpspi.org) (*Future Problem Solvers Program International*) is a non-profit program with 3 different competitions:

* [Community Problem Solving](http://www.fpspi.org/cmps.html)
* [Global Issue Problem Solving](http://www.fpspi.org/gips.html)
* [Scenario Writing](http://www.fpspi.org/sw.html)

### GIPS
In *Global Issue Problem Solving* (GIPS), you and your team of up to 4 people recieve a Future scene or *Fuzzy* – because this scene could possibly happen. You go through a six step process to fix the Fuzzy:

1. Find 16 **Problems**
2. Find the **Underlying Problem (UP)** or biggest problem in those 16 problems
3. Make 16 **Solutions** to the UP
4. **Select Criteria**: Create 5 criteria to grade your solutions on
5. Grade and **Apply Criteria** to the top 8 solutions
6. Creat an **Action Plan (AP)** for the best solution

A trained judge then grades the packet based on creativity, categories used, and possiblity. The goal of FPS Packet Analysis is to have a computer grade a packet. The reasons I am creating the FPS PA are
A) The computer will not be biased.
B) A computer would grade a packet a lot faster than a human.
C) I want to creating a machine learning program.

## _._.N.N.
CANN stands for Categorizing Artificial Neural Network. This is going to be located in `nn/CANN.py` where the neural network class will be but the grading of the packet will be in `main.py`.


## Sections of the project
### catagory.py
This file's job is to find the desired output of a neural network – at least for the training data. The `catagory.py` is where the FPS data object is stored which is used for retrieving data to check with the CANN of the problem or solution.

### main.py
The main file is going to be the file where it takes the data found from catagory.py and scores the Packet based on the CANN. `Main.py` possibly may tell the user what they did well on and what they need to improve on.

### Packet Directory
The packet directory contains the data that would be used for the testing and training of the CANN. The files in the packet directory would be typed in
