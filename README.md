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

A judge then grades your packet based on creativity, futuristic thinking, and being elaborate. The goal of the FPS Packet Analysis program is to have a comuter grade a packet.


### The Framework of Neural Nets
The FPS judge has to be able to decide which category a problem is, if it is relevent to the future scene - and if it isn't, why? - and, if the problem is a logical cause or effect of the fuzzy.
Therefore, there are multiple independent ANNs in order to grade a packet.

#### The Categorizing Artifical Neural Network (The CANN)
Probably the easiest Neural Network to train, the most straight forward named ANN, probably the easiest Neural Network in general. The CANN will decide why a defense problem and communication solution are categorized the way they are and how to do so.

#### The Yes Challenge/Relevant Solution Neural Network (YC/RSNN)
No pronouncable name for this ANN. The YR as I've pronounced it, will find what makes good challenges and solutions and grades the packet on what it thinks

#### The Elaboration Neural Network (ENN)
"The N" for short, this Neural Network will decide if A) a challenge is clear on why it's a problem and B) a relevent solution is elaborated on.

#### Underlying Problem Neural Network (UPNN)
The UP Neural Network will find the different sections the Underlying Problem is required to have and will also grade the two intuitive parts of the UP, the Focus and the Adequacy of it.

#### The step 4 Relevance Neural Network (4RNN)
This Network could have be done by the YR Neural Net. But becuase it's output layer will consist of the five categories for a criteria rather than the binary decision the YR has to make, I decided against it. The 4R will decide if the criteria are Advanced, Modified, Generic, Duplicate, or Not Relevant at all.

#### The Action plan Neural Network (Ann)
The Ann will grade the Action plan on it's Relevance, Effectiveness, Impact, Humaness, and Development. This Network will definitly be influenced by the UPNN
and it's Adequacy.

#### The Overal Neural Network (ONN)
This is not "one ANN to rule them all", but the "hardworkness neural network". It grades the Research Applied, the Creative Strength, and Futuristic thinking. This will be the most difficult Neural Network to train becuase this is the most intuitive part of the grading.

### Sections

#### main.py
The main file is the file where it takes the formatted training data from format.py and scores the Packet. `Main.py` still needs to tell the user what they did well on and what they need to improve on.
