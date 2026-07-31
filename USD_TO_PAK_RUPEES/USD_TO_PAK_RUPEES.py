# convert usd to pak rupees


def usd_to_pkr(usd):
    rate = 278   # example rate (1 USD = 278 PKR)
    pkr = usd * rate
    return pkr

# take input
usd_amount = float(input("Enter USD amount: "))

# call function
result = usd_to_pkr(usd_amount)

# show result
print("PKR =", result)





