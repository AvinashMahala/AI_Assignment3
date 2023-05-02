Bayesian Network Conditional Probability Calculator
This program calculates the conditional probabilities P(G|B) and P(F|G,C) for a given Bayesian Network and training data. The Bayesian Network structure is as follows:
B -> G -> F <- C

The variables used in this Bayesian Network are:

B: True if there is a Baseball Game on TV, False if not
G: True if George watches TV, False if not
C: True if George is out of Cat Food, False if not
F: True if George feeds his cat, False if not
Training Data Format
The training data file should contain one data point per line, with each line representing the values of B, G, C, and F as space-separated integers:

B_value G_value C_value F_value

Each value should be either 0 (False) or 1 (True).

Usage
To use the program, run the following command in your terminal:
python bnet.py <training_data>
Replace <training_data> with the path to the training data file.


Output
The program will display the calculated conditional probabilities P(G|B) and P(F|G,C) in a readable format:

Conditional Probability Tables:

P(G|B):
P(G=0|B=0) = ...
P(G=1|B=0) = ...
P(G=0|B=1) = ...
P(G=1|B=1) = ...

P(F|G,C):
P(F=0|G=0,C=0) = ...
P(F=0|G=0,C=1) = ...
P(F=0|G=1,C=0) = ...
P(F=0|G=1,C=1) = ...
P(F=1|G=0,C=0) = ...
P(F=1|G=0,C=1) = ...
P(F=1|G=1,C=0) = ...
P(F=1|G=1,C=1) = ...


Dependencies
Python 3.6+ (No external libraries required)
License
This project is released under the MIT License.