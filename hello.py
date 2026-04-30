
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

transaction_id = transactions[0]
account = transactions[1]
transaction_type = transactions[2]
amount = transactions[3]

def initialize_account(variables):
    deposit_total: float = 0.0
    withdrawal_total: float = 0.0
    account_balances: dict[str, float] = {}
    negative_account_balances: list[str, float] = []
    suspious_account: list[str] = []
    withdrawal_count_per_account: dict[str, int] = {}
    total_transactions: int = 0

    def update_account_balances(account: str, amount: float):
        account_balances.setdefault(account, 0.0)
        if transaction_type == "deposit":
            account_balances[account] += amount
        elif transaction_type == "withdrawal":
            account_balances[account] -= amount

    def detect_large_transactions(account: float):
        if account_balances[account] < 0:
            negative_account_balances.append(account)

    def update_totals(transaction_type: str):
        if transaction_type == "deposit":
            deposit_total += amount
        elif transaction_type == "withdrawal":
            withdrawal_total += amount
        
















    
    


