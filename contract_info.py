contract_address = '0xd3ea43ea00bF3c136b21568B5Ea8dD7BB3b4C23f'

abi = [
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "indexShop",
				"type": "uint256"
			}
		],
		"name": "addProduct",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "indexShop",
				"type": "uint256"
			}
		],
		"name": "addShop",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "adr",
				"type": "address"
			}
		],
		"name": "lowerBeforeSeller",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_Role",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "_LastName",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_FirstName",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_MiddleName",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "_Password",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "_Balance",
				"type": "uint256"
			}
		],
		"name": "pushNewUser",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "requestLowerBeforeSeller",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "adr",
				"type": "address"
			}
		],
		"name": "upBeforeCustomer",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "_Password",
				"type": "string"
			}
		],
		"name": "autUser",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]