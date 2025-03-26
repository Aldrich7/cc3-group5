#CAR MODELS
toyotaCars = ["Vios", "Fortuner", "Innova", "Corolla", "Camry", "Hilux", "Land Cruiser", "RAV4", "Yaris", "Avalon"]
hondaCars = ["City", "Civic", "CRV", "Accord", "Jazz", "HR-V", "Pilot", "Odyssey", "Brio", "Passport"]
aureliosCars = ["GT", "RT", "XT", "ST", "LT", "MT", "PT", "QT", "UT", "VT"]
fordCars = ["Ranger", "Mustang", "Explorer", "F-150", "Escape", "Edge", "Bronco", "Fusion", "Taurus", "Expedition"]
MitsubishiCars = ["Mirage", "Montero", "Strada", "Pajero", "Lancer", "Outlander", "Xpander", "ASX", "Eclipse Cross", "Triton"]
bmwCars = ["Series 3", "Series 5", "Series 7", "X1", "X3", "X5", "Z4", "i8", "M3", "M5"]
mercedesCars = ["A-Class", "C-Class", "E-Class", "S-Class", "GLA", "GLC", "GLE", "GLS", "AMG GT", "EQC"]
audiCars = ["A3", "A4", "A6", "A8", "Q3", "Q5", "Q7", "Q8", "TT", "R8"]
chevroletCars = ["Spark", "Malibu", "Impala", "Camaro", "Equinox", "Traverse", "Tahoe", "Suburban", "Blazer", "Trailblazer"]
nissanCars = ["Micra", "Sunny", "Altima", "Maxima", "Juke", "Qashqai", "X-Trail", "Patrol", "GT-R", "370Z"]

#CAR BRANDS
carModels = [hondaCars, toyotaCars, aureliosCars, fordCars, MitsubishiCars, bmwCars, mercedesCars, audiCars, chevroletCars, nissanCars]
carBrands = ["Honda", "Toyota", "Aurelio", "Ford", "Mitsubishi", "BMW", "Mercedes", "Audi", "Chevrolet", "Nissan"]

#CAR PRICES
toyotaCarsPrice = [2000000, 2500000, 3000000, 2200000, 2700000, 3200000, 3700000, 2400000, 1900000, 2800000]
hondaCarsPrice = [1000000, 1500000, 2000000, 1800000, 1300000, 1700000, 2500000, 3000000, 900000, 2200000]
aureliosCarsPrice = [3000000, 3500000, 4000000, 3200000, 3700000, 4200000, 4500000, 3800000, 3400000, 3600000]
fordCarsPrice = [1500000, 2000000, 2500000, 3000000, 1800000, 2300000, 2800000, 2100000, 2600000, 3500000]
MitsubishiCarsPrice = [1200000, 1800000, 2300000, 2800000, 1500000, 2000000, 2500000, 1700000, 2200000, 2700000]
bmwCarsPrice = [3000000, 4000000, 5000000, 3500000, 4500000, 5500000, 6000000, 7000000, 8000000, 9000000]
mercedesCarsPrice = [3200000, 4200000, 5200000, 6200000, 3700000, 4700000, 5700000, 6700000, 7700000, 8700000]
audiCarsPrice = [3100000, 4100000, 5100000, 6100000, 3600000, 4600000, 5600000, 6600000, 7600000, 8600000]
chevroletCarsPrice = [1500000, 2500000, 3500000, 4500000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000]
nissanCarsPrice = [1400000, 2400000, 3400000, 4400000, 1900000, 2900000, 3900000, 4900000, 5900000, 6900000]

checker = 1

