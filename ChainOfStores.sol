// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;
pragma experimental ABIEncoderV2;

contract ChainOfStores{

    struct User{
        uint Role;
        string LastName;
        string FirstName;
        string MiddleName;
        bytes32 Password;
        uint Balance;
        bool isExist;
    }

    struct Product{
        uint IdProduct;
        uint Price;
    }

    struct Shop{
        Product[] products;
    }

    Shop[] shops;

    mapping (address => User) private users;

    mapping (address => Shop) private shop;

    address[] reg;

    function pushNewUser (uint _Role, string memory _LastName, string memory _FirstName, string memory _MiddleName, string memory _Password, uint _Balance) public{
        require(users[msg.sender].isExist == false, "Users already exist");
        users[msg.sender] = User(
            _Role,
            _LastName,
            _FirstName,
            _MiddleName,
            keccak256(abi.encodePacked(_Password)),
            _Balance,
            true 
        );
        reg.push(msg.sender);
    }

    function autUser(string memory _Password) public view returns (bool){
        require(users[msg.sender].isExist == true, "User not exist");
        if (users[msg.sender].Password == keccak256(abi.encodePacked(_Password)))
        return true;

        return false;
    }

    function upBeforeSeller(address adr) public{
        require(users[msg.sender].Role == 1, "You are admin");
        require(users[adr].Role == 3, "You not customer");
        users[adr].Role = 2;
    } 

    function lowerBeforeCustomer(address adr) public{
        require(users[msg.sender].Role == 1, "You are admin");
        require(users[adr].Role == 2, "You not seller");
        users[adr].Role = 3;
    } 

    address[] addresse;
    uint[] roles;

    mapping (address => uint) private requestrole;

    function requestLowerBeforeSeller() public{
        require(users[msg.sender].Role != 1, "You are not admin");
        if (users[msg.sender].Role == 2){
            requestrole[msg.sender] = 2;
            addresse.push(msg.sender);
            roles.push(2);
        }
        else if (users[msg.sender].Role == 3){
            requestrole[msg.sender] = 3;
            addresse.push(msg.sender);
            roles.push(3);
        }
    }

    string[] nameproduct;

    function addShop(uint indexShop) public{
        indexShop;
        shops.push();
    }

    function addProduct(uint indexShop) public {
        if (indexShop == 0){
        shops[indexShop].products.push(Product(1, 10));
        shops[indexShop].products.push(Product(2, 11));
        shops[indexShop].products.push(Product(3, 176));
        }
        if (indexShop == 1){
        shops[indexShop].products.push(Product(4, 90));
        shops[indexShop].products.push(Product(5, 152));
        shops[indexShop].products.push(Product(6, 175));
        }

        if (indexShop == 2){
        shops[indexShop].products.push(Product(7, 74));
        shops[indexShop].products.push(Product(8, 150));
        shops[indexShop].products.push(Product(9, 462));
        }
        if (indexShop == 3){
        shops[indexShop].products.push(Product(1, 40));
        shops[indexShop].products.push(Product(2, 450));
        shops[indexShop].products.push(Product(3, 4413));
        }
    }

    //function buyProduct(uint indexShop, uint _idproduct, uint _Price, uint count) public{
    //    require(users[msg.sender].Role != 3, "You not customer");
    //    if (indexShop == 0){
    //        require(msg.value >= Product[_idproduct].Price);
    //    }
    //    if (indexShop == 1){
    //        
    //    }
    //
    //    if (indexShop == 2){
    //        
    //    }
    //    if (indexShop == 3){
    //        
    //    }
    //} 
}   
