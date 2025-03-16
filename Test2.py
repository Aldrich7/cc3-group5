honda = 1000000
toyota = 2000000
aurelio = 3000000
checker = 1

while checker == 1:
    try:
        print("WELCOME TO ABC DEALERSHIP")
        car = int(input("""    CHOOSE YOUR CAR
    1. Honda
    2. Toyota
    3. Aurelio
    
CHOSEN CAR: """))

        if car >= 1 and car <= 3:
            mop = int(input("""\n        CHOOSE MODE OF PAYMENT:
    1. Cash (10% Discount)
    2. Installment (5% Interest)
    
CHOSEN PAYMENT: """))

            try:
                if mop == 1:  # cash payment
                    if car == 1:
                        print("\n<=====RECEIPT=====>")
                        print("Chosen your car: Honda ")
                        print("Total amount: PHP", honda - (honda * 0.1))
                        print("<=====RECEIPT=====>\n")
                    elif car == 2:
                        print("\n<=====RECEIPT=====>")
                        print("Chosen your car: Toyota ")
                        print("Total amount: PHP", toyota - (toyota * 0.1))
                        print("<=====RECEIPT=====>\n")
                    elif car == 3:
                        print("\n<=====RECEIPT=====>")
                        print("Chosen your car: Aurelio ")
                        print("Total amount: PHP", aurelio - (aurelio * 0.1))
                        print("<=====RECEIPT=====>\n")

                elif mop == 2:  # installment payment
                    raise Exception
            except Exception:
                months = int(input("""CHOOSE HOW MANY MONTHS: 12, 24 OR 36
        CHOSEN MONTHS: """))
                if months == 12 or months == 24 or months == 36:
                    if car == 1:
                        print("\n<=====RECEIPT=====>")
                        print("Chosen your car: Honda ")
                        print("Total amount: PHP", honda + (honda * 0.05))
                        print("Monthly payment: PHP", (honda + (honda * 0.05)) / months)
                        print("<=====RECEIPT=====>\n")
                    elif car == 2:
                        print("\n<=====RECEIPT=====>")
                        print("Chosen your car: Toyota ")
                        print("Total amount: PHP", toyota + (toyota * 0.05))
                        print("Monthly payment: PHP", (toyota + (toyota * 0.05)) / months)
                        print("<=====RECEIPT=====>\n")
                    elif car == 3:
                        print("\n<=====RECEIPT=====>")
                        print("Chosen your car: Aurelio ")
                        print("Total amount: PHP", aurelio + (aurelio * 0.05))
                        print("Monthly payment: PHP", (aurelio + (aurelio * 0.05)) / months)
                        print("<=====RECEIPT=====>\n")
                else:
                    print("Invalid input")
        else:
            print("Invalid input")
        checker = int(input("""Do you still want to continue?
    1. Yes
    2. No

Enter here: """))
    except ValueError:
        print("Invalid input")
    finally:
        print("\nThank you for visiting ABC Dealership!!\n")