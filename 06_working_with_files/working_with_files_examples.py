# how to open files
# f = open(".\\names.txt", mode="r")

# f.read returns the file
# print(f.read())
# tochen_shel_hakovets = f.read(15)
# print(tochen_shel_hakovets)

# f remembers where it left off
# print(f.read(3))
# print(f.read(3))
# print(f.read(3))

#############################################3

# print(f.readline())
# print(f.read(4))
# print(f.readline())

# print(f.readlines())

# for line in f.readlines():
#     print(f'Hello {line}!')

# f.readline()

#########################
# f = open(".\\names.txt", mode="r")
#
# for line in f:
#     print(line)

#########################


# f.close()


#########################
# r - opens in read only mode
# w - dores the file (if the file doesnt exist, it will create it) and opens as writable
# a - not dores and whatever we write, appends to the end of the file
# x - does same as W, but throw an error if file exists
#########################
# f_read = open("names.txt", mode="r")
# if there is \n at the end, then elad\n
# else \nelad\n


# f.writelines("elad\n")

# f.write("my name is ariel")


# f.close()


# x:

for i in range(10):

    f = open(f"names{i}.txt", mode="a")

    f.write("""
ariel
yaniv
shir
yaniv
    """)

    f.close()

