import time

products = ["Apples", "Bananas"]
Places_1 = ["Salvador", "Khandisa", "KwaDlangezwa"]
Places_2 = ["Empangeni"]
current_time = time.localtime().tm_hour
day = ""
item = ""
days = 0
no_of_apples = 0
no_of_bananas = 0
price_apple = 3
price_banana = 2
tot_amount_apples = 0
tot_amount_bananas = 0
address = 0
universal_tariff = 1.1
username_lyst = []
password_lyst = []
Alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
Beta = list("abcdefghijklmnopqrstuvwxys")
special_char = list("!@#$%^&*")
digits = list("12345678")
print(Alpha)
username = "John"
password = "John@01"

#########CREATE USER ACCOUNT ###########################
"""
User Account:
1. Username:
    1.1 must begin with capital letters
2. Password:
    2.1 Minimum length must be 6 characters 
    2.2 Maximum length must be 16 characters
    2.3 Must have at least one special characters(!@#$%^&*())
    2.4 Must have at least one digit(1234567890)
    2.5 Must have at least one upper case and one lower case characters
"""

print(" "*57, "PICKALOT")
print(" "*40,"Welcome to Pickalot, where you find and pick all you need!")

def check_account_exist():
    global day
    account_check = input(f" {" "*20}Do you have an existing Account?\n Either enter 'Yes or No':")
    if account_check.upper() == "YES":
            open_account()
    elif account_check.upper() == "NO":
            create_account()
    while account_check.upper() != "YES" or account_check.upper() != "NO":
        print(f" {" "*20}Invalid characters. Please try again!")
        print(check_account_exist())
        break

def create_account():
    global day
    consent_check = input(f"Do you wish to open one?\n Either enter 'Yes or No':")
    if consent_check.upper() == "YES":
        create_username()
    elif consent_check.upper() == "NO":
        print(f" {" " * 40}Thank you and gave a good {day}")
        exit()

def create_username():
    global username_lyst, username
    print(f" {1}. Username must begin with Capital letter! \n {2}. Must have minimum 6 characters")
    username = input("Create username: ")
    username_lyst.append(username)
    username_lyst = list(username)
    print(username_lyst)
    if username_lyst[0].upper() in Alpha and len(username_lyst) >= 6 and username_lyst == list(username):
        print(f"Hi {username.upper()}, lets create password ")
        create_password()
    elif username_lyst[0].upper() not in Alpha and len(username) >= 6 and username_lyst == list(username):
        print(f"Error!\nUsername must begin with Capital letter!")
        create_username()
    elif username_lyst[0].upper() in Alpha and len(username) < 6 and username_lyst == list(username):
        print(f"Error!\nMust have minimum 6 characters")
        create_username()
    elif username_lyst[0].upper() not in Alpha and len(username) < 6 and username_lyst == list(username):
        print(f" Username must begin with Capital letter!\nMust have minimum 6 characters")
    else:
        print("Error")
        create_username()

def create_password():
    global password, password_lyst
    print(f"{1}. Must have minimum 6 characters\n{2}. Must have one special character(!@#$%^&*)\n{3}.Must have one digit(1234567890)\n{4}. Must have one upper case letter\n{5}. Must have one lower case letter.")
    password = input(f"Create password: ")
    password_lyst.append(password)
    password_lyst = list(password)
    print(password_lyst)
    if len(password) >= 6 and password_lyst in special_char and password_lyst in digits and password_lyst in Beta and password_lyst in Alpha and password_lyst == list(password):
        print(f"Password successfully created!")
        open_account()
    elif len(password) < 6 and password_lyst in special_char and password_lyst in digits and password_lyst in Beta and password_lyst in Alpha and password_lyst == list(password):
        print("Password length is short. Please try again!")
        create_password()
    elif len(password) >= 6 and password_lyst not in special_char and password_lyst in digits and password_lyst in Beta and password_lyst in Alpha and password_lyst == list(password):
        print("No special character. Please try again")
        create_password()
    elif len(password) >= 6 and password_lyst in special_char and password_lyst not in digits and password_lyst in Beta and password_lyst in Alpha and password_lyst == list(password):
        print("No digit in password. Please try again!")
        create_password()
    elif len(password) >= 6 and password_lyst in special_char and password_lyst in digits and password_lyst not in Beta and password_lyst in Alpha and password_lyst == list(password):
        print("No lower case character. Please try again!")
        create_password()
    elif len(password) >= 6 and password_lyst in special_char and password_lyst in digits and password_lyst in Beta and password_lyst not in Alpha and password_lyst == list(password):
        print("No Upper cace character. Please try again!")
        create_password()

