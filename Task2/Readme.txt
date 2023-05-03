Name:   [Avinash Mahala]
UTA ID: [1002079433]

Task 2

Programming Language: Python
Version: 3.8

Code Structure:
1. load_data: Function to read and parse the training data from a file.
2. count_occurrences: Count the occurrences of various combinations of B, G, C, and F in the data.
3. calculate_probabilities: Function to calculate the conditional probability tables for the Bayesian network from the training data.
4. display_probabilities: Display the calculated probabilities in a readable format
5. calculate_jpd_value: Function to calculate the joint probability distribution (JPD) value for a given set of variable values.
6. Main Program

How to Run the Code:
1. Ensure Python 3.8 is installed on your system.
3. Use the command prompt or terminal to navigate to the folder "Task1_Task2" containing "bnet.py".
4. Run the program with the following command:
    bnet.py <training_data> <Bt/Bf> <Gt/Gf> <Ct/Cf> <Ft/Ff>

        <training_data> text file with training data.
        Bt if B is true, Bf if B is false
        Gt if G is true, Gf if G is false
        Ct if C is true, Cf if C is false
        Ft if F is true, Ff if F is false

Example Invocations:
1. Task 2: python bnet.py training_data.txt Bt Gf Ct Ff




Sample Run Results From the Given Training Data:
python bnet.py training_data.txt Bt Gf Ct Ff 

------------------Task 2----------------------
P(B=1, G=0, C=1, F=0) = 0.002547

------------------Task 2----------------------