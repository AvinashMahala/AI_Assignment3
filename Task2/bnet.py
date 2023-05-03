import sys

#1. Load the training data from a file and store it as a list of tuples
def tsk2_load_data(tsk2_file_path):
    # Open the file with the training data
    with open(tsk2_file_path, 'r') as f:
        # Read all lines from the file
        tsk2_lines = f.readlines()
        # Convert each line to a tuple of integers and add it to the data list
        tsk2_data = [tuple(map(int, tsk2_line.strip().split())) for tsk2_line in tsk2_lines]
    # Return the list of tuples containing the training data
    return tsk2_data

#2. Count the occurrences of various combinations of B, G, C, and F in the data
def tsk2_count_occurrences(tsk2_data):
    # Initialize the counts dictionary with empty dictionaries for B, C, and GC
    tsk2_counts = {'B': {}, 'C': {}, 'GC': {}}
    # Iterate through the data (each tuple contains the values of B, G, C, and F)
    for tsk2_b, tsk2_g, tsk2_c, tsk2_f in tsk2_data:
        # Increment the count for the (B, G) combination
        tsk2_counts[(tsk2_b, tsk2_g)] = tsk2_counts.get((tsk2_b, tsk2_g), 0) + 1
        # Increment the count for the (G, C, F) combination
        tsk2_counts[(tsk2_g, tsk2_c, tsk2_f)] = tsk2_counts.get((tsk2_g, tsk2_c, tsk2_f), 0) + 1
        # Increment the count for the B value
        tsk2_counts['B'][tsk2_b] = tsk2_counts['B'].get(tsk2_b, 0) + 1
        # Increment the count for the C value
        tsk2_counts['C'][tsk2_c] = tsk2_counts['C'].get(tsk2_c, 0) + 1
        # Increment the count for the (G, C) combination
        tsk2_counts['GC'][(tsk2_g, tsk2_c)] = tsk2_counts['GC'].get((tsk2_g, tsk2_c), 0) + 1
    # Return the counts dictionary with all occurrences
    return tsk2_counts

#3. Calculate the conditional probabilities P(G|B) and P(F|G,C) using the counts
def tsk2_calculate_probabilities(tsk2_counts):
    # Initialize the probabilities dictionary
    tsk2_probabilities = {}
    # Calculate the total number of data points
    tsk2_total_data_points = len(tsk2_data)

    # Calculate the marginal probabilities of B and C

    tsk2_p_b = {0: tsk2_counts.get('B', 0)[0] / tsk2_total_data_points, 1: tsk2_counts.get('B', 0)[1] / tsk2_total_data_points}
    tsk2_p_c = {0: tsk2_counts.get('C', 0)[0] / tsk2_total_data_points, 1: tsk2_counts.get('C', 0)[1] / tsk2_total_data_points}

    # Store the marginal probabilities in the probabilities dictionary
    tsk2_probabilities['B'] = tsk2_p_b
    tsk2_probabilities['C'] = tsk2_p_c

    # Calculate P(G|B)
    for tsk2_g in [0, 1]:
        for tsk2_b in [0, 1]:
            # Get the count of the (B, G) combination
            tsk2_g_and_b_count = tsk2_counts.get((tsk2_b, tsk2_g), 0)
            # Get the count of the B value
            tsk2_b_count = tsk2_counts['B'].get(tsk2_b, 0)
            # Calculate and store the probability P(G|B)
            tsk2_probabilities[(tsk2_g, tsk2_b)] = tsk2_g_and_b_count / tsk2_b_count if tsk2_b_count > 0 else 0

    # Calculate P(F|G,C)
    for f in [0, 1]:
        for g in [0, 1]:
            for c in [0, 1]:
                # Get the count of the (G, C) combination
                tsk2_gc_count = tsk2_counts['GC'].get((g, c), 0)
                # Get the count of the (G, C, F) combination
                tsk2_gcf_count = tsk2_counts.get((g, c, f), 0)
                # Calculate and store the probability P(F|G,C)
                tsk2_probabilities[(f, g, c)] = tsk2_gcf_count / tsk2_gc_count if tsk2_gc_count > 0 else 0

    # Return the probabilities dictionary with all calculated probabilities
    return tsk2_probabilities

