# Exercise 1A: Create a string made of the first, middle and last character


# str1 = "James" # JMS
#       01234
str1 = "Arielus" # AIL
#         0123456
# str1 = "limudey-huts"
# str1 = "banana"
#       012345
#
# helllooo
# 01234567

first_char = str1[0]
last_char = str1[-1]


if len(str1) % 2 == 0: # זוגי
    after_middle_index = len(str1) // 2

    after_middle = str1[after_middle_index]
    before_middle = str1[after_middle_index - 1]

    middle_char = before_middle + after_middle

else: # אי זוגי
    middle_char = str1[len(str1) // 2]

new_str = first_char + middle_char + last_char

print(new_str)

