
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

def initialize_tracking_structures():
    total_deposit: float = 0.0
    total_withdrawal: float = 0.0
    account_balances: dict[str, float] = {}
    negative_account_balances: list[str] = []
    return(
        total_deposit,
        total_withdrawal,
        account_balances,
        negative_account_balances
    )

def process_transaction(transaction, account_balances):
    transaction_id, account_id, transaction_type, amount = transaction
    account_balances.setdefault(account_id, 0.0)
    if transaction_type == "deposit":
        account_balanes[account_id] += amount
    elif transaction_type == "withdrawal":
        account_balances[account_id] -= amount
    return account_balances

    
def detect_risk(negative_account_balances: dict[str, float]) ->list[str]:
    negative_account_balances: list[str] = []
    for account_id, balance in negative_account_balances.items():
        if balance < 0:
            negative_account_balances.append(account_id)
        return negative_account_balances


    
def summarize_transactions(transactions):
    for transaction in transactions:
        if transaction_type == "deposit":
            total_deposit += amount
        elif transaction_type == "withdrawal":
            total_withdrawal += amount















    
    