#4. Display the calculated probabilities in a readable format
def tsk2_display_probabilities(tsk2_probabilities):
    # Print the title for the conditional probability tables
    print("Conditional Probability Tables:\n")

    # Print the P(G|B) probabilities
    print("P(G|B):")
    for g in [0, 1]:
        for b in [0, 1]:
            # Print the probability P(G=g|B=b) with two decimal places
            print(f"P(G={g}|B={b}) = {tsk2_probabilities[(g, b)]:.2f}", end=' ')
        # Print a new line for the next row of probabilities
        print()

    # Print the P(F|G,C) probabilities
    print("\nP(F|G,C):")
    for f in [0, 1]:
        for g in [0, 1]:
            for c in [0, 1]:
                # Print the probability P(F=f|G=g,C=c) with two decimal places
                print(f"P(F={f}|G={g},C={c}) = {tsk2_probabilities[(f, g, c)]:.2f}", end=' ')
            # Print a new line for the next row of probabilities
            print()
        # Print an empty line to separate the tables for F=0 and F=1
        print()

#5. Calculate the JPD value using the conditional probability distributions
def tsk2_calculate_jpd_value(tsk2_probabilities, tsk2_b_value, tsk2_g_value, tsk2_c_value, tsk2_f_value):
    # Calculate P(B) using the probabilities dictionary
    tsk2_p_b = tsk2_probabilities['B'].get(tsk2_b_value, 0)

    # Calculate P(G|B) using the probabilities dictionary
    tsk2_p_g_given_b = tsk2_probabilities[(tsk2_g_value, tsk2_b_value)]

    # Calculate P(C) using the probabilities dictionary
    tsk2_p_c = tsk2_probabilities['C'].get(tsk2_c_value, 0)

    # Calculate P(F|G,C) using the probabilities dictionary
    tsk2_p_f_given_gc = tsk2_probabilities[(tsk2_f_value, tsk2_g_value, tsk2_c_value)]

    # Calculate the JPD value using the conditional probability distributions
    tsk2_jpd_value = tsk2_p_b * tsk2_p_g_given_b * tsk2_p_c * tsk2_p_f_given_gc

    # Return the JPD value
    return tsk2_jpd_value


#6. Entry point of the program
if __name__ == "__main__":
    #Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 6:
        # Print the correct usage of the program and exit
        print("Usage: bnet.py <training_data> <Bt/Bf> <Gt/Gf> <Ct/Cf> <Ft/Ff>")
        sys.exit(1)
    #sys_argv = ['z', 'training_data.txt', 'Bt', 'Gf', 'Ct', 'Ff']  #to debug

    # Load the training data from the file
    tsk2_training_data_file = sys.argv[1]
    tsk2_data = tsk2_load_data(tsk2_training_data_file)

    # Count the occurrences of various combinations in the data
    tsk2_counts = tsk2_count_occurrences(tsk2_data)

    # Calculate the probabilities using the counts
    tsk2_probabilities = tsk2_calculate_probabilities(tsk2_counts)

    # # Display the calculated probabilities in a readable format
    # display_probabilities(probabilities)


    print("\n------------------Task 2----------------------")
    # Parse the command-line arguments for B, G, C, and F values
    tsk2_b_value = 1 if sys.argv[2] == 'Bt' else 0
    tsk2_g_value = 1 if sys.argv[3] == 'Gt' else 0
    tsk2_c_value = 1 if sys.argv[4] == 'Ct' else 0
    tsk2_f_value = 1 if sys.argv[5] == 'Ft' else 0

    # Calculate the JPD value using the conditional probability distributions
    tsk2_jpd_value = tsk2_calculate_jpd_value(tsk2_probabilities, tsk2_b_value, tsk2_g_value, tsk2_c_value, tsk2_f_value)

    # Display the calculated JPD value
    print(f"P(B={tsk2_b_value}, G={tsk2_g_value}, C={tsk2_c_value}, F={tsk2_f_value}) = {tsk2_jpd_value:.6f}")

    print("\n------------------Task 2----------------------\n")
