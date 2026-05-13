def categorize_expense(amount: float)-> str:
    if amount < 50:
        return "small expense"
    elif amount < 500:
        return "medium expensive"
    else:
        return "large expense"
    
def check_budget(amount: float)-> str:
    if amount <= 300:
        return "within budget"
    else:
        return "over budget"

def cordinate_transaction()-> None:
    expenses_amount = 275
    category = categorize_expense()
    status = check_budget()
    print(category)
    print(status)

