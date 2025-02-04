
def devisible_by_7(num: int) -> bool:
    try:
        if num % 7 == 0:
            return True
        else:
            return False
    except TypeError:
        raise TypeError(f"There was an error with the input '{num}'. Please input a valid integer.")

print(devisible_by_7([1, 5, 2, 8]))


# devisible_by_7("asfasf")
# region explanation
# print("14".isdigit())
#
# int("14")

# if ... # + 0.2 seconds
#     pass # + 0.2 seconds
#
# try: # 0.01 seconds
#     pass

# except: # + 1 second
#     pass
# endregion

def contains_7(num: int) -> bool:
#     # 1
#     for digit in str(num):
#         # if int(digit) == 7
#         if digit == "7":
#             return True
#     return False

#     # 2
    if "7" in str(num):
        return True
    else:
        return False





#
# def contains_a_specific_number(specific_number: int, num: int) -> bool:
#     if str(specific_number) in str(num):
#         return True
#     else:
#         return False


# def error_example():



# if __name__ == '__main__':
    # print(contains_a_specific_number(specific_number=116, num=778197123511))
#     print(f"The number 18 is devisible by 7 - {devisible_by_7("7")}")
#
#     print(f"The number 21 is devisible by 7 - {devisible_by_7(21)}")
#
#     print(f"The number 77 is devisible by 7 - {devisible_by_7(77)}")
#
#     print(f"The number 40 contains 7 - {contains_7(40)}")
#
#     print(f"The number 882412490907 contains 7 - {contains_7(882412490907)}")
#
#     print(f"The number 6325290942 contains 7 - {contains_7(6325290942)}")
#
#
#
# # AttributeError
# # TypeError
# # IndentationError
# # ZeroDivisionError




