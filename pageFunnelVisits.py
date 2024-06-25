import pandas as pd

visits = pd.read_csv('visits.csv', parse_dates=[1])
cart = pd.read_csv('cart.csv', parse_dates=[1])
checkout = pd.read_csv('checkout.csv', parse_dates=[1])
purchase = pd.read_csv('purchase.csv', parse_dates=[1])

#Inspect the DataFrames
# print(visits.head())
# print(len(visits))
# print()
# print(cart.head())
# print(len(cart))
# print()
# print(checkout.head())
# print()
# print(purchase.head())
# print()

#Combine visits and cart
visitsAndCart = pd.merge(visits, cart, how="left")
print(visitsAndCart.head(7))
print()

#find out the number of rows
lenVisitsAndCart = len(visitsAndCart)
print(f"The count of users: {lenVisitsAndCart}")

#count no items in cart users
nullCartUsers = visitsAndCart[visitsAndCart["cart_time"].isnull()]
lenNullCartUsers = len(nullCartUsers)
print(f"The count of users without any items in carts are: {lenNullCartUsers}")

#percent of users who visited ended up not placing a t-shirt in their cart
percentNullCartUsers = float(lenNullCartUsers) / float(lenVisitsAndCart) * 100
print(f"Percent of users who visited and not placing anything in their cart: {percentNullCartUsers}")
print()

#merge cart and checkout, count users
cartAndCheckout = pd.merge(cart, checkout, how="left")
#print(cartAndCheckout)
print(f"The count of users with anything in their cart: {len(cartAndCheckout)}")
countNullCheckoutUsers = len(cartAndCheckout[cartAndCheckout["checkout_time"].isnull()])
print(f"The count of users did not proceed to checkout: {countNullCheckoutUsers}")
percentNullCheckoutUsers = float(countNullCheckoutUsers) / float(len(cartAndCheckout)) * 100
print(f"Percent of users who put items in their cart, but did not proceed to checkout: {percentNullCheckoutUsers:.2f}")
print()

#merge all data
allData = visits.merge(cart, how="left") \
    .merge(checkout, how="left") \
    .merge(purchase, how="left")
print(allData.head(10))
print()

#users proceeded to checkout
reachedCheckoutUsers = allData[~allData.checkout_time.isnull()]
print(len(reachedCheckoutUsers))
checkoutNotPurchaseUsers = allData[(~allData.checkout_time.isnull()) & (allData.purchase_time.isnull())]
print(len(checkoutNotPurchaseUsers))
checkoutNotPurchasePercent = float(len(checkoutNotPurchaseUsers)) / float(len(reachedCheckoutUsers)) * 100
print(checkoutNotPurchasePercent)
print()
#print(checkoutAndPurchase.head(10))
# countNullPurchaseUsers = len(checkoutAndPurchase[checkoutAndPurchase.purchase_time.isnull()])
# print(f"The count of users which did not purchase: {countNullPurchaseUsers}")
# percentNullPurchaseUsers = float(countNullPurchaseUsers) / len(checkoutAndPurchase) * 100
# print(f"Percent of users proceeded to checkout, but did not purchase: {percentNullPurchaseUsers:.2f}")
print()

#Add a column that is the difference between purchase_time and visit_time
allData["time_to_purchase"] = (allData["purchase_time"] - allData["visit_time"])
print(allData.head(5))
print()

#Calculate the average time to purchase
meanTimeToPurchase = allData.time_to_purchase.mean()
print(f"The average time to purchase: {meanTimeToPurchase}")