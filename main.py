import json
import os

# Define the path to the data file
DATA_FILE = 'bank_data.json'

# Function to load bank data from the file
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

# Function to save bank data to the file
def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

# Function to register a new user
def register(data):
    username = input("Enter username: ")
    if username in data:
        print("Username already exists.\n")
        return data
    password = input("Enter password: ")
    data[username] = {
        "password": password,
        "balance": 0.0,
        "transactions": []
    }
    save_data(data)
    print("User registered successfully.\n")
    return data

# Function to login
def login(data):
    username = input("Enter username: ")
    if username not in data:
        print("Username not found.\n")
        return None
    password = input("Enter password: ")
    if data[username]["password"] != password:
        print("Incorrect password.\n")
        return None
    print("Login successful.\n")
    return username

# Function to withdraw money
def withdraw(data, username):
    amount = float(input("Enter amount to withdraw: "))
    if data[username]["balance"] >= amount:
        data[username]["balance"] -= amount
        data[username]["transactions"].append(f"Withdrew ${amount}")
        save_data(data)
        print("Withdrawal successful.\n")
    else:
        print("Insufficient balance.\n")

# Function to deposit money
def deposit(data, username):
    amount = float(input("Enter amount to deposit: "))
    data[username]["balance"] += amount
    data[username]["transactions"].append(f"Deposited ${amount}")
    save_data(data)
    print("Deposit successful.\n")

# Function to display account balance
def account_balance(data, username):
    balance = data[username]["balance"]
    print(f"Account balance: ${balance}\n")

# Function to display mini statement
def mini_statement(data, username):
    print("Mini statement:")
    for transaction in data[username]["transactions"][-5:]:
        print(transaction)
    print()

# Function to display the menu
def display_menu():
    print("Bank System")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

# Function to display the user menu
def display_user_menu():
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Account Balance")
    print("4. Mini Statement")
    print("5. Logout")

# Main function
def main():
    data = load_data()

    while True:
        display_menu()
        choice = int(input("Choose an option: "))

        if choice == 1:
            data = register(data)
        elif choice == 2:
            username = login(data)
            if username:
                while True:
                    display_user_menu()
                    user_choice = int(input("Choose an option: "))
                    if user_choice == 1:
                        withdraw(data, username)
                    elif user_choice == 2:
                        deposit(data, username)
                    elif user_choice == 3:
                        account_balance(data, username)
                    elif user_choice == 4:
                        mini_statement(data, username)
                    elif user_choice == 5:
                        print("Logging out...\n")
                        break
                    else:
                        print("Invalid choice. Please try again.\n")
        elif choice == 3:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
