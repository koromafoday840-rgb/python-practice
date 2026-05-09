def update_balance(current_balance: float, deposit_amount: float) -> float:
    if deposit_amount <= 0:
        print("Invalid deposit")
    else:
        new_balance = current_balance + deposit_amount
    return new_balance

def update_new_balance(new_balance: float, withdrawal_amount: float) -> float:
    if withdrawal_amount <= 0:
        print("Invalid withdrawal")
        return new_balance
    else:
        updated_amount = new_balance - withdrawal_amount
    return updated_amount

def summarize_transaction():
    current_balance = 1000
    deposit = 500
    