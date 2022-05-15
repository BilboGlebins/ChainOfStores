from web3 import Web3

import service
import web3.exceptions

w3 = Web3

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))

contract = w3.eth.contract(address=service.contract_address,
                           abi=service.abi)

print("Статус подключения: ", w3.isConnected())

print("Список адресов в системе: ")
for address in w3.eth._get_accounts():
    print(address)

print("Пользоваели при старте системы:")
print("Администратор: Адрес - 0x8d5168336d56Dd5ba35890a82fB30D031fe3A49f / Пароль - testA")
print("Продавец: Адрес - 0x4f1f3328f491304B2d7A3500cd092fd37a245468 / Пароль - testS")
print("Покупатель: Адрес - 0xcc3DDa53B653988b0B995710e5689872B0E7bbEd / Пароль - testC")


def auth():
    print("Авторизация")
    address = input("Введите адрес: ")
    password = input("Введите пароль: ")

    if address != '' and password != '':
        try:
            auth_user = contract.functions.autUser(password).call({'from': address})
            if auth_user:
                print("Вы авторизированны")
                service.buff_user_address = address
                service.buff_user_data = contract.functions.users(
                    service.buff_user_address).call()
                if service.buff_user_data[0] == 0:
                    admin_function()
                if service.buff_user_data[0] == 1:
                    seller_function()
                if service.buff_user_data[0] == 2:
                    customer_function()
            else:
                print("Вы не авторизированны")
                return
        except web3.exceptions.ContractLogicError as err:
            print("Ошибка: ", err)


def reg():
    while True:
        print("Регистрация")
        print("1 - Добавить нового пользователя")
        print("0 - Выход")
        buff_choice = int(input("Выберите функцию: "))
        if buff_choice == 1:
            address = input("Введите адрес: ")
            role = input("Введите роль: ")
            login = input("Введите логин: ")
            password = input("Введите пароль: ")

            if address != '' and role != '' and login != '' and password != '':
                try:
                    contract.functions.pushNewUser(role, login, password).call({'from': address})
                except web3.exceptions.ContractLogicError as err:
                    print("Ошибка: ", err)
        elif buff_choice == 0:
            break
        else:
            break


def admin_function():
    while True:
        print("Функции администратора:")
        print("1 - Повышение обычного покупателя до роли продавец")
        print("2 - Понижение продавца до роли покупатель")
        print("3 - Переключиться к роли покупатель")
        print("4 - Ввод в систему новых администраторов")
        print("0 - Выход")
        buff_choice = int(input("Выберите функцию: "))
        if buff_choice == 1:
            print("Повышение обычного покупателя до роли продавец")
            customer_address = input("Введите адрес пользователя: ")
            try:
                contract.functions.riseCustomeBeforeSeller(customer_address).call({'from': service.buff_user_address})
            except web3.exceptions.ContractLogicError as err:
                print("Ошибка: ", err)

        elif buff_choice == 2:
            print("Понижение продавца до роли покупатель")
            seller_address = input("Введите адрес продавца: ")
            try:
                contract.functions.lowerSelerBeforeCoustomer(seller_address).call({'from': service.buff_user_address})
            except web3.exceptions.ContractLogicError as err:
                print("Ошибка: ", err)

        elif buff_choice == 3:
            print("Переключиться к роли покупатель")
            customer_address = input("Ввыедите адресс покупателя: ")
            customer_password = input("Ввыедите пароль покупателя: ")
            try:
                contract.functions.autUser(customer_password).call({'from': customer_address})
            except web3.exceptions.ContractLogicError as err:
                print("Ошибка: ", err)

        elif buff_choice == 4:
            print("Ввод в систему новых администраторов")
            admin_login = input("Введите логин: ")
            admin_password = input("Введите пароль: ")
            try:
                contract.functions.pushNewAdmin(admin_login, admin_password).call({'from': service.buff_user_address})
            except web3.exceptions.ContractLogicError as err:
                print("Ошибка: ", err)

        elif buff_choice == 0:
            break
        else:
            break


def seller_function():
    while True:
        print("Функции продавца:")
        print("1 - Переключение к роли покупатель")
        print("2 - Отправка запроса на понижение до роли покупатель")
        print("3 - Подтверждение / отклонение запроса покупателя на покупку, возврат товара, оформление брака")
        print("0 - Выход")
        buff_choice = int(input("Выберите функцию: "))
        if buff_choice == 1:
            print("Переключение к роли покупатель")
            customer_address = input("Ввыедите адресс покупателя: ")
            customer_password = input("Ввыедите пароль покупателя: ")
            try:
                auth_user = contract.functions.autUser(customer_password).call({'from': customer_address})
                if auth_user:
                    print("Вы авторизированны")
                    customer_function()
            except web3.exceptions.ContractLogicError as err:
                print("Ошибка: ", err)

        elif buff_choice == 2:
            print("Отправка запроса на понижение до роли покупатель")
            try:
                contract.functions.requestSellerToAdmin().call({'from': service.buff_user_address})
            except web3.exceptions.ContractLogicError as err:
                print("Ошибка: ", err)

        elif buff_choice == 3:
            print("3 - Подтверждение / отклонение запроса покупателя на покупку, возврат товара, оформление брака")

        elif buff_choice == 0:
            break
        else:
            break


def customer_function():
    while True:
        print("Функции покупателя:")
        print("1 - Подать запрос на повышение до роли продавец.")
        print("2 - Покупка товар в магазине")
        print("3 - Возврат товар в магазин")
        print("4 - Просмотр баланса")
        print("5 - Просмотр товара")
        print("0 - Выход")
        buff_choice = int(input("Выберите функцию: "))
        if buff_choice == 1:
            print("Подать запрос на повышение до роли продавец.")
            try:
                contract.functions.requestCustomerrToAdmin().call({'from': service.buff_user_address})
            except web3.exceptions.ContractLogicError as err:
                print("Ошибка: ", err)

        elif buff_choice == 2:
            print("Покупка товар в магазине")
            index_product = int(input("Введите индекс товара: "))
            try:
                contract.functions.buyProduct(index_product).call({'from': service.buff_user_address})
            except web3.exceptions.ContractLogicError as err:
                print("Ошибка: ", err)

        elif buff_choice == 3:
            print("Возврат товар в магазин")
            index_product = int(input("Введите индекс товара: "))
            try:
                contract.functions.returnProduct(index_product).call({'from': service.buff_user_address})
            except web3.exceptions.ContractLogicError as err:
                print("Ошибка: ", err)

        elif buff_choice == 4:
            print("Просмотр баланса")
            try:
                contract.functions.ViewBalance().call({'from': service.buff_user_address})
            except web3.exceptions.ContractLogicError as err:
                print("Ошибка: ", err)

        elif buff_choice == 5:
            print("Просмотр товара")
            try:
                contract.functions.getProduct().call({'from': service.buff_user_address})
            except web3.exceptions.ContractLogicError as err:
                print("Ошибка: ", err)

        elif buff_choice == 0:
            break
        else:
            break


while True:
    print("Стартовое меню")
    print("1 - Авторизация")
    print("2 - Регистрация")
    print("0 - Выход")

    menu_choice = int(input("Выберите действие: "))

    if menu_choice == 1:
        auth()
    elif menu_choice == 2:
        reg()
    elif menu_choice == 0:
        break
    else:
        break
