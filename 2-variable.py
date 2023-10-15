import math

name = "Coca Cola"
price = 11.11
quantity =  input("Quantity: ")
is_soleout = True

print("Product name: ", name,
    "\nTotal: ", round(price * float(quantity)),
    "\nTotal: ", math.floor(price * float(quantity)),
    "\nTotal: ", math.ceil(price * float(quantity)),
    "\nTotal: ", '{:.4f}'.format(price * float(quantity)),
    "\nOn sale: ", type(is_soleout))

