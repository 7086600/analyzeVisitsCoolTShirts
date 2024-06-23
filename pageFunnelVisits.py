import pandas as pd

visits = pd.read_csv('visits.csv', parse_dates=[1])
cart = pd.read_csv('cart.csv', parse_dates=[1])
checkout = pd.read_csv('checkout.csv', parse_dates=[1])
purchase = pd.read_csv('purchase.csv', parse_dates=[1])

#Inspect the DataFrames
print(visits.head())
print(len(visits))
print()
print(cart.head())
print(len(cart))
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
print(f"The count of users: {lenVisitsAndCart}")

#count no items in cart users
nullCartUsers = visitsAndCart[visitsAndCart["cart_time"].isnull()]
lenNullCartUsers = len(nullCartUsers)
print(f"The count of users without any items in carts are: {lenNullCartUsers}")

#percent of users who visited ended up not placing a t-shirt in their cart
percentNullCartUsers = float(lenNullCartUsers) / lenVisitsAndCart * 100
print(f"Percent of users who visited and not placing anything in their cart: {percentNullCartUsers}")
print()

#merge cart and checkout, count users
cartAndCheckout = pd.merge(cart, checkout, how="left")
print(cartAndCheckout)
print(f"The count of users with anything in their cart: {len(cartAndCheckout)}")
countNullCheckoutUsers = len(cartAndCheckout[cartAndCheckout["checkout_time"].isnull()])
print(f"The count of users did not proceed to checkout: {countNullCheckoutUsers}")
percentNullCheckoutUsers = float(countNullCheckoutUsers) / len(cartAndCheckout) * 100
print(f"Percent of users who put items in their cart, but did not proceed to checkout: {percentNullCheckoutUsers:.2f}")
print()

#merge all data
allData = visits.merge(cart, how="left") \
    .merge(checkout, how="left") \
    .merge(purchase, how="left")
print(allData)
