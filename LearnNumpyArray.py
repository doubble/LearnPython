# Create 2 new lists height and weight
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85, 1.83]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45, 80.00]

import numpy as np

# Create 2 numpy arrays from height and weight
np_height = np.array(height)
np_weight = np.array(weight)

print(type(np_height))

# Calculate bmi
bmi = np_weight / np_height ** 2

# Print the result
print(bmi)

# For a boolean response
print (bmi > 25)

# Print only those observations above 23
print (bmi[bmi > 25])

weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

np_weigth_kg = np.array(weight_kg)
np_weight_lbs = np_weigth_kg * 2.2
print (np_weight_lbs)
