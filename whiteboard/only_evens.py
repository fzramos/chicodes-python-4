import random

def only_evens(orig):
    return [i for i in orig if i % 2 == 0]

original = tuple(random.sample(range(1, 100), 10))

print(f"Original list: {original}")
print(f"Filtered list: {only_evens(original)}")