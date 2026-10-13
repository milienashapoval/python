amount = float(input("enter the amount in hryvnas:"))
currency = input("USD | EUR:")

if currency.lower() == "usd":
 print(f"the amount of the sume in dollars: {amount / 45.10}")
elif currency.lower() == "eur":
 print(f"the amount of the sume in euros: {amount / 50.33}")