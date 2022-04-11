from web3 import Web3

import contract_info

w3 = Web3

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))
print(w3.isConnected())

#current_address = '0x35D67E42967ea35A857483dafc566D08bB25f2F5'

contract = w3.eth.contract(address=contract_info.contract_address,
                           abi=contract_info.abi)

for address in w3.eth._get_accounts():
    print(address)

contract.functions.pushNewUser(1, 'testA', 'testA', 'testA', 'Ox6407c46437f7c2a167fd59408b1109b4a186d16beee8e8ef617ac7d94159c77f', 1000).transact({'from':
'0xdDaf2CE853FA2622743094292D3a7427C882fbdB'})
#
print(contract.functions.autUser('Ox6407c46437f7c2a167fd59408b1109b4a186d16beee8e8ef617ac7d94159c77f').call())


