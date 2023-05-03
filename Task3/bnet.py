import sys
import itertools


#1. Load the training data from a file and store it as a list of tuples
def load_data(file_path):
    # Open the file with the training data
    with open(file_path, 'r') as f:
        # Read all lines from the file
        lines = f.readlines()
        # Convert each line to a tuple of integers and add it to the data list
        data = [tuple(map(int, line.strip().split())) for line in lines]
    # Return the list of tuples containing the training data
    return data

#2. Count the occurrences of various combinations of B, G, C, and F in the data
def count_occurrences(data):
    # Initialize the counts dictionary with empty dictionaries for B, C, and GC
    counts = {'B': {}, 'C': {}, 'GC': {}}
    # Iterate through the data (each tuple contains the values of B, G, C, and F)
    for b, g, c, f in data:
        # Increment the count for the (B, G) combination
        counts[(b, g)] = counts.get((b, g), 0) + 1
        # Increment the count for the (G, C, F) combination
        counts[(g, c, f)] = counts.get((g, c, f), 0) + 1
        # Increment the count for the B value
        counts['B'][b] = counts['B'].get(b, 0) + 1
        # Increment the count for the C value
        counts['C'][c] = counts['C'].get(c, 0) + 1
        # Increment the count for the (G, C) combination
        counts['GC'][(g, c)] = counts['GC'].get((g, c), 0) + 1
    # Return the counts dictionary with all occurrences
    return counts

#3. Calculate the conditional probabilities P(G|B) and P(F|G,C) using the counts
def calculate_probabilities(counts):
    # Initialize the probabilities dictionary
    probabilities = {}
    # Calculate the total number of data points
    total_data_points = len(data)

    # Calculate the marginal probabilities of B and C

    p_b = {0: counts.get('B', 0)[0] / total_data_points, 1: counts.get('B', 0)[1] / total_data_points}
    p_c = {0: counts.get('C', 0)[0] / total_data_points, 1: counts.get('C', 0)[1] / total_data_points}

    # Store the marginal probabilities in the probabilities dictionary
    probabilities['B'] = p_b
    probabilities['C'] = p_c

    # Calculate P(G|B)
    for g in [0, 1]:
        for b in [0, 1]:
            # Get the count of the (B, G) combination
            g_and_b_count = counts.get((b, g), 0)
            # Get the count of the B value
            b_count = counts['B'].get(b, 0)
            # Calculate and store the probability P(G|B)
            probabilities[(g, b)] = g_and_b_count / b_count if b_count > 0 else 0

    # Calculate P(F|G,C)
    for f in [0, 1]:
        for g in [0, 1]:
            for c in [0, 1]:
                # Get the count of the (G, C) combination
                gc_count = counts['GC'].get((g, c), 0)
                # Get the count of the (G, C, F) combination
                gcf_count = counts.get((g, c, f), 0)
                # Calculate and store the probability P(F|G,C)
                probabilities[(f, g, c)] = gcf_count / gc_count if gc_count > 0 else 0

    # Return the probabilities dictionary with all calculated probabilities
    return probabilities

#4. Display the calculated probabilities in a readable format
def display_probabilities(probabilities):
    # Print the title for the conditional probability tables
    print("Conditional Probability Tables:\n")

    # Print the P(G|B) probabilities
    print("P(G|B):")
    for g in [0, 1]:
        for b in [0, 1]:
            # Print the probability P(G=g|B=b) with two decimal places
            print(f"P(G={g}|B={b}) = {probabilities[(g, b)]:.2f}", end=' ')
        # Print a new line for the next row of probabilities
        print()

    # Print the P(F|G,C) probabilities
    print("\nP(F|G,C):")
    for f in [0, 1]:
        for g in [0, 1]:
            for c in [0, 1]:
                # Print the probability P(F=f|G=g,C=c) with two decimal places
                print(f"P(F={f}|G={g},C={c}) = {probabilities[(f, g, c)]:.2f}", end=' ')
            # Print a new line for the next row of probabilities
            print()
        # Print an empty line to separate the tables for F=0 and F=1
        print()

#5. Calculate the JPD value using the conditional probability distributions
def calculate_jpd_value(probabilities, b_value, g_value, c_value, f_value):
    # Calculate P(B) using the probabilities dictionary
    p_b = probabilities['B'].get(b_value, 0)

    # Calculate P(G|B) using the probabilities dictionary
    p_g_given_b = probabilities[(g_value, b_value)]

    # Calculate P(C) using the probabilities dictionary
    p_c = probabilities['C'].get(c_value, 0)

    # Calculate P(F|G,C) using the probabilities dictionary
    p_f_given_gc = probabilities[(f_value, g_value, c_value)]

    # Calculate the JPD value using the conditional probability distributions
    jpd_value = p_b * p_g_given_b * p_c * p_f_given_gc

    # Return the JPD value
    return jpd_value

#6. Inference by enumeration
def inference_by_enumeration(probabilities, query_variables, evidence_variables):
    query_variables.update(evidence_variables)
    total_probability = 0.0

    for b in [0, 1]:
        for g in [0, 1]:
            for c in [0, 1]:
                for f in [0, 1]:
                    merged_dict = {'B': b, 'G': g, 'C': c, 'F': f}
                    if all(merged_dict[key] == value for key, value in query_variables.items()):
                        jpd_value = calculate_jpd_value(probabilities, b, g, c, f)
                        total_probability += jpd_value

    return total_probability


#7. Entry point of the program
if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) < 4 or (len(sys.argv) > 4 and sys.argv[4] != "given"):
        # Print the correct usage of the program and exit
        print("Usage: bnet.py <training_data> <query variable values> [given <evidence variable values>]")
        sys.exit(1)

    # Load the training data from the file
    training_data_file = sys.argv[1]
    data = load_data(training_data_file)

    # Count the occurrences of various combinations in the data
    counts = count_occurrences(data)

    # Calculate the probabilities using the counts
    probabilities = calculate_probabilities(counts)

    # Display the calculated probabilities in a readable format
    # display_probabilities(probabilities)



    print("\n------------------Task 3----------------------")
    # Parse the command-line arguments for the query and evidence variables
    query_variables = {var[0]: 1 if var.endswith("t") else 0 for var in sys.argv[2:] if var[0] in "BGCF" and not var.startswith("given")}
    evidence_variables = {}
    if "given" in sys.argv:
        evidence_start = sys.argv.index("given") + 1
        evidence_variables = {var[0]: 1 if var.endswith("t") else 0 for var in sys.argv[evidence_start:] if var[0] in "BGCF"}



    # Calculate the probability of the query given the evidence using inference by enumeration
    probability = inference_by_enumeration(probabilities, query_variables, evidence_variables)

    # Display the calculated probability value
    print(f"P({', '.join([f'{k}={v}' for k, v in query_variables.items()])} | {', '.join([f'{k}={v}' for k, v in evidence_variables.items()])}) = {probability:.6f}")

    print("\n------------------Task 3----------------------")