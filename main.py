
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

    address = input("Введите адрес: ")
    print("1 - Администратор / 2 - Продавец / 3 - Покупатель")
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
print("Доступные функции")
buff_choice = 1
while buff_choice == 1:

    print("1 - Администратор / 2 - Продавец / 3 - Покупатель")
    choice_role=int(input("Введите роль: "))

    if choice_role == 1:

        address_admin = input("Введите адрес администратора: ")
        address_password = input("Введите пароль администратора: ")
        print("Статус авторизации", contract.functions.autUser(address_password).call({'from': address_admin}))
        print()

        buff_function = 1
        while buff_function == 1:
            print("Список функций администратора:")
            print("1. Повышение покупателя до роли продавеца")
            print("2. Понижение продавца до роли покупателя")
            print("3. Добавление нового администратора")
            choice_function=int(input("Введите номер функции: "))
            print()

            if choice_function == 1:
                print("Повышение покупателя до роли продавца")
                address_customer=input("Ввидите адрес покупателя: ")
                contract.functions.upBeforeCustomer(address_customer).call({'from': address_admin})
                break
            if choice_function == 2:
                print("Понижение продавца до роли покупателя")
                address_saller=input("Ввидите адрес продавца: ")
                contract.functions.lowerBeforeSeller(address_saller).call({'from': address_admin})
                break
            if choice_function == 3:
                print("Добавление нового администратора")
                address = input("Введите адрес: ")
                role = 1
                lastname = input("Введите фамилию: ")
                firstname = input("Введите имя: ")
                middlename = input("Введите отчество: ")
                password = input("Введите пароль: ")
                balance = int(input("Введите баланс: "))
                contract.functions.pushNewUser(role, lastname, firstname, middlename, password, balance).transact({'from': address_admin})
                break

            print("Хотите выбрать другую функцию?")
            print("Да - 1 / Нет - 0")
            buff_function = int(input())
            if buff_function == 0:
                break

    #if choice_role == 2:


    #
    #if choice_role == 3:



