# while loops and for loops

# count = 5
#
# while count != 0:
#     print("shalom")
#     count = count-1
#
#
# print("end of code")





# For loops

# names = ["ariel", "batel", "yaniv", "sivan", "shay"]
#
#
# for name in names:
#     print(f"shalom {name}")


# print(f"Greeting " + names[0])
# print(f"Greetings {names[0]}")
# print(f"Greetings {names[1]}")
# print(f"Greetings {names[2]}")
# print(f"Greetings {names[3]}")


# for mashehoo in range(5, 10, 2):  # [5:10:2]
#     print(mashehoo)
#



# num_list1 = [1, 6, 12, 7]
#
# num_list2 = [7, 12, 6, 100]
#
#
# for i in range(len(num_list1)):
#     print(num_list1[i] + num_list2[i])
#
#

# import random
#
# print(random.randint(0, 100))
#

















# "real world" example

# word = "sHalOm MY Friends"
#
# num_of_lower = 0
# num_of_capital = 0
#
# for ma_she_ba_lahem in word:
#     if ma_she_ba_lahem.islower():
#         num_of_lower = num_of_lower + 1
#
#     elif ma_she_ba_lahem.isupper():
#         num_of_capital = num_of_capital + 1
#
#
# print(f"The string has {num_of_capital} capital letters and {num_of_lower} lower case letters")
#
#



# BREAK



# while True:
#     res = input("continue?")
#     if res != "yes":
#         break
#     else:
#         print("okay lets continue")
#
# print("out of the loop")


#
# for i in range(10):
#     print(i)
#     if i == 7:
#         break
#


# BREAK
# names = ["Ariel", "Sapir", "shlomi"]
#
# words = ["Hello", "Goodbye"]
#
#
# for name in names:
#     # print(f"{}")
#     for word in words:
#         print(word, name)
#
#     print("finishing the loop instance")
#



# # 1
# # 2 2
# # 3 3 3
# # 4 4 4 4
#
#
# for num in range(6):
#     print((str(num) + " ") * num)


# break pass continue

# continue - skips an iteration

# names = ["Ariel", "Sapir", "shlomi"]
#
# words = ["Hello", "Goodbye"]
#
#
# for name in names:
#     if name == "Sapir":
#         continue
#     for word in words:
#         print(word, name)
#
#     print("finishing the loop instance")


# pass - used to replace real code

# str1 = "banana"
#
# if len(str1) % 2 == 0:
#     pass
#
# else:
#     pass
#
# if bmi > 18:
#     pass
# elif bmi < 20:
#     pass
# elif bmi < 30:
#     pass

