import pandas as pd

visits = pd.read_csv('visits.csv', parse_dates=[1])
cart = pd.read_csv('cart.csv', parse_dates=[1])
checkout = pd.read_csv('checkout.csv', parse_dates=[1])
purchase = pd.read_csv('purchase.csv', parse_dates=[1])

#Inspect the DataFrames
print(visits.head())
print()
print(cart.head())
print()
print(checkout.head())
print()
print(purchase.head())
print()

#Combine visits and cart
visitsAndCart = pd.merge(visits, cart, how="left")
print(visitsAndCart)

#find out the number of rows
lenVisitsAndCart = len(visitsAndCart)
print(f"The number of row is: {lenVisitsAndCart}")

#count no items in cart users
nullCartTimeRows = visitsAndCart[visitsAndCart["cart_time"].isnull()]
lenNullCartTimeRows = len(nullCartTimeRows)
print(f"The count of users without any items in carts are: {lenNullCartTimeRows}")