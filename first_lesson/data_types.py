# 2 data types
# 1) sequential and non sequential

####################################################################################
# string - מחרוזת
####################################################################################

# var_1 = "hello world"
# #        0123456789....
#
# var_1_2 = 'hello world'
# var_1_3 = """hello world"""
# var_1_4 = '''hello world'''


# we can use a combination of " and ', to print them out as well
# print("hello my name is 'ariel'")



# how to access specific characters?
# print(var_1[0]) # print character on index 0
# print(var_1[5]) # print character on index 5
# print(var_1[2:5]) # print characters from index 2, up to index 5 (not including!)
# print(var_1[:5]) # print characters from the start up to index 5 (not including!)
# print(var_1[6:]) # print characters from index 6 until the end


####################################################################################
# list - רשימות
####################################################################################

# var_2 = ["shalom", 2, 45, var_1]

# print(var_2)


# to access specific objects in a list is very similar to how we do it with strings
# print(var_2[2]) # print object in index 2


# we can also continue to get the index inside the indexed object!
# print(var_2[0][5])
# var_2[0] -> "shalom"[5] -> "m"
#              012345



####################################################################################
# tuple
# דומה לרישמות אבל קצת שונה
# נלמד בהמשך
####################################################################################

# var_3 = ("shalom", 2, 45, var_1)



####################################################################################
# 2) Non sequentials
# אובייקטים שלא מסודרים/מאורגנים


####################################################################################
# int (integer) - מספר שלם
####################################################################################

# var_4 = 4235

# print(var_4) # will still print "4235"


# we cant index ints!
#print(var_4[0]) <----- won`t work!


# we can use math operations on ints
# print(5 * 3) #  = 15
# print("5" * 3)# = 555



####################################################################################
# float - מספר עשרוני
####################################################################################
# var_6 = 4235.6




#############################################################
# Dictionary
# {key: value, key: value, key: value}

#!1) we cant have the same key twice

# dict

# car
# car1 = {
#     "color": "black",
#     "price": 5000,
#     "year": 2001,
# }
#
#
# car2 = {
#     "color": "blue",
#     "price": 15000,
#     "year": 2018
# }

# Change the value of a key

# print(car1)
# car1["price"] = 4500
# print(car1)


# Add a new key: value

# print(car1)
#
# car1["owner"] = "Ariel Agranovich"
#
# print(car1)
#
# car1["owner"] = "Shir"
#
# print(car1)


# Delete a key: value

# print(car1)

# del car1["owner"]
#
# print(car1)
#
# if car1["owner"] == "Ariel":
#     pass

# dict methods

car1 = {
    "color": "black",
    "price": [5000, 2000],
    "year": 2001,
}


# print(car1["price"])

# to get all values
# print(car1.values())

# to get all keys
# print(car1.keys())

# to get all items (key, value)
# print(car1.keys())

# for zoog in car1.items():
#     print(f"{zoog[0]}: {zoog[1]}")


# for val in car1.values():
#     print(val)

list1 = [
    {
        "color": "blue",
        "price": [15000, 10000, 1500],
        "year": 2018
    },
    {
        "year": 2001,
        "color": "black",
        "price": 5000,
    },
    {
        "year": 2001,
        "color": "blue",
        "price": 1234,
    },

]
#
#
# for car in list1:
#     if car["color"] == "blue":
#         print(car["price"])
#
#
#
#
# cars_dict = {
#     1: car1,
#     2: car2
# }

# print(car1["year"])
#
# print(car2["price"])
#
#
# print(cars_dict[1])
#
#
#
#
#
#

my_bank = {

}













