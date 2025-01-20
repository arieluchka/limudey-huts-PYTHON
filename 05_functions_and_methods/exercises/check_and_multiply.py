# Create a function that receives a string. it checks how many times the letter "k" is present
# and returns it.
# then multiply the result by 5 and print it.
#
# mila = "saglkjrlgsgrgkkkk"
# mila = "hello my name is kandis"
# mila = "koka kola"
#
# mila = "kikoklk,kmkj"

# num_of_k = 0
# for ot in mila:
#     if ot == "k":
#         num_of_k = num_of_k + 1
#         # num_of_k += 1  <- another option
# print(num_of_k)
#

def how_many_k(mila):
    num_of_k = 0
    for ot in mila:
        if ot == "k":
            num_of_k = num_of_k + 1
            # num_of_k += 1  <- another option
    return num_of_k


# print()
# print(how_many_k(mila="kikoklk,kmkj"))
# print(how_many_k(mila="hello my name is kandis"))
# how_many_k(mila="saglkjrlgsgrgkkkk")
#
res = how_many_k(mila="koka kola")
print(res * 5)