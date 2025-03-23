toyotaCars = ["Vios", "Fortuner", "Innova"]
hondaCars = ["City", "Civic", "CRV"]
aureliosCars = ["GT", "RT", "XT"]
fordCars = ["Ranger", "Mustang", "Explorer"]
MitsubishiCars = ["Mirage", "Montero", "Strada"]
toyotaCarsPrice = [2000000, 2500000, 3000000]
hondaCarsPrice = [1000000, 1500000, 2000000]
aureliosCarsPrice = [3000000, 3500000, 4000000]
fordCarsPrice = [1500000, 2000000, 2500000]
MitsubishiCarsPrice = [1200000, 1800000, 2300000]

checker = 1

while checker == 1:
    if checker == 2:
        break
    try:
        print("   WELCOME TO ABC DEALERSHIP")  # welcome message & car brands
        carBrand = int(input("""    CHOOSE CAR BRAND (1-5)
        1. Honda
        2. Toyota
        3. Aurelio
        4. Ford
        5. Mitsubishi
CHOSEN BRAND: """))
        print(" ")

        if carBrand >= 1 and carBrand <= 5:

            if carBrand == 1:
                carChosen = int(input(f"""    CHOOSE CAR MODEL (1-3)
    1. Honda City - PHP {hondaCarsPrice[0]:,}
    2. Honda Civic - PHP {hondaCarsPrice[1]:,}
    3. Honda CRV - PHP {hondaCarsPrice[2]:,}
    
CHOSEN MODEL: """))
                carPrice = hondaCarsPrice[carChosen - 1]
            elif carBrand == 2:
                carChosen = int(input(f"""    CHOOSE CAR MODEL (1-3)
    1. Toyota Vios - PHP {toyotaCarsPrice[0]:,}
    2. Toyota Fortuner - PHP {toyotaCarsPrice[1]:,}
    3. Toyota Innova - PHP {toyotaCarsPrice[2]:,}
    
CHOSEN MODEL: """))
                carPrice = toyotaCarsPrice[carChosen - 1]
            elif carBrand == 3:
                carChosen = int(input(f"""    CHOOSE CAR MODEL (1-3)
    1. Aurelio GT - PHP {aureliosCarsPrice[0]:,}
    2. Aurelio RT - PHP {aureliosCarsPrice[1]:,}
    3. Aurelio XT - PHP {aureliosCarsPrice[2]:,}
    
CHOSEN MODEL: """))
                carPrice = aureliosCarsPrice[carChosen - 1]
            elif carBrand == 4:
                carChosen = int(input(f"""    CHOOSE CAR MODEL (1-3)
    1. Ford Ranger - PHP {fordCarsPrice[0]:,}
    2. Ford Mustang - PHP {fordCarsPrice[1]:,}
    3. Ford Explorer - PHP {fordCarsPrice[2]:,}
    
CHOSEN MODEL: """))
                carPrice = fordCarsPrice[carChosen - 1]
            elif carBrand == 5:
                carChosen = int(input(f"""    CHOOSE CAR MODEL (1-3)
    1. Mitsubishi Mirage - PHP {MitsubishiCarsPrice[0]:,}
    2. Mitsubishi Montero - PHP {MitsubishiCarsPrice[1]:,}
    3. Mitsubishi Strada - PHP {MitsubishiCarsPrice[2]:,}
    
CHOSEN MODEL: """))
                carPrice = MitsubishiCarsPrice[carChosen - 1]
            else:
                print("Invalid input")
                continue
        else:
            print("Invalid input")
            continue

        print(" ")

        if carChosen < 1 or carChosen > 3:
            print("Invalid input")
            continue
        mop = int(input("""     CHOOSE MODE OF PAYMENT:
    1. Cash (10% Discount)
    2. Installment (5% Interest annually)
    
CHOSEN PAYMENT: """))
        if mop != 1 and mop != 2:
            print("\nInvalid input\n")
            continue

        try:
            if mop == 1:  # cash payment
                priceCalculation = round(carPrice * 0.90, 2)
                tupledPrice = f"{priceCalculation:,}"
                print("\n<=======RECEIPT=======>")
                print(f"Chosen your car: {carBrand} {carChosen}")
                print(f"Total amount: PHP {tupledPrice}")
                print("<=======RECEIPT=======>\n")

            elif mop == 2:  # installment payment
                raise Exception
        except Exception:
            months = int(input("""CHOOSE HOW MANY MONTHS: 12, 24 OR 36
    CHOSEN MONTHS: """))
            if months == 12 or months == 24 or months == 36:
                annual_interest_rate = 0.05
                total_interest = annual_interest_rate * (months / 12)
                priceCalculation = round(carPrice * (1 + total_interest), 2)
                tupledPrice = f"{priceCalculation:,}"
                monthlyPayment = round(priceCalculation / months, 2)
                tupledMonthlyPayment = f"{monthlyPayment:,}"
                print("\n<=======RECEIPT=======>")
                print(f"Chosen your car: {carBrand} {carChosen}")
                print(f"Total amount: PHP {tupledPrice}")
                print(f"Monthly payment: PHP {tupledMonthlyPayment}")
                print("<=======RECEIPT=======>\n")
            else:
                print("Invalid input\n")

        checker = int(input("""Make another transaction?
    1. Yes
    2. No

Enter here: """))
    except ValueError:
        print("Invalid input\n")
    finally:
        print("\nThank you for visiting ABC Dealership!!\n")
        continue