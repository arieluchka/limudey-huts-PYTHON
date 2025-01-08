

name = "Ariel"

list1 = [1, 2, 3]

fav_color = "blue"

# without fstrings we need to seperate the strings with "," or by adding strings to each other with "+"
print("hello", name, "What a nice day! How are you? i heard you favorite color is ", fav_color)

# regular string wont translate the {}
"hello {name}! How are you? i heard your fav color is {fav_color}. btw here is a number: {list1[1] + 5}"

# fstring will!
f"hello {name}! How are you? i heard your fav color is {fav_color}. btw here is a number: {list1[1] + 5}"

print(f"hello {name}! How are you? i heard your fav color is {fav_color}. btw here is a number: {list1[1] + 5}")


##########
# TASK 1 #
##########

# Create a variable of the name of the user
# Create a var with the age of the user
# greet the user with his name and tell him how old he will be in 10 years


# input("str") == read <------- bash alternative


name = input('please enter your name: ')
print(f"the type of name is {type(name)}")



age = input("please enter your age ")
age = int(age)  # דורס את המשתנה הקודם

# OR

# age = int(input("please enter your age "))


# # int()
# # float()
# # str()
# # list()
# # tuple()
# # dict()

print(f"the type of age is {type(age)}")

age_in_10_years = age + 10

print(f"hey {name}! you will be {age_in_10_years} in ten years!")
