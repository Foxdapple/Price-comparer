# Bakery problem
# Aaron Heald, 16/10/19

# V1: Get's inputs for lists and stores then displays them
# V2: Sets up functions to fix errors within the code
# V3: Makes printing more efficient and fixes xxx input if nothing is in list

# Functions go here

def budget_check(question):
    valid = False
    while not valid:
        try:
            response = float(input(question))
            if response < 5 :
                print("Please enter a price greater than or equal to 5 ")
                print("")
            else:
                valid = True
                return response
        except ValueError:
            print("Please enter an integer")
            print()

def int_check(question):
    valid = False
    while not valid:
        try:
            response = int(input(question))
            if response <= 0 or response >= 5 :
                print("Please enter a number between 1-4 (those numbers included)")
                print("")
            else:
                valid = True
                return response
        except ValueError:
            print("Please enter an integer")
            print()

def unit_check(question):
    valid = False
    while not valid:
        try:
            response = float(input(question))
            if response <= 0 :
                print("Please enter a number greater than 0")
                print("")
            else:
                valid = True
                return response
        except ValueError:
            print("Please enter an integer")
            print()

def float_check(question):
    valid = False
    while not valid:
        try:
            response = float(input(question))
            if response <= 0 :
                print("Please enter a price greater than $0")
                print("")
            else:
                valid = True
                return response
        except ValueError:
            print("Please enter an integer")
            print()

def blank_check(question):
    valid = False
    while not valid:
        response = input(question)

        try:
            response = float(response)
            print("Please input a string")
            print()

        except ValueError:
            valid = True

    return(response)

def comparison_print(heading,summary):

    print(heading)
    # Sets up Header for the businesses
    print("\nProduct:\tPrice($)\tMass/Volume\tUnit_Price($)")

    # prints table
    for item in summary:
        #separates items in list from each other
        print(*item, sep="\t")

    print()

#-----------------------------------------

# Main routine

conti = False
while not conti:

    # set up lists for later use
    summary = []
    price = []

    # asks user for that is greater than $5
    budget = budget_check("How much money do you have on hand? (min is $5): ")

    loop = False
    while not loop:

        temp_product = []

        # asks user what the name of the product is
        print()
        repeat = False
        while not repeat:
            p_name = blank_check("What is the name of the product? (if you don't wish to add anymore enter xxx): ")
            if p_name == "xxx" and price == [] or p_name == "XXX" and price == [] or p_name == "":
                xxx_check = True
                print()
                print("Please put an item in the list first!")
                print()

            elif p_name == "xxx" or p_name == "XXX" or p_name == "":
                xxx_check = False
                loop = True
                repeat = True
                print()

            else:
                repeat = True
                xxx_check = False
                print()

                # asks user for unit of measurement for their product
                print("<1> for g, <2> for Kg, <3> for ml and <4> for L")
                unit = int_check("What is the unit of measurement?: ")
                print()

                # Sets up units for later use
                if unit == 1:
                    measure = "g"

                elif unit == 2:
                    measure = "Kg"

                elif unit == 3:
                    measure = "ml"

                elif unit == 4:
                    measure = "L"

                # starts main routine
                print("You have chosen <{}>".format(measure))
                print()

                # asks user for the weight and price of their product
                mass = unit_check("What is the mass/volume of the product? <{}>: ".format(measure))

                # Price check if statement
                p_price = unit_check("What is the price of the product?: ")

                # calculates weight
                if measure == "g" or measure == "ml":
                    mass = mass/1000

                # Calculates unit price
                unit_price = round((p_price/mass),2)
                print("The unit price is ${}".format(unit_price))

                if measure == "g":
                    measure = "Kg"

                elif measure == "ml":
                    measure = "L"

                # sets up price as a string so list can be organised
                p_price = "${}".format(p_price)
                p_mass = "{}{}".format(mass, measure)
                p_unit_price = "${} per Kg/L".format(unit_price)

                # adds figures and information to their designated lists
                temp = []
                price.append(unit_price)
                temp.append(p_name)
                temp.append(p_price)
                temp.append(p_mass)
                temp.append(p_unit_price)

                summary.append(temp)

    while not xxx_check:

        # Gets highest and lowest products for later use
        summary.sort(key=lambda x:x[3], reverse=True)
        recommended = (summary[1:3])
        recommended = (recommended[:1])
        summary.sort(key=lambda x:x[3])
        high_recommended = (summary[:1])

        # find's the low, high, average and recommended price of all the products
        low = (min(price))
        high = (max(price))
        average = round((low + high)/2,2)

        # Sort sales summary by High-low (descending)
        summary.sort(key=lambda x:x[1], reverse=True)
        comparison_print("***** Results by Price (Descending) ******",summary)

        # prints high, low and average of the list's unit price
        print("The highest unit price is: ${}".format(high))
        print("The lowest unit price is: ${}".format(low))
        print("The average unit price is: ${}".format(average))
        print()

        # Prints recommended product for user to buy
        print("Recommended item is (by unit price):", recommended)
        print("The most expensive item is (by unit price):", high_recommended)
        print()

        # Checks if user wants to repeat for different product
        cont = input("Do you compare more prices? <yes to continue> <anything else to end>: ").lower()

        if cont == "yes" or cont == "y":
            print()
            xxx_check = True

        else:
            exit("Thanks for using this price comparer")
