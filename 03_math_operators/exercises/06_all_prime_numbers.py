# Receive a number from the user, and print if the number is a prime number.

num = 7 # check if it divides by 2, 3, 4, 5, 6
# [2, 3, 4, 5, 6]

# 1) get all the numbers prior the chosen num

# range(n, m, j)
# n - first number
# m - last number (not including)
# j - jumps

if num % 2 == 0: #
    print(f"{num} is not a prime number")

else: #            [3:num+1:2]
    for i in range(3, num + 1, 2): # check that "num" is not divisable by any i in range
        print(f"i = {i}")

        if i == num:
            print("The number is a prime number")
            break

        if num % i == 0:
            print(f"{num} is not a prime number")
            break

    print("will print anyway")



# check all nums up to that chosen num