
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
# This function initializes the empty variables that will be updated by the main function.
def initialze_tracking_structures():
    total_deposit: float = 0.0
    total_withdrawal: float = 0.0
    account_balances: dict[str, float] = {}
    negative_account_balance: list[str] = []

def process_transactions(transaction, account_balances):
    transaction_id, account, transaction_type, amount = transaction
    account_balances.setdefault(account, 0.0)
    if transaction_type == "deposit":
        account_balances += amount
        total_deposit += amount
    elif transaction_type == "withdrawal":
        account_balances -= amount
        total_withdrawal += amount

# This function detects accounts whose balances are negative; it helps
# detects fraud and bank overdraft.
def detect_risk(account, account_balances):
    if account_balances[account] < 0:
        negative_account_balance.append(account)











    
    


