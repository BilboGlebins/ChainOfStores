
from web3 import Web3

import contract_info

w3 = Web3

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))
print("Статус подключения:", w3.isConnected())
print()

contract = w3.eth.contract(address=contract_info.contract_address,
                           abi=contract_info.abi)

print("Список адресов в системе:")
for address in w3.eth._get_accounts():
    print(address)

print()
print("Добавление пользователей")
buff_ans = 1
while buff_ans == 1:

    print("1 - Администратор / 2 - Продавец / 3 - Покупатель")
    address = input("Введите адрес: ")
    role= int(input("Введите роль: "))
    lastname=input("Введите фамилию: ")
    firstname=input("Введите имя: ")
    middlename=input("Введите отчество: ")
    password = input("Введите пароль: ")
    balance=int(input("Введите баланс: "))

    contract.functions.pushNewUser(role, lastname, firstname, middlename, password, balance).transact({'from': address})

    print("Хотите довавить еще одного пользователя?")
    print("Да - 1 / Нет - 0")

    buff_ans=int(input())

    if buff_ans == 0:
        break




print()
buff_choice = True
while buff_choice:

    choice_function=input("Введите номер выбранной функции: ")

    if choice_function == 1:
        print("Проверка авторизации в системе")
        address = input("Введите адрес: ")
        print("Статус авторизации: ", contract.functions.autUser(password).call({'from': address}))
    #if choice_function == 2:

#contract.functions.upBeforeCustomer().call({'from': address})


