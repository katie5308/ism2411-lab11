# customers.py
 # Reflection 1:
# I would use .get() if I am not sure a key is there because it helps
# stop errors. I would use brackets if I know the key is there and
# want to get its information. 
#
# Reflection 2:
# This reminds me of using Excel to organize and add up information.
# Python is better for bigger amounts of data because it can do the
# work faster and automatically instead of doing everything by hand.
print("---Exercise 1 ---")
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])


print("---Exercise 2 ---")
customer["phone"] = "813-555-0142"

print(customer)
customer["tier"] = "platinum"

print(customer)
del customer["email"]

print(customer)

print(customer.get("email", "Email not found"))


print("---Exercise 3 ---")

print(customer.get("email", "no email on file "))

try:
    print(customer["email"])
except KeyError as error:
    print(f"Key not found: {error}")

print("---Exercise 4 ---")
for key, value in customer.items():
    print(f"Key: {key}, Value: {value}")

for item in customer:
    print(item)

print("---Exercise 5 ---")
tier_discounts = {"bronze": 0,
                  "silver": 0.05,
                  "gold": 0.1,
                  "platinum": 0.15}
purchase_amount = 200
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase_amount * (1 - discount_rate)

print(f"Tier: {customer['tier']}")
print(f"Discount Rate: {discount_rate * 100:.0f}%")
print(f"Final Price: {final_price:.2f}")

print("---Exercise 6 ---")
customers = [
    {"name": "Carol", "tier": "gold", "ytd_spend": 8750},
    {"name": "Bob", "tier": "silver", "ytd_spend": 3200},
    {"name": "David", "tier": "bronze", "ytd_spend": 450}
]
for record in customers:
    rate = tier_discounts.get(record["tier"], 0)
    discount = 300 * rate
    print(f"Customer: {record['name']}, Tier: {record['tier']}, Discount: {discount:.2f}")

print("---Exercise 7 ---")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Widget B": {"price": 49.99, "stock": 8}
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK ALERT: {product} has only {details['stock']} units left in stock.")

print("---Exercise 8 ---")
transactions = [
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 300},
    {"region": "South", "amount": 200},
]
sales_by_region = {}
for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]
    sales_by_region[region] = sales_by_region.get(region, 0) + amount

for region, total_sales in sales_by_region.items():
    print(f"Total sales for {region}: {total_sales}")

