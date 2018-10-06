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
4. **Select 5 Criteria** to grade your solutions on
5. Grade and **Apply Criteria** to the top 8 solutions
6. Creat an **Action Plan (AP)** for the best solution

A judge then grades your packet based on creativity, futuristic thinking, and being elaborate. The goal of the FPS Packet Analysis program is to have a comuter grade a packet.


## The Framework of Neural Nets

The FPS judge has to be able to decide which category a problem/solution is, if it is relevent to the future scene, - and if it isn't, why? - and if the problem is a logical cause or effect of the fuzzy.
Therefore, there are multiple independent networks to grade a packet.

#### The Categorizing Recurrent Neural Network
Probably the most complicated Neural Network to built and train, and the most straight forward named network, but probably the most complicated Neural Network in general. The CRNN will categorize and decide why a problem or solution is categorized the way it is.

#### The Yes Challenge/Relevant Solution Neural Network (YC/RSNN)
The YR as I've dubed it, which is a nickname for an abreviation, will find what makes good challenges and good solutions and grades them accordingly.

#### The Elaboration Neural Network (ENN)
"The N" for short, this Neural Network will decide if A) a challenge has clarity on why it's a futuristic problem and B) a relevent solution is elaborated on.

#### The step 4 Relevance Neural Network (4RNN)
This neural network's output will consist of the five types of criteria. The 4RNN will decide if a criteria is Advanced, Modified, Generic, Duplicate, or Not Relevant to the UP.

#### The Overal Neural Network (ONN)
This is not "one ANN to rule them all", but the "hardworkness neural network". It grades the Research Applied, the Creative Strength, and Futuristic thinking. This will be a difficult Neural Network to train becuase this is the most intuitive part of the grading, and I'm not even sure what the inputs will be.

#### Underlying Problem Neural Network
The UP Neural Network will find the different sections the Underlying Problem is required to have and will also grade the two intuitive parts of the UP, the Focus and the Adequacy of it.

#### The Action plan Neural Network (Ann)
The Ann will grade the Action plan on it's Relevance, Effectiveness, Impact, Humaness, and Development. This Network will definitly be influenced by the UPNN
and it's Adequacy.


### Sections

#### main.py
The main file is the file where it takes the formatted training data from format.py and scores the Packet. `Main.py` still needs to tell the user what they did well on and what they need to improve on.
