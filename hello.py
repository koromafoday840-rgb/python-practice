
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

def summarize_financial_trnsactions(transactions):
    total_number_of_transactions:int = 0
    total_withdrawal_amount: float = 0.0
    total_deposit_amount: float = 0.0
    account_balances: dict[str, float] = {}
    negative_balance_accounts: list[str] = []
    for transaction in transactions:
        transaction_id = transaction[0]
        account = transaction[1]
        transaction_type = transaction[2]
        amount = transaction[3]
        total_number_of_transactions = len(transaction_id)
        if transaction_type == "withdrawal":
            total_withdrawal_amount += "withdrawal"
        elif transaction_type == "deposit":
            total_deposit_amount += "deposit"
            account_balances.setdefault(account, amount = {})






    
    



