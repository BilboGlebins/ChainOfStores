from web3 import Web3

import contract_info

w3 = Web3

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))
print(w3.isConnected())

contract = w3.eth.contract(address=contract_info.contract_address,
                           abi=contract_info.abi)

for address in w3.eth._get_accounts():
    print(address)

address = input("Введите адрес: ")
role= int(input("Введите роль: "))
lastname=input("Введите фамилию: ")
firstname=input("Введите имя: ")
middlename=input("Введите отчество: ")
password = input("Введите пароль: ")
balance=int(input("Введите баланс: "))

contract.functions.pushNewUser(role, lastname, firstname, middlename, password, balance).transact({'from': address})
#print(contract.all_functions())
print(contract.functions.autUser(password).call({'from': address}))


