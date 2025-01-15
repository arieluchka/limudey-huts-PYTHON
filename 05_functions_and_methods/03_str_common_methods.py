# func vs method

# func
# print(5)
# print("banana")
# print([1, 2, "hello"])
# print()

# method
# "hello".upper()
# [1, 2].upper() # wont work!!!


# upper/lower
# str1 = "Hello world! My name is Ariel! my age is 90"

# print(str1)
#
# print(str1.upper())
#
# print(str1.lower())
#
# print(str1[0:5].upper() + str1[5:].lower())


# if "Hello" in str1:


###############################3
# startwith() / endswith(".txt")
#
# str1 = "Hello world! My name is Ariel! my age is 55"
#
# print(str1.startswith("world"))
#
# print(str1.endswith("90"))
#
# check_endswith = str1.endswith("90")
#
# if check_endswith:
#     print("the string ends with 90!")

####################################
# split


# str1 = "Hello world! My name is Ariel! my age is 55"
#
# print(str1)
#
# print(str1.split("!"))

# path = "/home/arieluchka/python/project/python/hello-world/python"
#
# print(path[17:23])
#
# count = 0
# word_list = path.split("/")
# print(word_list)
# # print(word_list[-2])
# for word in word_list:
#     if word == "python":
#         count += 1
#
# print(count)


#### join

# list1 = ["Ariel", "Batel", "iliya", "yehuda"]
#
# new_str = "/".join(list1)
# print(new_str)


# folder = "/workspace/oases-qa/repos/argocd/helm/dev/alerts"
#
# print(folder)
#
#
# splitted_path = folder[1:].split("/")
# print(splitted_path)
# print("/".join(splitted_path[0:4] + splitted_path[5:]))
#
# test1 = "shalom!!!1!11! my name is ariel!!11!!!!"
# print("!".join(test1.split("1")))

# Create a program that check if the *third* octet is even or odd
#
# ip = "192.168.1.50"
# ip = "10.0.11.12"
# ip = "1.1.2.5"
#
# print(ip.split("."))
#
# third_octet = int(ip.split(".")[2])
# print(third_octet)
# if int(ip.split(".")[2]) % 2 == 0:
#     print("The third octet is even")
# else:
#     print("Not even")

list1 = [1, 2, 3, "hello", 5, [1, 2, 3], "goodbye"]

print(list1[5][2])
print(list1)
list1[3] = 4
print(list1)




one = 1
two = 2
three = 4



