def deposit(num):
    """Function to handle deposit."""
    global balance
    balance += num

def withdrawal(num):
    """Function to handle withdrawal."""
    global balance
    if balance >= num:
        balance -= num
    else:
        print("Withdrawal not possible. Insufficient balance.")

# Initialize balance to 0
balance = 0

while True:
    # Take input for transactions
    data = input("Please enter the transaction details (or 'Exit' to quit): ")

    # Exit condition
    if data.lower() == 'exit':
        break

    # Split the input into parts
    transaction = data.split()

    # Check if the transaction is deposit (D) or withdrawal (W)
    if transaction[0] == 'D':
        deposit(int(transaction[1]))  # Deposit amount
    elif transaction[0] == 'W':
        withdrawal(int(transaction[1]))  # Withdrawal amount
    else:
        print("Invalid transaction type. Please use 'D' for deposit or 'W' for withdrawal.")
   
    # Print the current balance after each transaction
    print(f"Current Balance: {balance}")
