# FPS Packet Analytics

## General description

Making an analytical program to judge Future Problem Solvers competition packets.
[FPSPI](https://www.fpspi.org) (*Future Problem Solvers Program International*) is a non-profit program with 3 different categories:

* [Community Problem Solving](http://www.fpspi.org/cmps.html)
* [Global Issue Problem Solving](http://www.fpspi.org/gips.html)
* [Scenario Writing](http://www.fpspi.org/sw.html)

##### GIPS
In *Global Issue Problem Solving* (GIPS), you recieve a Future scene or *Fuzzy* -because this scene could possibly happen. Then you go through a six step process to fix this Fuzzy:

1. Find 16 **Problems**
2. Find the **Underlying Problem (UP)** in the 16 problems
3. Make 16 **Solutions** to the UP
4. **Select Criteria** - 5
5. **Apply Criteria** to top 8 solutions
6. Creat an **Action Plan (AP)** for the highest scored solution

A trained judge then grades the packet based on creativity, categories used, and possiblity.

The goal of Packet Analysis is to have a computer grade a packet. Just like an AP is written, benifits of a computer are:
A) A computer would grade a packet a lot faster than a Human.
B) The computer cannot be biased
C) I just want make this to test my neural network knowledge

The next part talks about the sections of this project

### catagory.py
This file takes the input of a folder in the root directory called Packet and
outputs data associated with each problem, solution, the UP, etc.

### main.py
The main file is going to be the file where it takes the arrays and dictionaries
from catagory.py and scores the Packet. Main.py possibly may tell the user what
they did well on and what they need to improve on.

### Packet
The packet directory contains the data that would be used for the testing and
training of the CANN (Categorizing Artificial Neural Network). The files in the
packet directory
