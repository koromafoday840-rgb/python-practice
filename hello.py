
transactions: list[tuple[str, str, str, float]] = [
("TNX001", "ACC100", "deposit", 450.4),
("TNX002", "ACC200", "withdrawal", 345.6),
("TNX003", "ACC300", "deposit", 6345.2),
("TNX004", "ACC100", "withdrawal", 145.5),
("TNX005", "ACC200", "deposit", 753.8),
("TNX006", "ACC400", "deposit", 2345.9),
("TNX007", "ACC500", "deposit", 536.8),
("TNX008", "ACC400", "withdrawal", 324.9),
("TNX009", "ACC500", "withdrawal", 456.3),
("TNX010", "ACC600", "deposit", 756.9),
("TNX011", "ACC600", "withdrawal", 964.8)
]
total_number_of_transactions: int = 0
total_deposit_amount: float = 0.0
total_withdrawn_amount: float = 0.0
final_balance_per_account: float = 0.0

def summarize_financial_transactions():
    total_number_of_transactions = len(transactions)
    return total_number_of_transactions
for transaction in transactions:
    if transaction == "deposit":
        total_deposit_amount += transaction[3]
        return total_deposit_amount
    elif transaction == "withdrawal":
        total_withdrawal_amount += transaction[3]
        return total_withdrawal_amount
    
    



