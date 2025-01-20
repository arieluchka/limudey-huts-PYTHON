# Create to functions
# 1) that converts a decimal number (14) to a binary one (1110) (return the binary as a string)
# 2) that converts a binary number (10101010) to a decimal (170)(return the decimal as a number)

# The functions needs to be able to handle numbers of any length!
# (Dont use the bin() function in python, you need to implement the conversion yourself)

# refer to this article, to help you convert from decimal to binary
# https://medium.com/@jamesjefferyuk/how-to-convert-decimal-to-binary-7256d7d82b07

### START YOUR CODE HERE <---------------

def to_binary(decimal_num: int) -> str:
    return # return the binary number as a string


def to_decimal(binary_num: str) -> int:
    return # return the decimal number as an integer


### DONT CHANGE THE CODE BELOW THIS LINE <---------------

# Test the functions
assert to_binary(14) == '1110', "The function to_binary(14) should return '1110'"
assert to_binary(15) == '1111', "The function to_binary(15) should return '1111'"
assert to_binary(16) == '10000', "The function to_binary(16) should return '10000'"
assert to_binary(532) == '1000010100', "The function to_binary(532) should return '1000010100'"


assert to_decimal('1110') == 14, "The function to_decimal('1110') should return 14"
assert to_decimal('11100011') == 227, "The function to_decimal('11100011') should return 227"
assert to_decimal('1000010100') == 532, "The function to_decimal('1000010100') should return 532"
assert to_decimal('101011101101') == 2797, "The function to_decimal('101011101101') should return 2797"




