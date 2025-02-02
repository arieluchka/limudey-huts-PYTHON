my_favorite_even_number = [2, 4, 6, 10, 12, 14, 16]

def is_even(user_num: int):
    if (user_num % 2) == 0:
        return True
    else:
        return False


def main():
    print("welcome to the even number tester!")
    while True:
        user_num = int(input("choose a number "))
        res = is_even(user_num=user_num)
        if res:
            print("Your number is Even!")
        else:
            print("The number is odd!")



if __name__ == '__main__':
    print("hello")
    print("This is an even number tester!")
    print(f"Ariels favorite even numbers are {my_favorite_even_number}")
    main()
