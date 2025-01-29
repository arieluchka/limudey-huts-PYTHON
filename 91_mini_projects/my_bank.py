# [client_first_name, client_last_name, user_gov_id, balance]
#       0                     1              2         3

# bank_clients_dict_format = {
#     "user_id": str,
#     "fisrt_name": str,
#     "last_name": str,
#     "balance": float
# }

def get_clients_list_from_file(client_file):
    client_file = open(client_file, mode="r")
    list_of_clients_from_file = []

    for line in client_file.readlines():
        client_dict = {}
        stripped_line = line.strip("\n")
        zoogot = stripped_line.split(",")

        for zoog in zoogot:
            seperated_zoog = zoog.split(":")
            if seperated_zoog[0] == "balance":
                client_dict[seperated_zoog[0]] = float(seperated_zoog[1])
            else:
                client_dict[seperated_zoog[0]] = seperated_zoog[1]

        list_of_clients_from_file.append(client_dict)
    client_file.close()
    return list_of_clients_from_file


list_of_clients = get_clients_list_from_file(client_file=".\\client_list.txt")
# print(list_of_clients)

# list_of_clients = [
#     ["Hezi", "Cohen", "124124135", 500],
#     ["Ariel", "Agranovich", "123123123", 500],
#     ["Yedidiah", "tzur", "444444444", 100],
#     ["Yaniv", "Rauper", "123456789", 1000],
#     ["111111111", "Shir Sheli", "Eliasi", 100000000],
# ]



# list_of_clients[0][0] = "Kobi"
# print(list_of_clients)

# print(list_of_clients)
# print(list_of_clients)
# user_bank_account = list_of_clients[1]

# 1) create a function, that will return the balance of the user, by user_gov_id


def return_client_by_id(user_gov_id: str):
    for client_account in list_of_clients:
        if client_account["user_id"] == user_gov_id:
            return client_account


def return_balance(user_gov_id: str):
    client_account = return_client_by_id(user_gov_id=user_gov_id)
    return client_account["balance"]


def greet_client(user_gov_id: str):
    client_account = return_client_by_id(user_gov_id=user_gov_id)
    first_name = client_account.get("first_name", "<USER>")

    print(f"Welcome back {first_name}!")


# Write a function that will deposit money to the account of the user
def deposit_to_account(user_gov_id: str, amount: float):
    client = return_client_by_id(user_gov_id=user_gov_id)
    client["balance"] += amount
    return client


# Write a function that will withdraw money from the account of the user
def withdraw_from_account(user_gov_id: str, amount: float):
    client = return_client_by_id(user_gov_id=user_gov_id)
    client["balance"] -= amount
    return client


# Write a function that will transfer money from one account to another
# IMPORTANT: check if the user has enough money
def transfer_money(from_user_gov_id: str, to_user_gov_id: str, amount: float):
    if return_balance(from_user_gov_id) < amount:
        print(f"The account with the id {from_user_gov_id} doesn't have sufficient funds")
        return
    else:
        withdraw_from_account(user_gov_id=from_user_gov_id, amount=amount)
        deposit_to_account(user_gov_id=to_user_gov_id, amount=amount)
        return


# Write a function that will add a new client to the bank
# IMPORTANT: check if the user is already in the bank
def add_new_client(user_gov_id: str, first_name: str, last_name: str, balance: float):
    pass

# 1) get the user id
# 2) greet client
# 3) see balance

option_list="""
1) See balance
2) Deposit to account
3) Withdraw from account
4) Transfer money to another account
5) log out
"""

# x = 6
#
#
# if x == 6:
#     y = 10
#
# print(y + 3)
#
#
#







def main():
    user_id = input("Please enter your gov ID: ")

    greet_client(user_gov_id=user_id)




    while True:
        print(option_list)
        user_choice = input("Enter here: ")
        if user_choice == "1":
            balance = return_balance(user_gov_id=user_id)
            print(f"Your balance is {balance}₪")
        elif user_choice == "2":
            deposit_amount = float(input("How much do you want to deposit? "))
            deposit_to_account(user_gov_id=user_id, amount=deposit_amount)
            print(f"{deposit_amount} has been successfully deposited into your account.")
            print(f"Your new balance is: {return_balance(user_gov_id=user_id)}")
        elif user_choice == "3":
            pass
        elif user_choice == "4":
            pass
        elif user_choice == "5":
            print("Goodbye!")
            return
        else:
            print("Please choose a valid option!")

main()




# Validate the user input, and if it's 1, run the show_balance function, if 2, run deposit function.





# verify user exists




# list_of_clients = [
#     {"user_id": "124124135", "balance": 500, "first_name": "Hezi", "last_name": "Cohen"},
#     {"user_id": "322833344", "first_name": "Ariel", "last_name": "Agranovich", "balance": 500},
#     {"user_id": "444444444", "first_name": "Yedidiah", "last_name": "tzur", "balance": 100},
#     {"user_id": "515212521", "balance": 5000}
# ]

# Work with single client every time (dont fetch all clients)

# Good example of .items() method
# client_list.txt\
def write_clients_list_to_file():
    """This is a function that writes the list into a text file."""
    client_file = open(".\\client_list.txt", mode="w")

    for client in list_of_clients:
        line = ""
        for zoog in client.items():
            line += f"{zoog[0]}:{zoog[1]},"

        line = line.strip(",")
        client_file.write(line)
        client_file.write("\n")

    client_file.close()

write_clients_list_to_file()
# .split()
# .strip()
# create a function that opens the bank clients file and returns the list of clients





with open("client_list.txt", mode="r") as client_file:
    client_file.readlines()
    client_file.read()





print("hello")










def get_specific_client_info_from_file():
    pass
write_clients_list_to_file()

# write_clients_list_to_file()
# get_clients_list_from_file()









