Name:   [Avinash Mahala]
UTA ID: [1002079433]

Task 3

Programming Language: Python
Version: 3.8

Code Structure:
1. tsk3_load_data: Function to read and parse the training data from a file.
2. tsk3_count_occurrences: Count the occurrences of various combinations of B, G, C, and F in the data.
3. tsk3_calculate_probabilities: Function to calculate the conditional probability tables for the Bayesian network from the training data.
4. tsk3_display_probabilities: Display the calculated probabilities in a readable format.
5. tsk3_calculate_jpd_value: Function to calculate the joint probability distribution (JPD) value for a given set of variable values.
6. tsk3_inference_by_enumeration: Function to perform inference by enumeration and calculate the probability for any event given evidence (if available).
7. Main Program

How to Run the Code:
1. Ensure Python 3.8 is installed on your system.
2. Save the code in a file named "bnet.py".
3. Use the command prompt or terminal to navigate to the folder containing "bnet.py".
4. Run the program with the following command:
    python bnet.py <training_data> <query variable values> [given <evidence variable values>]
   Replace <training_data> with the path to the training data file, <query variable values> with the values of the query variables, and <evidence variable values> with the values of the evidence variables (if any).

Example Invocations:
1. Task 3: python bnet.py training_data.txt Bt Gf given Ff

------------------Task 3----------------------
P(B=1, G=0, F=0 | F=0) = 0.003298

------------------Task 3----------------------

2. Task 3: python bnet.py training_data.txt Bt Ff
Sample Run Results From the Given Training Data:

------------------Task 3----------------------
P(B=1, F=0 | ) = 0.118007

------------------Task 3----------------------

