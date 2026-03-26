'''
Author: Sam

'''

products = ["Apples", "Bananas", "Oranges"]
item = input("Desired product:")
no_of_items = int(input("Number of product: "))
add_cart = ["Yes", "No"]
customer_cart = []
tariff_per_prod = 1.1
Total_amount = 0
quantity = 0

############## Define functions for all products ##############
def apples():
    customer_cart.append("Apples")
    print(customer_cart)
    price_per_apple = 3
    print("Price for", no_of_items, item, "is ZAR", no_of_items * price_per_apple * tariff_per_prod)

def bananas():
    customer_cart.append("Bananas")
    print(customer_cart)
    price_per_banana = 3
    print("Price for", no_of_items, item, "is ZAR", no_of_items * price_per_banana * tariff_per_prod)

def oranges():
    customer_cart.append("Oranges")
    print(customer_cart)
    print("Products in cart include",customer_cart, "Do you want add more?(Yes/No):")
    while add_cart == "Yes":

    price_per_oranges = 4
    print("Price for", no_of_items, item, "is ZAR", int(no_of_items * price_per_oranges * tariff_per_prod))

########### Loops #######
while item in products:
    if item == "Apples":
        print(apples())
        break

    elif item == "Bananas" :
        print(bananas())
        break

    else:
        print(oranges())
        break

print()
