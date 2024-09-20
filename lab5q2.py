# Number of correct answers and their frequencies
correct_answers = [0, 1, 2, 3, 4, 5]
frequencies = [5, 7, 10, 20, 12, 6]

# Total students
total_students = sum(frequencies)

# Mean = Σ(x * f) / N
mean = sum(x * f for x, f in zip(correct_answers, frequencies)) / total_students

# Variance = Σ(f * (x - mean)^2) / N
variance = sum(f * (x - mean) ** 2 for x, f in zip(correct_answers, frequencies)) / total_students

print(f"Mean: {mean:.2f}")
print(f"Variance: {variance:.2f}")
# Number of students with at least 4 correct answers (scores 4 or 5)
students_with_at_least_4 = sum(frequencies[4:])

# Probability = favorable outcomes / total outcomes
probability_at_least_4 = students_with_at_least_4 / total_students
print(f"Probability of scoring at least 4: {probability_at_least_4:.4f}")
