import sys

# Load the training data from a file and store it as a list of tuples
def load_data(file_path):
    # Open the file with the training data
    with open(file_path, 'r') as f:
        # Read all lines from the file
        lines = f.readlines()
        # Convert each line to a tuple of integers and add it to the data list
        data = [tuple(map(int, line.strip().split())) for line in lines]
    # Return the list of tuples containing the training data
    return data

# Count the occurrences of various combinations of B, G, C, and F in the data
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

# Calculate the conditional probabilities P(G|B) and P(F|G,C) using the counts
def calculate_probabilities(counts):
    # Initialize the probabilities dictionary
    probabilities = {}
    # Calculate the total number of data points
    total_data_points = len(data)

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

# Display the calculated probabilities in a readable format
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

# Entry point of the program
if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        # Print the correct usage of the program and exit
        print("Usage: bnet.py <training_data>")
        sys.exit(1)

    # Load the training data from the file
    training_data_file = sys.argv[1]
    data = load_data(training_data_file)

    # Count the occurrences of various combinations in the data
    counts = count_occurrences(data)

    # Calculate the probabilities using the counts
    probabilities = calculate_probabilities(counts)

    # Display the calculated probabilities in a readable format
    display_probabilities(probabilities)

