# Define a dictionary of user account information
user_accounts = {
    "1111": {"name": "Isro", "balance": 1000},
    "2222": {"name": "sam", "balance": 500},
    "3333": {"name": "osama", "balance": 2000},
}

# Define a list of valid ATM PINs
valid_pins = ["1111", "2222", "3333"]

# Define a function to validate a PIN
def validate_pin(pin):
    return pin in valid_pins

# Define a function to display the user's account balance
def display_balance(account):
    print("Your current balance is %d" %(account['balance']))

# Define a function to withdraw money from the user's account
def withdraw(account, amount):
    if amount > account["balance"]:
        print("Insufficient funds")
    else:
        account["balance"] -= amount
        print(f"Withdrawal of {amount} successful")
        

# Define a function to deposit money into the user's account
def deposit(account, amount):
    account["balance"] += amount
    print(f"Deposit of {amount} successful")

# Main program loop
while True:
    # Prompt the user to enter their PIN
    pin = input("Enter your PIN: ")

    # Validate the PIN
    if not validate_pin(pin):
        print("Invalid PIN")
        continue

    # Get the user's account information
    account = user_accounts[pin]

    # Display the user's account balance
    display_balance(account)

    # Prompt the user to select an action
    action = input("Select an action (1=withdraw, 2=deposit, 3=quit): ")

    # Process the user's selected action
    if action == "1":
        amount = float(input("Enter the amount to withdraw: "))
        withdraw(account, amount)
        print("your balance is %d now" %(account['balance']))
    elif action == "2":
        amount = float(input("Enter the amount to deposit: "))
        deposit(account, amount)
        print("your balance is %d now" %(account['balance']))
    elif action == "3":
        break
    else:
        print("Invalid action")