while checker == 1 or checker == 2:
    if checker == 2:
        break
    try:
        print("   WELCOME TO ABC DEALERSHIP")  # welcome message & car brands
        carBrand = int(input("""    CHOOSE CAR BRAND (1-10)
        1. Honda
        2. Toyota
        3. Aurelio
        4. Ford
        5. Mitsubishi
        6. BMW
        7. Mercedes
        8. Audi
        9. Chevrolet
        10. Nissan
    CHOSEN BRAND: """))
        print(" ")

        if carBrand >= 1 and carBrand <= 10:
            carBrandName = carBrands[carBrand - 1]
            carModelsList = carModels[carBrand - 1]

            if carBrand == 1:
                carChosen = int(input(f"""    CHOOSE CAR MODEL (1-10)
        1. Honda City - PHP {hondaCarsPrice[0]:,}
        2. Honda Civic - PHP {hondaCarsPrice[1]:,}
        3. Honda CRV - PHP {hondaCarsPrice[2]:,}
        4. Honda Accord - PHP {hondaCarsPrice[3]:,}
        5. Honda Jazz - PHP {hondaCarsPrice[4]:,}
        6. Honda HR-V - PHP {hondaCarsPrice[5]:,}
        7. Honda Pilot - PHP {hondaCarsPrice[6]:,}
        8. Honda Odyssey - PHP {hondaCarsPrice[7]:,}
        9. Honda Brio - PHP {hondaCarsPrice[8]:,}
        10. Honda Passport - PHP {hondaCarsPrice[9]:,}
    CHOSEN MODEL: """))
                carPrice = hondaCarsPrice[carChosen - 1]
            elif carBrand == 2:
                carChosen = int(input(f"""    CHOOSE CAR MODEL (1-10)
    1. Toyota Vios - PHP {toyotaCarsPrice[0]:,}
    2. Toyota Fortuner - PHP {toyotaCarsPrice[1]:,}
    3. Toyota Innova - PHP {toyotaCarsPrice[2]:,}
    4. Toyota Corolla - PHP {toyotaCarsPrice[3]:,}
    5. Toyota Camry - PHP {toyotaCarsPrice[4]:,}
    6. Toyota Hilux - PHP {toyotaCarsPrice[5]:,}
    7. Toyota Land Cruiser - PHP {toyotaCarsPrice[6]:,}
    8. Toyota RAV4 - PHP {toyotaCarsPrice[7]:,}
    9. Toyota Yaris - PHP {toyotaCarsPrice[8]:,}
    10. Toyota Avalon - PHP {toyotaCarsPrice[9]:,}
    
CHOSEN MODEL: """))
                carPrice = toyotaCarsPrice[carChosen - 1]
            elif carBrand == 3:
                carChosen = int(input(f"""    CHOOSE CAR MODEL (1-10)
    1. Aurelio GT - PHP {aureliosCarsPrice[0]:,}
    2. Aurelio RT - PHP {aureliosCarsPrice[1]:,}
    3. Aurelio XT - PHP {aureliosCarsPrice[2]:,}
    4. Aurelio ST - PHP {aureliosCarsPrice[3]:,}
    5. Aurelio LT - PHP {aureliosCarsPrice[4]:,}
    6. Aurelio MT - PHP {aureliosCarsPrice[5]:,}
    7. Aurelio PT - PHP {aureliosCarsPrice[6]:,}
    8. Aurelio QT - PHP {aureliosCarsPrice[7]:,}
    9. Aurelio UT - PHP {aureliosCarsPrice[8]:,}
    10. Aurelio VT - PHP {aureliosCarsPrice[9]:,}
    
CHOSEN MODEL: """))
                carPrice = aureliosCarsPrice[carChosen - 1]
            elif carBrand == 4:
                carChosen = int(input(f"""    CHOOSE CAR MODEL (1-10)
    1. Ford Ranger - PHP {fordCarsPrice[0]:,}
    2. Ford Mustang - PHP {fordCarsPrice[1]:,}
    3. Ford Explorer - PHP {fordCarsPrice[2]:,}
    4. Ford F-150 - PHP {fordCarsPrice[3]:,}
    5. Ford Escape - PHP {fordCarsPrice[4]:,}
    6. Ford Edge - PHP {fordCarsPrice[5]:,}
    7. Ford Bronco - PHP {fordCarsPrice[6]:,}
    8. Ford Fusion - PHP {fordCarsPrice[7]:,}
    9. Ford Taurus - PHP {fordCarsPrice[8]:,}
    10. Ford Expedition - PHP {fordCarsPrice[9]:,}
    
CHOSEN MODEL: """))
                carPrice = fordCarsPrice[carChosen - 1]
            elif carBrand == 5:
                carChosen = int(input(f"""    CHOOSE CAR MODEL (1-10)
    1. Mitsubishi Mirage - PHP {MitsubishiCarsPrice[0]:,}
    2. Mitsubishi Montero - PHP {MitsubishiCarsPrice[1]:,}
    3. Mitsubishi Strada - PHP {MitsubishiCarsPrice[2]:,}
    4. Mitsubishi Pajero - PHP {MitsubishiCarsPrice[3]:,}
    5. Mitsubishi Lancer - PHP {MitsubishiCarsPrice[4]:,}
    6. Mitsubishi Outlander - PHP {MitsubishiCarsPrice[5]:,}
    7. Mitsubishi Xpander - PHP {MitsubishiCarsPrice[6]:,}
    8. Mitsubishi ASX - PHP {MitsubishiCarsPrice[7]:,}
    9. Mitsubishi Eclipse Cross - PHP {MitsubishiCarsPrice[8]:,}
    10. Mitsubishi Triton - PHP {MitsubishiCarsPrice[9]:,}
    
CHOSEN MODEL: """))
                carPrice = MitsubishiCarsPrice[carChosen - 1]
            elif carBrand == 6:
                carChosen = int(input(f"""    CHOOSE CAR MODEL (1-10)
    1. BMW Series 3 - PHP {bmwCarsPrice[0]:,}
    2. BMW Series 5 - PHP {bmwCarsPrice[1]:,}
    3. BMW Series 7 - PHP {bmwCarsPrice[2]:,}
    4. BMW X1 - PHP {bmwCarsPrice[3]:,}
    5. BMW X3 - PHP {bmwCarsPrice[4]:,}
    6. BMW X5 - PHP {bmwCarsPrice[5]:,}
    7. BMW Z4 - PHP {bmwCarsPrice[6]:,}
    8. BMW i8 - PHP {bmwCarsPrice[7]:,}
    9. BMW M3 - PHP {bmwCarsPrice[8]:,}
    10. BMW M5 - PHP {bmwCarsPrice[9]:,}
    
CHOSEN MODEL: """))
                carPrice = bmwCarsPrice[carChosen - 1]
            elif carBrand == 7:
                carChosen = int(input(f"""    CHOOSE CAR MODEL (1-10)
    1. Mercedes A-Class - PHP {mercedesCarsPrice[0]:,}
    2. Mercedes C-Class - PHP {mercedesCarsPrice[1]:,}
    3. Mercedes E-Class - PHP {mercedesCarsPrice[2]:,}
    4. Mercedes S-Class - PHP {mercedesCarsPrice[3]:,}
    5. Mercedes GLA - PHP {mercedesCarsPrice[4]:,}
    6. Mercedes GLC - PHP {mercedesCarsPrice[5]:,}
    7. Mercedes GLE - PHP {mercedesCarsPrice[6]:,}
    8. Mercedes GLS - PHP {mercedesCarsPrice[7]:,}
    9. Mercedes AMG GT - PHP {mercedesCarsPrice[8]:,}
    10. Mercedes EQC - PHP {mercedesCarsPrice[9]:,}
    
CHOSEN MODEL: """))
                carPrice = mercedesCarsPrice[carChosen - 1]
            elif carBrand == 8:
                carChosen = int(input(f"""    CHOOSE CAR MODEL (1-10)
    1. Audi A3 - PHP {audiCarsPrice[0]:,}
    2. Audi A4 - PHP {audiCarsPrice[1]:,}
    3. Audi A6 - PHP {audiCarsPrice[2]:,}
    4. Audi A8 - PHP {audiCarsPrice[3]:,}
    5. Audi Q3 - PHP {audiCarsPrice[4]:,}
    6. Audi Q5 - PHP {audiCarsPrice[5]:,}
    7. Audi Q7 - PHP {audiCarsPrice[6]:,}
    8. Audi Q8 - PHP {audiCarsPrice[7]:,}
    9. Audi TT - PHP {audiCarsPrice[8]:,}
    10. Audi R8 - PHP {audiCarsPrice[9]:,}
    
CHOSEN MODEL: """))
                carPrice = audiCarsPrice[carChosen - 1]
            elif carBrand == 9:
                carChosen = int(input(f"""    CHOOSE CAR MODEL (1-10)
    1. Chevrolet Spark - PHP {chevroletCarsPrice[0]:,}
    2. Chevrolet Malibu - PHP {chevroletCarsPrice[1]:,}
    3. Chevrolet Impala - PHP {chevroletCarsPrice[2]:,}
    4. Chevrolet Camaro - PHP {chevroletCarsPrice[3]:,}
    5. Chevrolet Equinox - PHP {chevroletCarsPrice[4]:,}
    6. Chevrolet Traverse - PHP {chevroletCarsPrice[5]:,}
    7. Chevrolet Tahoe - PHP {chevroletCarsPrice[6]:,}
    8. Chevrolet Suburban - PHP {chevroletCarsPrice[7]:,}
    9. Chevrolet Blazer - PHP {chevroletCarsPrice[8]:,}
    10. Chevrolet Trailblazer - PHP {chevroletCarsPrice[9]:,}
    
CHOSEN MODEL: """))
                carPrice = chevroletCarsPrice[carChosen - 1]
            elif carBrand == 10:
                carChosen = int(input(f"""    CHOOSE CAR MODEL (1-10)
    1. Nissan Micra - PHP {nissanCarsPrice[0]:,}
    2. Nissan Sunny - PHP {nissanCarsPrice[1]:,}
    3. Nissan Altima - PHP {nissanCarsPrice[2]:,}
    4. Nissan Maxima - PHP {nissanCarsPrice[3]:,}
    5. Nissan Juke - PHP {nissanCarsPrice[4]:,}
    6. Nissan Qashqai - PHP {nissanCarsPrice[5]:,}
    7. Nissan X-Trail - PHP {nissanCarsPrice[6]:,}
    8. Nissan Patrol - PHP {nissanCarsPrice[7]:,}
    9. Nissan GT-R - PHP {nissanCarsPrice[8]:,}
    10. Nissan 370Z - PHP {nissanCarsPrice[9]:,}
    
CHOSEN MODEL: """))
                carPrice = nissanCarsPrice[carChosen - 1]
            else:
                print("\nInvalid Input!! Try again!!\n")
                continue
        else:
            print("\nInvalid Input!! Try again!!\n")
            continue

        print(" ")

        if carChosen < 1 or carChosen > 10:
            print("\nInvalid Input!! Try again!!\n")
            continue

        mop = int(input("""     CHOOSE MODE OF PAYMENT:
    1. Cash (10% Discount)
    2. Installment (5% Interest annually)
    
CHOSEN PAYMENT: """))
        if mop != 1 and mop != 2:
            print("\nInvalid Input!! Try again!!\n")
            continue

        try:
            if mop == 1:  # cash payment
                priceCalculation = round(carPrice * 0.90, 2)
                tupledPrice = f"{priceCalculation:,}"
                print("\n<=======RECEIPT=======>")
                print(f"Chosen your car: {carBrandName} {carModelsList[carChosen - 1]}")
                print(f"Total amount: PHP {tupledPrice}")
                print("<=======RECEIPT=======>\n")

            elif mop == 2:  # installment payment
                raise Exception
        except Exception:
            months = int(input("""\nCHOOSE HOW MANY MONTHS: 12, 24 OR 36
    CHOSEN MONTHS: """))
            if months == 12 or months == 24 or months == 36:
                annual_interest_rate = 0.05
                total_interest = annual_interest_rate * (months / 12)
                priceCalculation = round(carPrice * (1 + total_interest), 2)
                tupledPrice = f"{priceCalculation:,}"
                monthlyPayment = round(priceCalculation / months, 2)
                tupledMonthlyPayment = f"{monthlyPayment:,}"
                print("\n<=======RECEIPT=======>")
                print(f"Chosen your car: {carBrandName} {carModelsList[carChosen - 1]}")
                print(f"Total amount: PHP {tupledPrice}")
                print(f"Total months: {months}")
                print(f"Monthly payment: PHP {tupledMonthlyPayment}")
                print("<=======RECEIPT=======>\n")
            else:
                print("\nInvalid Input!! Try again!!\n")
                continue

        checker = int(input("""Make another transaction?
    1. Yes
    2. No

Enter here: """))
        if checker != 1 and checker != 2:
            print("Invalid Input!!\n")
            break
    except ValueError:
        print("\nInvalid Input!! Try again!!\n")
        break
    except IndexError:
        print("\nInvalid Input!! Try again!!\n")
        break
    else:
        print("\nThank you for visiting ABC Dealership!!\n")
        continue
