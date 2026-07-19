import pandas as pd
from datetime import datetime
orders = pd.read_csv("data/cleaned/orders_clean.csv")
order_items = pd.read_csv("data/cleaned/order_items_clean.csv")

def test_invalid_order_id():
    print("\nTest 1: Invalid Order ID")

    valid_orders = set(orders["order_id"])

    invalid = order_items[
        ~order_items["order_id"].isin(valid_orders)
    ]

    if invalid.empty:
        print("PASS: No invalid order IDs found.")
    else:
        print("FAIL: Invalid order IDs detected.")
        print(invalid)

def test_discount():
    print("\nTest 2: Discount Greater Than 100")

    invalid = order_items[
        order_items["discount_percent"] > 100
    ]

    if invalid.empty:
        print("PASS: No invalid discounts found.")
    else:
        print("FAIL: Invalid discounts detected.")
        print(invalid)

def test_zero_quantity():
    print("\nTest 3: Zero Quantity")

    invalid = order_items[
        order_items["quantity"] == 0
    ]

    if invalid.empty:
        print("PASS: No zero quantities found.")
    else:
        print("FAIL: Zero quantity records detected.")
        print(invalid)

def test_future_date():
    print("\nTest 4: Future Order Date")

    orders["order_date"] = pd.to_datetime(
        orders["order_date"],
        errors="coerce"
    )

    today = datetime.today()

    future = orders[
        orders["order_date"] > today
    ]

    if future.empty:
        print("PASS: No future dates found.")
    else:
        print("FAIL: Future order dates detected.")
        print(future)
if __name__ == "__main__":

    print("=" * 50)
    print("Running Edge Case Tests")
    print("=" * 50)

    test_invalid_order_id()
    test_discount()
    test_zero_quantity()
    test_future_date()

    print("\nAll edge case tests completed.")