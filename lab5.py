from collections import Counter
from itertools import product

outcomes = list(product(range(1, 9), repeat=4))

# Calculate sum of each outcome
sums = [sum(roll) for roll in outcomes]

sum_frequencies = Counter(sums)
total_outcomes = len(outcomes)
probability_distribution = {sum_val: count / total_outcomes for sum_val, count in sum_frequencies.items()}

# Display the results
for sum_val, probability in sorted(probability_distribution.items()):
    print(f"Sum: {sum_val}, Probability: {probability:.4f}")
