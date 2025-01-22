# [client_first_name, client_last_name, user_gov_id, balance]
#       0                     1              2         3

# bank_clients_dict_format = {
#     "user_id": str,
#     "fisrt_name": str,
#     "last_name": str,
#     "balance": float
# }

list_of_clients = [
    {"user_id": "124124135", "balance": 500, "first_name": "Hezi", "last_name": "Cohen"},
    {"user_id": "322833344", "first_name": "Ariel", "last_name": "Agranovich", "balance": 500},
    {"user_id": "444444444", "first_name": "Yedidiah", "last_name": "tzur", "balance": 100},
]

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


def return_balance(user_gov_id: str):
    for client_account in list_of_clients:
        if client_account["user_id"] == user_gov_id:
            return client_account["balance"]


def greet_client(user_gov_id: str):
    for client_account in list_of_clients:
        if client_account["user_id"] == user_gov_id:
            print(f"Welcome back {client_account['first_name']}!")


# Write a function that will deposit money to the account of the user
def deposit_to_account(user_gov_id: str, amount: float):
    pass


# Write a function that will withdraw money from the account of the user
def withdraw_from_account(user_gov_id: str, amount: float):
    pass


# Write a function that will transfer money from one account to another
# IMPORTANT: check if the user has enough money
def transfer_money(from_user_gov_id: str, to_user_gov_id: str, amount: float):
    pass


# Write a function that will add a new client to the bank
# IMPORTANT: check if the user is already in the bank
def add_new_client(user_gov_id: str, first_name: str, last_name: str, balance: float):
    pass