def open_account():
    open_username = input(f"Provide username: ")
    open_password = input(f"Enter Password: ")
#############END USER ACCOUNT ################################



##################### Iteration function #######################
def restart_error():
    global item
    again_item = input("Try again:")
    item = again_item
    if item == "Apples":
        print(apples())
    elif item == "Bananas":
        print(bananas())

def add_to_cart():
    global no_of_apples, no_of_bananas
    global tot_amount_apples, tot_amount_bananas
    global address
    global days
    global current_time
    global day

    another_item = input("Search again:")

    if another_item == "Apples":
        print("Price of 1 apple is R3")
        add_no_of_apples = int(input("How many apples?"))
        no_of_apples += add_no_of_apples

        tot_amount_apples = int(no_of_apples * price_apple * universal_tariff)

    elif another_item == "Bananas":
        print("Price of 1 banana is R2")
        add_no_of_bananas = int(input("How many bananas?"))
        no_of_bananas += add_no_of_bananas

        tot_amount_bananas = int(no_of_bananas * price_banana * universal_tariff)

    print("Current total is ZAR", tot_amount_apples + tot_amount_bananas)

    check_procedure = input("Do you still wish to add more products (Yes / No)?")

    if check_procedure == "Yes":
        return add_to_cart()

    if check_procedure == "No":
        address = input("Please write street name to address for delivery:")
        print(delivery_time())
        print(time_of_day())
        print("Great! Your checkout price is ZAR",
              tot_amount_apples + tot_amount_bananas,
              "\nVisit banking app to confirm EFT!\nProduct shall be delivered at",
              address, "in", days,"days\nThanks and have a good"+ day +"!")
    exit()

print(check_account_exist())
###################### END #####################################

############# FUNCTIONS FOR PRODUCTS ############################
def apples():
    global no_of_apples,\
        tot_amount_apples,\
        address, \
        days, \
        day,\
        current_time, \
        item
    print(" " * 57, "PICKALOT")
    print("Price of 1 apple is R3")
    item = input("Search :")
    if item == products[0]:
        no_of_apples = int(input("How many apples?"))
        tot_amount_apples = int(no_of_apples * price_apple * universal_tariff)

        print("Price for", no_of_apples, "apples is ZAR", tot_amount_apples)

        check_procedure_apple = input("Do you wish to add more products (Yes / No)?")

        if check_procedure_apple == "Yes":
            return add_to_cart()

        if check_procedure_apple == "No":
            address = input("Please write street name to address for delivery:")
            print(delivery_time())
            print(time_of_day())
            print("Great! Your checkout price is ZAR",
                  tot_amount_apples + tot_amount_bananas,
                  "\nVisit banking app to confirm EFT!\nProduct shall be delivered at",
                  address, "in", days," days\nThanks and have a good"+ day +"!")
    exit()

def delivery_time():
    global days
    if address in Places_1:
        days = 1
    if address in Places_2:
        days = 2

def time_of_day():
    global day
    if 5 <= current_time < 12:
        day = "morning"
    elif 12 <= current_time < 18:
        day = "day"
    else:
        day = "night"

def bananas():
    global no_of_bananas
    global  tot_amount_bananas
    global address
    global days
    global current_time
    global day
    global item

    print(" " * 57, "PICKALOT")
    print("Price of 1 banana is R2")
    item = input("Search :")
    if item == products[1]:
        no_of_bananas = int(input("How many bananas?"))
        tot_amount_bananas = int(no_of_bananas * price_banana * universal_tariff)

        print("Price for", no_of_bananas, "bananas is ZAR", tot_amount_bananas)

        check_procedure_banana = input("Do you wish to add more products (Yes / No)?")

        if check_procedure_banana == "Yes":
            return add_to_cart()

        if check_procedure_banana == "No":
            address = input("Please write street name to address for delivery:")
            print(delivery_time())
            print(time_of_day())
            print("Great! Your checkout price is ZAR",
                  tot_amount_apples + tot_amount_bananas,
                  "\nVisit banking app to confirm EFT!\nProduct shall be delivered at",
                  address, "in", days ,"days\nThanks and have a good"+ day +"!")
    exit()

#################### MAIN LOOP ##################################
while item in products:
    if item == "Apples":
        print(apples())

    elif item == "Bananas":
        print(bananas())
    else:
        print("Invalid Input")
        print(restart_error())


