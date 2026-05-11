def update_balance(current_balance: float, deposit_amount: float) -> float:
    if deposit_amount <= 0:
        print("Invalid deposit")
        return current_balance
    else:
        return current_balance + deposit_amount

def update_new_balance(new_balance: float, withdrawal_amount: float) -> float:
    if withdrawal_amount <= 0:
        print("Invalid withdrawal")
        return new_balance
    
    elif withdrawal_amount > new_balance:
        print("Insufficient funds")
        return new_balance
    return new_balance - withdrawal_amount

def summarize_transaction():
    current_balance = 1000
    deposit = 500
    withdrawal_amount = 300
    current_balance = update_balance(current_balance, deposit)
    current_balance = update_new_balance(current_balance, withdrawal_amount)
    print(current_balance)
   
summarize_transaction()
    