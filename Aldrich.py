print("Welcome to ABC Car Dealership!!\n")

toyota = 100000000
ford = 500000000
mclaren = 1000000000

try:
    carchoice = int(input("""CAR CHOICES:
    1. TOYOTA = PHP 100,000,000
    2. FORD = PHP 500,000,000
    3. MCLAREN = PHP 1,000,000,000
    
    Enter here: """))

    cashchoice = int(input("""\nCHOICES:
    1. CASH
    2. INSTALLMENT
    
    Enter here: """))

    if cashchoice == 1:
        print("\nYou have picked Cash payment & you will receive a 10% discount for the car that you have chosen: ")
        if carchoice == 1:
            print("Car: Toyota")
            print("")
        elif carchoice == 2:
            print("Car: Ford")
            print("")
        elif carchoice == 3:
            print("Car: Mclaren")
            print("")

    elif cashchoice == 2:
        print("\nYou have picked Installment: ")
        installment = int(input("""How many months do you want to loan: 
    1. 12 Months
    2. 24 Months
    3. 36 Months
        
    Enter here: """))
        if installment == 1:
            print("\nYou have picked 12 Months")
            if carchoice == 1:
                print("Car: Toyota")
                print("")
            elif carchoice == 2:
                print("Car: Ford")
                print("")
            elif carchoice == 3:
                print("Car: Mclaren")
                print("")
        elif installment == 2:
            print("\nYou have picked 24 Months")
            if carchoice == 1:
                print("Car: Toyota")
                print("")
            elif carchoice == 2:
                print("Car: Ford")
                print("")
            elif carchoice == 3:
                print("Car: Mclaren")
                print("")
        elif installment == 2:
            print("\nYou have picked 36 Months")
            if carchoice == 1:
                print("Car: Toyota")
                print("")
            elif carchoice == 2:
                print("Car: Ford")
                print("")
            elif carchoice == 3:
                print("Car: Mclaren")
                print("")

except ValueError:
    print("\nInvalid Input!! Try again!!")

finally:
    print("Thank you for vising ABC Car Dealership")
