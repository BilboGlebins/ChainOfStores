pragma solidity >=0.7.0 <0.9.0;
pragma experimental ABIEncoderV2;

contract RemakeChainOfStores{

    struct Shop{
        uint IndexShop; // Index starts from 0
        string NameShop;
        address AddressSeller;
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
        string LastName;
        string FirstName;
        string MiddleName;
        string City;
        uint Balance;
        bool isExist;
    }

    mapping (address => User) public users;
    mapping (uint => Shop) public shops;
    mapping (uint => Product) public products;

    address[] reg;

    Product[] prod;
    Shop[] shopss;

    address[] requestaddress;
    uint[] requstrole;

    mapping (address => uint) public requestroles;

    constructor(){
        shopss.push(shops[0] = Shop(0, "test1", 0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2));
        shopss.push(shops[1] = Shop(1, "test2", 0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2));
        shopss.push(shops[2] = Shop(2, "test3", 0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2));
        shopss.push(shops[3] = Shop(3, "test4", 0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2));

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

        users[0x5B38Da6a701c568545dCfcB03FcB875f56beddC4] = User(0, "testA", keccak256(abi.encodePacked("testA")), "testA", "testA", "testA", "testA", 1000, true);
        users[0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2] = User(1, "testS", keccak256(abi.encodePacked("testS")), "testS", "testS", "testS", "testS", 1000, true);
        users[0x4B20993Bc481177ec7E8f571ceCaE8A9e22C02db] = User(2, "testC", keccak256(abi.encodePacked("testC")), "testC", "testC", "testC","testC", 1000, true);
    }

    //General functions

    function pushNewUser(uint Role, string memory Login, string memory Password, string memory LastName, string memory FirstName, string memory MiddleName, string memory City) public{
        require(users[msg.sender].isExist == false, "User not exist");
        users[msg.sender]=User(
            Role,
            Login,
            keccak256(abi.encodePacked(Password)),
            LastName,
            FirstName,
            MiddleName,
            City,
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

    function getLogin() public view returns(string memory){
        return users[msg.sender].Login;
    }

    function getFullName() public view returns(string memory, string memory, string memory){
        return (users[msg.sender].LastName, users[msg.sender].FirstName, users[msg.sender].MiddleName);
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

    function pushNewAdmin(string memory Login, string memory Password, string memory LastName, string memory FirstName, string memory MiddleName, string memory City) public{
        require(users[msg.sender].Role == 0, "User is not admin");
        users[msg.sender]=User(
            0,
            Login,
            keccak256(abi.encodePacked(Password)),
            LastName,
            FirstName,
            MiddleName,
            City,
            1000,
            true
        );
    }

    function getRequst() public view returns(address[] memory, uint[] memory){
        require(users[msg.sender].Role == 0, "User is not admin");
        return (requestaddress, requstrole);
    }

    //function getSeller(uint IndexShop) public view returns(){
    //    if(shops[IndexShop].AddressSeller == msg.sender){
        
    //    }
    //}

    //function getAdmin() public view returns(address[] memory){
    //    require(users[msg.sender].Role == 0, "User is not admin");

    //}

    //Seller functions

    function requestSellerToAdmin() public returns(bool){
        require(users[msg.sender].Role == 1, "User is not seller");
        requestroles[msg.sender] = 1;
        requestaddress.push(msg.sender);
        requstrole.push(2);

        return true;
    }

    function getCity() public view returns(string memory){
        return users[msg.sender].City;
    }

    //function getShop() public view returns(string memory){
    //    if(shops[].AddressSeller == msg.sender){
            
    //    }
    //}

    //Customer functions

    function requestCustomerrToAdmin() public returns(bool){
        require(users[msg.sender].Role == 2, "User is not customer");
        requestroles[msg.sender] = 2;
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
