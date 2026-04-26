
transactions: list[tuple[str, str, str, float]] = [
("TNX001", "ACC100", "deposit", 450.4),
("TNX002", "ACC200", "deposit", 345.6),
("TNX003", "ACC300", "deposit", 6345.2),
("TNX004", "ACC100", "withdrawal", 145.5),
("TNX005", "ACC200", "withdrawal", 753.8),
("TNX006", "ACC400", "deposit", 2345.9),
("TNX007", "ACC500", "deposit", 536.8),
("TNX008", "ACC400", "withdrawal", 324.9),
("TNX009", "ACC500", "withdrawal", 456.3),
("TNX010", "ACC600", "deposit", 756.9),
("TNX011", "ACC600", "withdrawal", 964.8)
]

def summarize_financial_transactions(transactions):
    total_transactions:int = 0
    total_withdrawal_amount: float = 0.0
    total_deposit_amount: float = 0.0
    account_balances: dict[str, float] = {}
    negative_balance_accounts: list[str] = []
    total_transactions = len(transactions)
    for transaction in transactions:
        transaction_id, account, transaction_type, amount = transaction
        account_balances.setdefault(account, 0.0)
        if transaction_type == "deposit":
            account_balances[account] += amount
            total_deposit_amount += amount
        elif transaction_type == "withdrawal":
            account_balances[account] -= amount
            total_withdrawal_amount += amount
        if account_balances[account] < 0:
            if account not in negative_balance_accounts:
                negative_balance_accounts.append(account)
    return(
         total_transactions,
         total_deposit_amount,
         total_withdrawal_amount,
         account_balances,
         negative_balance_accounts 

    )
results = summarize_financial_transactions(transactions)
print(results)
















    
    



