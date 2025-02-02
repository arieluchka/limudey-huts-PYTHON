import random


print(random.random())

print(random.randint(1, 100))

print(random.randrange(1, 100, 2))

print(random.choice(["apple", "banana", "cherry"]))

print(random.choices(["apple", "banana", "cherry"], k=2)) # can repeat

print(random.sample(["apple", "banana", "cherry"], k=2)) # can't repeat