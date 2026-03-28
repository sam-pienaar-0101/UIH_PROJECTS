products = ["Apples", "Bananas", "Oranges"]
item = input("Search :")
no_of_apples = 0
no_of_bananas = 0
price_apple = 3
price_banana = 2
tot_amount_apples = 0
tot_amount_bananas = 0
address = 0
universal_tariff = 1.1


##################### Iteration function #######################
def add_to_cart():
    another_item = input("Search again:")
    new_num_of_apples = no_of_apples
    new_num_of_bananas = no_of_bananas
    global address
    if another_item == "Apples":
        print("Price of 1 apple is R3")
        add_no_of_apples = int(input("How many apples?"))
        new_num_of_apples += add_no_of_apples
        print("Now new price for", new_num_of_apples, "apples is ZAR", int((new_num_of_apples * price_apple) * universal_tariff))
        check_procedure = input("Do you still wish to add more products (Yes / No)?")
        while check_procedure == "Yes":
            return add_to_cart()
        if check_procedure == "No":
            address = input("Please write street name to address for delivery:")
            print("Great! Your checkout price for ", new_num_of_apples, "apples is ZAR", int((new_num_of_apples * price_apple) * universal_tariff),"\n Visit banking app to confirm EFT! \n product shall be delivered at",address, "in 2 days \n Thanks and have a good day!" )

    elif another_item == "Bananas":
        print("Price of 1 banana is R2")
        add_no_of_bananas = int(input("How many bananas?"))
        new_num_of_bananas += add_no_of_bananas
        print("Now new price for", new_num_of_bananas, "bananas is ZAR", int((new_num_of_bananas * price_banana) * universal_tariff))
        check_procedure = input("Do you still wish to add more products (Yes / No)?")
        while check_procedure == "Yes":
            return add_to_cart()
        if check_procedure == "No":
            address = input("Please write street name to address for delivery:")
            print("Great! Your checkout price for ", new_num_of_bananas, "apples is ZAR", int((new_num_of_bananas * price_banana) * universal_tariff),"\n Visit banking app to confirm EFT! \n product shall be delivered at",address, "in 2 days \n Thanks and have a good day!" )
    exit()
###################### END OF ITERATION FUNCTION ##############################################

############# FUNCTIONS FOR PRODUCTS ###########################################################
def apples():
    print("Price of 1 apple is R3")
    global no_of_apples
    global tot_amount_apples
    global address
    if item == products[0]:
        no_of_apples = int(input("How many apples?"))
        tot_amount_apples = int((no_of_apples * price_apple) * universal_tariff)
        print("Price for", no_of_apples, "apples is ZAR", tot_amount_apples, )
        check_procedure_apple = input("Do you wish to add more products (Yes / No)?")
        while check_procedure_apple == "Yes":
            return add_to_cart()
        if check_procedure_apple == "No":
            address = input("Please write street name to address for delivery:")
            print("Great! Your checkout price for ", no_of_apples, "Apples is",
                  tot_amount_apples, "\n Visit banking app to confirm EFT! \n product shall be delivered at",address, "in 2 days \n Thanks and have a good day!")
    exit()

def bananas():
    print("Price of 1 banana is R2")
    global no_of_bananas
    global tot_amount_bananas
    global address
    if item == products[1]:
        no_of_bananas = int(input("How many bananas?"))
        tot_amount_bananas = int((no_of_bananas * price_banana) * universal_tariff)
        print("Price for", no_of_bananas, "apples is ZAR",tot_amount_bananas )
        check_procedure_banana = input("Do you wish to add more products (Yes / No)?")
        while check_procedure_banana == "Yes":
            return add_to_cart()
        if check_procedure_banana == "No":
            address = input("Please write street name to address for delivery:")
            print("Great! Your checkout price for ", no_of_bananas, "bananas is",
                  tot_amount_bananas,
                  "\n Visit banking app to confirm EFT! \n product shall be delivered at", address,
                  "in 2 days \n Thanks and have a good day!")
    exit()

################# END OF PRODUCT FUNCTIONS ######################################################


############# FUNCTIONS FOR ALL PERMUTATIONS #######################################
def two_products():
    if item == "Apples" and item == "Bananas":
        print("Great! Your checkout price for ", no_of_bananas, "bananas and", no_of_apples, "apples is ZAR",
              (tot_amount_bananas + tot_amount_apples),
                  "\n Visit banking app to confirm EFT! \n product shall be delivered at", address,
                  "in 2 days \n Thanks and have a good day!")






###################### END OF PERMUTATIONS #########################################


#################### Loops to print outcome ########################################
while item in products:
    if item == "Apples":
        print(apples())

    elif item == "Bananas":
        print(bananas())

#################3 END OF LOOPS ######################################################         
