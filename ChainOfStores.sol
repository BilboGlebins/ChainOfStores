// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;
pragma experimental ABIEncoderV2;

contract ChainOfStores{

    struct Shop{
        uint IndexShop; // Index starts from 0
        string NameShop;
    }

    struct Product{
        uint IndexProduct; // Index starts from 0
        string NameProduct;
        uint PriceProduct;
        uint IndexShop;
    }

    struct User{
        uint Role; // 0 - Administrator / 1 - Seller / 2 - Customer
        string Login;
        bytes32 Password;
        uint Balance;
        bool isExist;
    }

    mapping (address => User) public users;
    mapping (uint => Shop) public shops;
    mapping (uint => Product) public products;

    address[] reg;

    Product[] prod;

    constructor(){
        shops[0] = Shop(0, "test1");
        shops[1] = Shop(1, "test2");
        shops[2] = Shop(2, "test3");
        shops[3] = Shop(3, "test4");

        prod.push(products[0] = Product(0, "test01", 1000, 0));
        prod.push(products[0] = Product(1, "test02", 1500, 0));
        prod.push(products[0] = Product(2, "test03", 100, 0));

        prod.push(products[1] = Product(3, "test11", 500, 1));
        prod.push(products[1] = Product(4, "test12", 1050, 1));
        prod.push(products[1] = Product(5, "test13", 10000, 1));

        prod.push(products[2] = Product(6, "test21", 1800, 2));
        prod.push(products[2] = Product(7, "test22", 10500, 2));
        prod.push(products[2] = Product(8, "test23", 150, 2));

        prod.push(products[3] = Product(9, "test31", 1500, 3));
        prod.push(products[3] = Product(10, "test32", 350, 3));
        prod.push(products[3] = Product(11, "test33", 250, 3));

        users[0x8d5168336d56Dd5ba35890a82fB30D031fe3A49f] = User(0, "testA", "testA", 1000 ,true);
        users[0x4f1f3328f491304B2d7A3500cd092fd37a245468] = User(1, "testS", "testS", 1000 ,true);
        users[0xcc3DDa53B653988b0B995710e5689872B0E7bbEd] = User(2, "testC", "testC", 1000 ,true);
    }

    //General functions

    function pushNewUser(uint Role, string memory Login, string memory Password) public{
        require(users[msg.sender].isExist == false, "User not exist");
        users[msg.sender]=User(
            Role,
            Login,
            keccak256(abi.encodePacked(Password)),
            1000,
            true
        );

        reg.push(msg.sender);
    } 

    function autUser(string memory Password) public view returns (bool){
        require(users[msg.sender].isExist == true, "User not exist");
        if (users[msg.sender].Password == keccak256(abi.encodePacked(Password))){
                return true;
        }
        else{
            return false;
        }
    }

    function ViewBalance() public view returns(uint){
        return users[msg.sender].Balance;
    }

    function getProduct() public view returns(Product[] memory){
        return prod;
    }

    //Administator functions

    function riseCustomeBeforeSeller(address adr) public{
        require(users[msg.sender].Role == 0, "User is not admin");
        require(users[adr].Role == 2, "User is not customer");
        users[adr].Role = 1;
    }

    function lowerSelerBeforeCoustomer(address adr) public{
        require(users[msg.sender].Role == 0, "User is not admin");
        require(users[adr].Role == 1, "User is not customer");
        users[adr].Role = 2;
    }

    function pushNewAdmin(string memory Login, string memory Password) public{
        require(users[msg.sender].Role == 0, "User is not admin");
        users[msg.sender]=User(
            0,
            Login,
            keccak256(abi.encodePacked(Password)),
            1000,
            true
        );
    }

    address[] requestaddress;
    uint[] requstrole;

    mapping (address => uint) public requestrole;

    //Seller functions

    function requestSellerToAdmin() public returns(bool){
        require(users[msg.sender].Role == 1, "User is not seller");
        requestrole[msg.sender] = 1;
        requestaddress.push(msg.sender);
        requstrole.push(2);

        return true;
    }

    //Customer functions

    function requestCustomerrToAdmin() public returns(bool){
        require(users[msg.sender].Role == 2, "User is not customer");
        requestrole[msg.sender] = 2;
        requestaddress.push(msg.sender);
        requstrole.push(1);

        return true;
    }

    function buyProduct(uint IndexProduct) public returns(bool){
        require(users[msg.sender].Role == 2, "User is not customer");
        require(users[msg.sender].Balance >= prod[IndexProduct].PriceProduct);
        users[msg.sender].Balance = users[msg.sender].Balance - prod[IndexProduct].PriceProduct;
        return true;
    }

    function returnProduct(uint IndexProduct) public returns(bool){
        require(users[msg.sender].Role == 2, "User is not customer");
        users[msg.sender].Balance = users[msg.sender].Balance + prod[IndexProduct].PriceProduct;
        return true;
    }
}
