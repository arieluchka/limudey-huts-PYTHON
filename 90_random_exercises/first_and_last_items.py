# Exercise 5: Check if the first and last numbers of a list are the same



numbers = [10, 20, 30, 40, 10]
#          0    1   2   3   4
# numbers = [75, 65, 35, 75, 30]

first_num = numbers[0]

# op1 for last number
last_num = numbers[-1]

# op2 for last number
# last_num_index = len(numbers) - 1
# last_num = numbers[last_num_index]

if last_num == first_num:
    print("first number and last number are the same")
