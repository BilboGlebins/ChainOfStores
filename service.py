buff_user_address = ''
buff_user_data = ''

contract_address = '0xf522Ffb04DBE718D9b77acB76b2Cef81847367c0'

abi = [
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "IndexProduct",
				"type": "uint256"
			}
		],
		"name": "buyProduct",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
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
		"name": "lowerSelerBeforeCoustomer",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "Login",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "Password",
				"type": "string"
			}
		],
		"name": "pushNewAdmin",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "Role",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "Login",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "Password",
				"type": "string"
			}
		],
		"name": "pushNewUser",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "requestCustomerrToAdmin",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "requestSellerToAdmin",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "IndexProduct",
				"type": "uint256"
			}
		],
		"name": "returnProduct",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
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
		"name": "riseCustomeBeforeSeller",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "Password",
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
	},
	{
		"inputs": [],
		"name": "getProduct",
		"outputs": [
			{
				"components": [
					{
						"internalType": "uint256",
						"name": "IndexProduct",
						"type": "uint256"
					},
					{
						"internalType": "string",
						"name": "NameProduct",
						"type": "string"
					},
					{
						"internalType": "uint256",
						"name": "PriceProduct",
						"type": "uint256"
					},
					{
						"internalType": "uint256",
						"name": "IndexShop",
						"type": "uint256"
					}
				],
				"internalType": "struct RemakeChainOfStores.Product[]",
				"name": "",
				"type": "tuple[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "getShop",
		"outputs": [
			{
				"components": [
					{
						"internalType": "uint256",
						"name": "IndexShop",
						"type": "uint256"
					},
					{
						"internalType": "string",
						"name": "NameShop",
						"type": "string"
					}
				],
				"internalType": "struct RemakeChainOfStores.Shop[]",
				"name": "",
				"type": "tuple[]"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "products",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "IndexProduct",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "NameProduct",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "PriceProduct",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "IndexShop",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"name": "requestrole",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "shops",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "IndexShop",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "NameShop",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"name": "users",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "Role",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "Login",
				"type": "string"
			},
			{
				"internalType": "bytes32",
				"name": "Password",
				"type": "bytes32"
			},
			{
				"internalType": "uint256",
				"name": "Balance",
				"type": "uint256"
			},
			{
				"internalType": "bool",
				"name": "isExist",
				"type": "bool"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [],
		"name": "ViewBalance",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"stateMutability": "view",
		"type": "function"
	}
]
