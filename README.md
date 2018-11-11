# FPS Computer Judge
A Machine Learning algorithm that grades Future Problem Solvers competition packets.


## The Basis of My Project: [FPSPI](https://www.fpspi.org)

FPSPI (*Future Problem Solvers Program International*) is a non-profit program with 3 competitions:

* [Global Issue Problem Solving](http://www.fpspi.org/gips.html)
* [Scenario Writing](http://www.fpspi.org/sw.html)
* [Community Problem Solving](http://www.fpspi.org/cmps.html)

This program just focuses on grading GIPS

### GIPS
In *Global Issue Problem Solving* (GIPS), you and your team of up to 4 people recieve a Future scene or *Fuzzy*. You go through a six step process to find the best solution to the Fuzzy:

1. **Problems:** Find 16 problems that are from the fuzzy 
2. **Underlying Problem (UP):** Find the biggest problem in the 16 problems that you created
3. **Solutions:** Make 16 solutions to the UP
4. **Select Criteria:** Pick the 5 best ways to grade your solutions
5. **Apply Criteria:** Grade the top 8 solutions (that you've chosen) based on your 5 selected Criteria
6. **Action Plan (AP):** Create a more in-detail passage about the best solution

A judge then grades your packet based on creativity, futuristic thinking, and elaboration. The goal of the FPS Computer Judge is to have a comuter be able to do the exact same thing.

## The program

### The Framework of Neural Nets

To grade a challenge, the Computer Judge (CJ) has to be able to decide which category the challenge is. If it is relevent to the fuzzy - if it isn't relevent, why? And if the challenge is a logical cause or effect of the fuzzy. Therefore, there are multiple independent networks to grade **just** a challenge.

So far, I have developed (or am developing) the folowing Neural Networks:

* Categorizing RNN

And that's it...

<!--
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
-->

## FAQ
   #### Where's all the Training Data?
   Well, FPSPI says that no one can post the Future scene of any packet online until 4 years after the packet was used... so let me know when it's 2023, the training data from 2018 will be open source then. If you want to help, and you need the training data, the best I can do is show you the JSON format that I use. It is located under the [template packet](https://github.com/th4t-gi/FPS-CJ/tree/master/template%20packet) directory.

## Acknowledgements
Thank you to FPSPI for inspiration and training data for this prodject. Not to mention its the reason I get up on friday mornings.

Thank you to datalogue and their repository [keras-attention](https://github.com/datalogue/keras-attention) for building a model that I didn't need to build.

