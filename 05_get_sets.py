import csv
import random

with open('all_sets.csv', newline='') as f:
    reader = csv.reader(f)
    all_sets_data = list(reader)

numbers = random.choice(all_sets_data)
print(numbers)