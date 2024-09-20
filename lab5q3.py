import random

def draw_random_numbers(distribution, n):
  # Calculate the cumulative distribution function (CDF)
  cdf = {}
  cumulative_prob = 0
  for value, prob in distribution.items():
    cumulative_prob += prob
    cdf[value] = cumulative_prob

  # Generate random numbers
  random_numbers = []
  for _ in range(n):
    random_value = random.random()
    for value, cum_prob in cdf.items():
      if random_value <= cum_prob:
        random_numbers.append(value)
        break

  return random_numbers

# Define the probability mass function (PMF)
pmf = {1: 0.3, 2: 0.4, 3: 0.2, 4: 0.1}

# Draw 2000 random numbers
random_samples = draw_random_numbers(pmf, 2000)

# Print the random numbers
print(random_samples)