Python Bank Account Simulator

A simple Python project that simulates Banking Operations with Object Oriented Programming.
The program uses a class to generate instances of a bank account with operations like deposit, withdrawal, and check balance.

Features

Create Banking Accounts with account holder and balance.
Deposit amount in a bank account.
Withdraw money from the bank account.
Check the balance of the account.
Restricted negative values for deposits and withdrawals.
Restricted withdrawals greater than the available balance.
Create multiple objects for the bank account.

Technologies

Python
Object Oriented Programming.
OOP Concepts

The following concepts of OOP were used in this project:

Classes

Objects

Constructor ( __init__ )

Attributes

Methods

Conditional Flow Control

Validation of deposits and withdrawals.

Implementation

The BankAccount class was used to create objects (instances) of the class.

Each object created is a bank account with an account holder and an optional balance.

The deposit() method was used to add funds to the account.

The withdraw() method was used to deduct funds from the account if the withdrawal amount is positive and less than the account balance.

The check_balance() method displays the account holder and the balance.

The program shows how the methods can be used to perform banking operations.

The code below shows how it was done:

Project Structure

python-bank-account-simulator/

└── Bank System(class fun).py

How to Use

Ensure that Python is installed in your system.

Clone the repository to your local device.

Open the terminal in the project folder.

Run the following command:

python "Bank System(class fun).py"

You will see the following output in your terminal:

.............Banking Operation...............

New Account Created Successfully for Gamer with 1000 Balance...

500 was Deposited Successfully
300 withdrawl succesfully, Account balance is 1200
Insufficient Balance, Current Balance : 1200
Account Holder: Gamer, Account Balance : 1200

The above output shows the possible operations, although the format may be different.

What I learned
From this project, I learned how to:

Use classes and objects in Python.
Create objects using a constructor.
Create methods that perform actions on an object.
Store information specific to each object.
Use conditional statements.
Validate deposits and withdrawals.
Learn about banking operations.

Background
I created this project during my study of python to develop my understanding of OOP further.

Future Improvements

The following future improvements can be added to this project:
Add a menu to the application so that the user can choose what to do.
Accept user input to dynamically generate account details instead of hard-coding it.
Allow multiple accounts to be stored in a list or a dictionary.
Add a history of transactions.
Validate all user inputs.
Add a feature that allows account holders transfer money from one account to another.
Security Warning

The project is just a simple simulation and should not be used for any application that requires secure transactions.

Author

This project was created as part of my Python learning journey.
