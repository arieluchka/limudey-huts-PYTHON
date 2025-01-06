# 2 data types
# 1) sequential and non sequential

####################################################################################
# string - מחרוזת
####################################################################################

var_1 = "hello world"
#        0123456789....

var_1_2 = 'hello world'
var_1_3 = """hello world"""
var_1_4 = '''hello world'''


# we can use a combination of " and ', to print them out as well
# print("hello my name is 'ariel'")



# how to access specific characters?
print(var_1[0]) # print character on index 0
print(var_1[5]) # print character on index 5
print(var_1[2:5]) # print characters from index 2, up to index 5 (not including!)
print(var_1[:5]) # print characters from the start up to index 5 (not including!)
print(var_1[6:]) # print characters from index 6 until the end


####################################################################################
# list - רשימות
####################################################################################

var_2 = ["shalom", 2, 45, var_1]

print(var_2)


# to access specific objects in a list is very similar to how we do it with strings
print(var_2[2]) # print object in index 2


# we can also continue to get the index inside the indexed object!
print(var_2[0][5])
# var_2[0] -> "shalom"[5] -> "m"
#              012345



####################################################################################
# tuple
# דומה לרישמות אבל קצת שונה
# נלמד בהמשך
####################################################################################

var_3 = ("shalom", 2, 45, var_1)



####################################################################################
# 2) Non sequentials
# אובייקטים שלא מסודרים/מאורגנים


####################################################################################
# int (integer) - מספר שלם
####################################################################################

var_4 = 4235

print(var_4) # will still print "4235"


# we cant index ints!
#print(var_4[0]) <----- won`t work!


# we can use math operations on ints
print(5 * 3) #  = 15
print("5" * 3)# = 555



####################################################################################
# float - מספר עשרוני
####################################################################################
var_6 = 4235.6

