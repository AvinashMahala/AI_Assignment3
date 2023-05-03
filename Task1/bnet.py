import sys

# Load the training data from a file and store it as a list of tuples
def tsk1_load_data(file_path):
    # Open the file with the training data
    with open(file_path, 'r') as f:
        # Read all lines from the file
        lines = f.readlines()
        # Convert each line to a tuple of integers and add it to the data list
        data = [tuple(map(int, line.strip().split())) for line in lines]
    # Return the list of tuples containing the training data
    return data

# Count the occurrences of various combinations of B, G, C, and F in the data
def tsk1_count_occurrences(data):
    # Initialize the counts dictionary with empty dictionaries for B, C, and GC
    counts = {'B': {}, 'C': {}, 'GC': {}}
    # Iterate through the data (each tuple contains the values of B, G, C, and F)
    for tsk1_b, tsk1_g, tsk1_c, tsk1_f in data:
        # Increment the count for the (B, G) combination
        counts[(tsk1_b, tsk1_g)] = counts.get((tsk1_b, tsk1_g), 0) + 1
        # Increment the count for the (G, C, F) combination
        counts[(tsk1_g, tsk1_c, tsk1_f)] = counts.get((tsk1_g, tsk1_c, tsk1_f), 0) + 1
        # Increment the count for the B value
        counts['B'][tsk1_b] = counts['B'].get(tsk1_b, 0) + 1
        # Increment the count for the C value
        counts['C'][tsk1_c] = counts['C'].get(tsk1_c, 0) + 1
        # Increment the count for the (G, C) combination
        counts['GC'][(tsk1_g, tsk1_c)] = counts['GC'].get((tsk1_g, tsk1_c), 0) + 1
    # Return the counts dictionary with all occurrences
    return counts

# Calculate the conditional probabilities P(G|B) and P(F|G,C) using the counts
def tsk1_calculate_probabilities(counts):
    # Initialize the probabilities dictionary
    probabilities = {}
    # Calculate the total number of data points
    total_data_points = len(data)

    # Calculate the marginal probabilities of B and C

    tsk1_p_b = {0: counts.get('B', 0)[0] / total_data_points, 1: counts.get('B', 0)[1] / total_data_points}
    tsk1_p_c = {0: counts.get('C', 0)[0] / total_data_points, 1: counts.get('C', 0)[1] / total_data_points}

    # Store the marginal probabilities in the probabilities dictionary
    probabilities['B'] = tsk1_p_b
    probabilities['C'] = tsk1_p_c

    # Calculate P(G|B)
    for tsk1_g in [0, 1]:
        for tsk1_b in [0, 1]:
            # Get the count of the (B, G) combination
            tsk1_g_and_b_count = counts.get((tsk1_b,tsk1_g), 0)
            # Get the count of the B value
            tsk1_b_count = counts['B'].get(tsk1_b, 0)
            # Calculate and store the probability P(G|B)
            probabilities[(tsk1_g, tsk1_b)] = tsk1_g_and_b_count / tsk1_b_count if tsk1_b_count > 0 else 0
    

        # Calculate P(F|G,C)
    for tsk1_f in [0, 1]:
        for tsk1_g in [0, 1]:
            for tsk1_c in [0, 1]:
                # Get the count of the (G, C) combination
                tsk1_gc_count = counts['GC'].get((tsk1_g, tsk1_c), 0)
                # Get the count of the (G, C, F) combination
                tsk1_gcf_count = counts.get((tsk1_g, tsk1_c, tsk1_f), 0)
                # Calculate and store the probability P(F|G,C)
                probabilities[(tsk1_f, tsk1_g, tsk1_c)] = tsk1_gcf_count / \
                    tsk1_gc_count if tsk1_gc_count > 0 else 0

    # Return the probabilities dictionary with all calculated probabilities
    return probabilities


#Display the calculated probabilities in a readable format
def tsk1_display_probabilities(probabilities):
    # Print the title for the conditional probability tables
    print("Conditional Probability Tables:\n")
    # Print the P(G|B) probabilities
    print("P(G|B):")
    for tsk1_g in [0, 1]:
        for tsk1_b in [0, 1]:
            # Print the probability P(G=g|B=b) with two decimal places
            print(f"P(G={tsk1_g}|B={tsk1_b}) = {probabilities[(tsk1_g, tsk1_b)]:.2f}", end=' ')
        # Print a new line for the next row of probabilities
        print()

    # Print the P(F|G,C) probabilities
    print("\nP(F|G,C):")
    for tsk1_f in [0, 1]:
        for tsk1_g in [0, 1]:
            for tsk1_c in [0, 1]:
                # Print the probability P(F=f|G=g,C=c) with two decimal places
                print(f"P(F={tsk1_f}|G={tsk1_g},C={tsk1_c}) = {probabilities[(tsk1_f, tsk1_g, tsk1_c)]:.2f}", end=' ')
            # Print a new line for the next row of probabilities
            print()
        # Print an empty line to separate the tables for F=0 and F=1
        print()


#Entry point of the program
if __name__ == "__main__":
    #Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
    # Print the correct usage of the program and exit
        print("Usage: bnet.py <training_data>")
        sys.exit(1)
    #sys_argv = ['z', 'training_data.txt', 'Bt', 'Gf', 'Ct', 'Ff'] #to debug
    # Load the training data from the file
    tsk1_training_data_file = sys.argv[1]
    data = tsk1_load_data(tsk1_training_data_file)

    #Count the occurrences of various combinations in the data
    counts = tsk1_count_occurrences(data)

    # Calculate the probabilities using the counts
    probabilities = tsk1_calculate_probabilities(counts)

    print("\n------------------Task 1----------------------")
    # Display the calculated probabilities in a readable format
    tsk1_display_probabilities(probabilities)
    print("\n------------------Task 1----------------------")

