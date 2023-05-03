import sys
import itertools

#1. Load the training data from a file and store it as a list of tuples
def tsk3_load_data(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        tsk3_data = [tuple(map(int, line.strip().split())) for line in lines]
    return tsk3_data

#2. Count the occurrences of various combinations of B, G, C, and F in the data
def tsk3_count_occurrences(tsk3_data):
    tsk3_counts = {'B': {}, 'C': {}, 'GC': {}}
    for b, g, c, f in tsk3_data:
        tsk3_counts[(b, g)] = tsk3_counts.get((b, g), 0) + 1
        tsk3_counts[(g, c, f)] = tsk3_counts.get((g, c, f), 0) + 1
        tsk3_counts['B'][b] = tsk3_counts['B'].get(b, 0) + 1
        tsk3_counts['C'][c] = tsk3_counts['C'].get(c, 0) + 1
        tsk3_counts['GC'][(g, c)] = tsk3_counts['GC'].get((g, c), 0) + 1
    return tsk3_counts

#3. Calculate the conditional probabilities P(G|B) and P(F|G,C) using the counts
def tsk3_calculate_probabilities(tsk3_counts):
    tsk3_probabilities = {}
    tsk3_total_data_points = len(tsk3_data)

    tsk3_p_b = {0: tsk3_counts.get('B', 0)[0] / tsk3_total_data_points, 1: tsk3_counts.get('B', 0)[1] / tsk3_total_data_points}
    tsk3_p_c = {0: tsk3_counts.get('C', 0)[0] / tsk3_total_data_points, 1: tsk3_counts.get('C', 0)[1] / tsk3_total_data_points}

    tsk3_probabilities['B'] = tsk3_p_b
    tsk3_probabilities['C'] = tsk3_p_c

    for g in [0, 1]:
        for b in [0, 1]:
            tsk3_g_and_b_count = tsk3_counts.get((b, g), 0)
            tsk3_b_count = tsk3_counts['B'].get(b, 0)
            tsk3_probabilities[(g, b)] = tsk3_g_and_b_count / tsk3_b_count if tsk3_b_count > 0 else 0

    for f in [0, 1]:
        for g in [0, 1]:
            for c in [0, 1]:
                tsk3_gc_count = tsk3_counts['GC'].get((g, c), 0)
                tsk3_gcf_count = tsk3_counts.get((g, c, f), 0)
                tsk3_probabilities[(f, g, c)] = tsk3_gcf_count / tsk3_gc_count if tsk3_gc_count > 0 else 0

    return tsk3_probabilities

#4. Display the calculated probabilities in a readable format
def tsk3_display_probabilities(tsk3_probabilities):
    print("Conditional Probability Tables:\n")

    print("P(G|B):")
    for g in [0, 1]:
        for b in [0, 1]:
            print(f"P(G={g}|B={b}) = {tsk3_probabilities[(g, b)]:.2f}", end=' ')
        print()

    print("\nP(F|G,C):")
    for f in [0, 1]:
        for g in [0, 1]:
            for c in [0, 1]:
                print(f"P(F={f}|G={g},C={c}) = {tsk3_probabilities[(f, g, c)]:.2f}", end=' ')
            print()
        print()

#5. Calculate the JPD value using the conditional probability distributions
def tsk3_calculate_jpd_value(tsk3_probabilities, b_value, g_value, c_value, f_value):
    tsk3_p_b = tsk3_probabilities['B'].get(b_value, 0)
    tsk3_p_g_given_b = tsk3_probabilities[(g_value, b_value)]
    tsk3_p_c = tsk3_probabilities['C'].get(c_value, 0)
    tsk3_p_f_given_gc = tsk3_probabilities[(f_value, g_value, c_value)]

    tsk3_jpd_value = tsk3_p_b * tsk3_p_g_given_b * tsk3_p_c * tsk3_p_f_given_gc

    return tsk3_jpd_value

#6. Inference by enumeration
def tsk3_inference_by_enumeration(tsk3_probabilities, tsk3_query_variables, tsk3_evidence_variables):
    tsk3_query_variables.update(tsk3_evidence_variables)
    tsk3_total_probability = 0.0

    for b in [0, 1]:
        for g in [0, 1]:
            for c in [0, 1]:
                for f in [0, 1]:
                    tsk3_merged_dict = {'B': b, 'G': g, 'C': c, 'F': f}
                    if all(tsk3_merged_dict[key] == value for key, value in tsk3_query_variables.items()):
                        tsk3_jpd_value = tsk3_calculate_jpd_value(tsk3_probabilities, b, g, c, f)
                        tsk3_total_probability += tsk3_jpd_value

    return tsk3_total_probability

#7. Entry point of the program
if __name__ == "__main__":
    if len(sys.argv) < 4 or (len(sys.argv) > 4 and sys.argv[4] != "given"):
        print("Usage: bnet.py <training_data> <query variable values> [given <evidence variable values>]")
        sys.exit(1)

    tsk3_training_data_file = sys.argv[1]
    tsk3_data = tsk3_load_data(tsk3_training_data_file)

    tsk3_counts = tsk3_count_occurrences(tsk3_data)
    tsk3_probabilities = tsk3_calculate_probabilities(tsk3_counts)

    print("\n------------------Task 3----------------------")
    tsk3_query_variables = {var[0]: 1 if var.endswith("t") else 0 for var in sys.argv[2:] if var[0] in "BGCF" and not var.startswith("given")}
    tsk3_evidence_variables = {}
    if "given" in sys.argv:
        tsk3_evidence_start = sys.argv.index("given") + 1
        tsk3_evidence_variables = {var[0]: 1 if var.endswith("t") else 0 for var in sys.argv[tsk3_evidence_start:] if var[0] in "BGCF"}

    tsk3_probability = tsk3_inference_by_enumeration(tsk3_probabilities, tsk3_query_variables, tsk3_evidence_variables)

    print(f"P({', '.join([f'{k}={v}' for k, v in tsk3_query_variables.items()])} | {', '.join([f'{k}={v}' for k, v in tsk3_evidence_variables.items()])}) = {tsk3_probability:.6f}")

    print("\n------------------Task 3----------------------")


