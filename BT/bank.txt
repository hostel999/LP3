// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract BankAccount {
    mapping(address => uint256) private balances;

    // Deposit money into the bank account
    function deposit() public payable {
        require(msg.value > 0, "Deposit must be greater than zero");
        balances[msg.sender] += msg.value;
    }

    // Withdraw money from the bank account
    function withdraw(uint256 amount) public {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");
        balances[msg.sender] -= amount;
        payable(msg.sender).transfer(amount);
    }

    // Show balance of the caller
    function showBalance() public view returns (uint256) {
        return balances[msg.sender];
    }
}
