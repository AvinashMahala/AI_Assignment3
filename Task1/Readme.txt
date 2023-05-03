Name:   [Avinash Mahala]
UTA ID: [1002079433]

Task 1

Programming Language: Python
Version: 3.8

Code Structure:
1. load_data: Function to read and parse the training data from a file.
2. count_occurrences: Count the occurrences of various combinations of B, G, C, and F in the data.
3. calculate_probabilities: Function to calculate the conditional probability tables for the Bayesian network from the training data.
4. display_probabilities: Display the calculated probabilities in a readable format.
5. Main Program.

How to Run the Code:
1. Ensure Python 3.8 is installed on your system.
3. Use the command prompt or terminal to navigate to the folder "Task1_Task2" containing "bnet.py".
4. Run the program with the following command:
    bnet.py <training_data>
        <training_data> text file with training data.

Example Invocations:
1. Task 1: python bnet.py training_data.txt


Sample Run Results From the Given Training Data:
python bnet.py training_data.txt
------------------Task 1----------------------
Conditional Probability Tables:

P(G|B):
P(G=0|B=0) = 0.88 P(G=0|B=1) = 0.07 
P(G=1|B=0) = 0.12 P(G=1|B=1) = 0.93 

P(F|G,C):
P(F=0|G=0,C=0) = 0.04 P(F=0|G=0,C=1) = 0.68 
P(F=0|G=1,C=0) = 0.29 P(F=0|G=1,C=1) = 0.96 

P(F=1|G=0,C=0) = 0.96 P(F=1|G=0,C=1) = 0.32 
P(F=1|G=1,C=0) = 0.71 P(F=1|G=1,C=1) = 0.04 


------------------Task 1----------------------