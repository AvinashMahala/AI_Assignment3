import sys

def load_data(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        data = [tuple(map(int, line.strip().split())) for line in lines]
    return data

def count_occurrences(data):
    counts = {'B': {}, 'C': {}, 'GC': {}}
    for b, g, c, f in data:
        counts[(b, g)] = counts.get((b, g), 0) + 1
        counts[(g, c, f)] = counts.get((g, c, f), 0) + 1
        counts['B'][b] = counts['B'].get(b, 0) + 1
        counts['C'][c] = counts['C'].get(c, 0) + 1
        counts['GC'][(g, c)] = counts['GC'].get((g, c), 0) + 1
    return counts

def calculate_probabilities(counts):
    probabilities = {}
    total_data_points = len(data)

    # P(G|B)
    for g in [0, 1]:
        for b in [0, 1]:
            g_and_b_count = counts.get((b, g), 0)
            b_count = counts['B'].get(b, 0)
            probabilities[(g, b)] = g_and_b_count / b_count if b_count > 0 else 0

    # P(F|G,C)
    for f in [0, 1]:
        for g in [0, 1]:
            for c in [0, 1]:
                gc_count = counts['GC'].get((g, c), 0)
                gcf_count = counts.get((g, c, f), 0)
                probabilities[(f, g, c)] = gcf_count / gc_count if gc_count > 0 else 0

    return probabilities

def display_probabilities(probabilities):
    print("Conditional Probability Tables:\n")

    print("P(G|B):")
    for g in [0, 1]:
        for b in [0, 1]:
            print(f"P(G={g}|B={b}) = {probabilities[(g, b)]:.2f}", end=' ')
        print()

    print("\nP(F|G,C):")
    for f in [0, 1]:
        for g in [0, 1]:
            for c in [0, 1]:
                print(f"P(F={f}|G={g},C={c}) = {probabilities[(f, g, c)]:.2f}", end=' ')
            print()
        print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: bnet.py <training_data>")
        sys.exit(1)

    training_data_file = sys.argv[1]
    data = load_data(training_data_file)
    counts = count_occurrences(data)
    probabilities = calculate_probabilities(counts)
    display_probabilities(probabilities)
