import pandas as pd
import random
import datetime

# Generate random transactions
def generate_transactions(num_transactions):
    senders = [f"U{random.randint(100, 999)}" for _ in range(num_transactions)]
    receivers = [f"U{random.randint(100, 999)}" for _ in range(num_transactions)]
    amounts = [random.randint(100, 20000) for _ in range(num_transactions)]
    timestamps = [
        datetime.datetime(2023, 1, 1) + datetime.timedelta(days=random.randint(0, 365))
        for _ in range(num_transactions)
    ]
    return pd.DataFrame(
        {"sender": senders, "receiver": receivers, "amount": amounts, "time": timestamps}
    )

# Save to CSV
data = generate_transactions(1000)
data.to_csv("data/raw/generated_transactions.csv", index=False)
print("Generated transactions saved to 'data/raw/generated_transactions.csv'.")
