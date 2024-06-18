# Bank-management

Bank System Application Description
The Bank System application . It allows users to perform banking operations such as login, registration, deposit, withdrawal, check account balance, and view mini statements.

Features:
Login and Registration:

Users can login with their username and password.
New users can register by providing a username and password. The application checks if the username already exists.
Main Menu:

Upon successful login, users are presented with a main menu.
Options include Deposit, Withdraw, Account Balance, Mini Statement, and Logout.
Deposit and Withdraw:

Users can deposit money into their account by entering an amount.
They can withdraw money, provided they have sufficient balance.
Account Operations:

Account balance can be viewed, displaying the current balance.
Mini statement shows the last 5 transactions performed.
Data Persistence:

User data (username, password, balance, transactions) is stored in a JSON file (bank_data.json).
Data is loaded at startup and saved whenever there are updates (registration, deposit, withdrawal).
