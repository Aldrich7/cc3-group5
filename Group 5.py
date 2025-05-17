# CAR MODELS, BRANDS, AND PRICES
car_data = {
    "Honda": (["City", "Civic", "CRV", "Accord", "Jazz", "HR-V", "Pilot", "Odyssey", "Brio", "Passport"],
              [1000000, 1500000, 2000000, 1800000, 1300000, 1700000, 2500000, 3000000, 900000, 2200000]),
    "Toyota": (["Vios", "Fortuner", "Innova", "Corolla", "Camry", "Hilux", "Land Cruiser", "RAV4", "Yaris", "Avalon"],
               [2000000, 2500000, 3000000, 2200000, 2700000, 3200000, 3700000, 2400000, 1900000, 2800000]),
    "Aurelio": (["GT", "RT", "XT", "ST", "LT", "MT", "PT", "QT", "UT", "VT"],
                [3000000, 3500000, 4000000, 3200000, 3700000, 4200000, 4500000, 3800000, 3400000, 3600000]),
    "Ford": (["Ranger", "Mustang", "Explorer", "F-150", "Escape", "Edge", "Bronco", "Fusion", "Taurus", "Expedition"],
             [1500000, 2000000, 2500000, 3000000, 1800000, 2300000, 2800000, 2100000, 2600000, 3500000]),
    "Mitsubishi": (["Mirage", "Montero", "Strada", "Pajero", "Lancer", "Outlander", "Xpander", "ASX", "Eclipse Cross", "Triton"],
                   [1200000, 1800000, 2300000, 2800000, 1500000, 2000000, 2500000, 1700000, 2200000, 2700000]),
    "BMW": (["Series 3", "Series 5", "Series 7", "X1", "X3", "X5", "Z4", "i8", "M3", "M5"],
            [3000000, 4000000, 5000000, 3500000, 4500000, 5500000, 6000000, 7000000, 8000000, 9000000]),
    "Mercedes": (["A-Class", "C-Class", "E-Class", "S-Class", "GLA", "GLC", "GLE", "GLS", "AMG GT", "EQC"],
                 [3200000, 4200000, 5200000, 6200000, 3700000, 4700000, 5700000, 6700000, 7700000, 8700000]),
    "Audi": (["A3", "A4", "A6", "A8", "Q3", "Q5", "Q7", "Q8", "TT", "R8"],
             [3100000, 4100000, 5100000, 6100000, 3600000, 4600000, 5600000, 6600000, 7600000, 8600000]),
    "Chevrolet": (["Spark", "Malibu", "Impala", "Camaro", "Equinox", "Traverse", "Tahoe", "Suburban", "Blazer", "Trailblazer"],
                  [1500000, 2500000, 3500000, 4500000, 2000000, 3000000, 4000000, 5000000, 6000000, 7000000]),
    "Nissan": (["Micra", "Sunny", "Altima", "Maxima", "Juke", "Qashqai", "X-Trail", "Patrol", "GT-R", "370Z"],
               [1400000, 2400000, 3400000, 4400000, 1900000, 2900000, 3900000, 4900000, 5900000, 6900000])
}

class User:
    def choose_brand(self):
        print("   WELCOME TO ABC DEALERSHIP")
        print("   CHOOSE CAR BRAND:")
        for idx, brand in enumerate(car_data, start=1):
            print(f"   {idx}. {brand}")
        try:
            choice = int(input("CHOSEN BRAND: "))
            if 1 <= choice <= len(car_data):
                self.car_brand = list(car_data)[choice - 1]
            else:
                raise ValueError
        except ValueError:
            print("Invalid Input! Try again.")
            return self.choose_brand()

    def choose_model(self):
        models, prices = car_data[self.car_brand]
        print(f"\n   CHOOSE CAR MODEL FROM {self.car_brand}:")
        for idx, (model, price) in enumerate(zip(models, prices), start=1):
            print(f"   {idx}. {self.car_brand} {model} - PHP {price:,}")
        try:
            choice = int(input("CHOSEN MODEL: "))
            if 1 <= choice <= len(models):
                self.car_model, self.car_price = models[choice - 1], prices[choice - 1]
            else:
                raise ValueError
        except ValueError:
            print("Invalid Input! Try again.")
            return self.choose_model()

    def choose_payment(self):
        print("\n   CHOOSE MODE OF PAYMENT:")
        print("   1. Cash (10% Discount)")
        print("   2. Installment (5% Interest annually)")
        try:
            choice = int(input("CHOSEN PAYMENT: "))
            if choice == 1:
                self.payment_mode = "Cash"
                self.car_price = round(self.car_price * 0.90, 2)
            elif choice == 2:
                self.payment_mode = "Installment"
                self.choose_installment()
            else:
                print("Invalid Input! Try again.")
                self.choose_payment()
        except ValueError:
            print("Invalid Input! Try again.")
            self.choose_payment()

    def choose_installment(self):
        print("\n   CHOOSE INSTALLMENT PERIOD (MONTHS):")
        print("   12, 24, or 36")
        try:
            self.months = int(input("CHOSEN MONTHS: "))
            if self.months in [12, 24, 36]:
                annual_interest_rate = 0.05
                total_interest = annual_interest_rate * (self.months / 12)
                self.car_price = round(self.car_price * (1 + total_interest), 2)
            else:
                print("Invalid Input! Try again.")
                self.choose_installment()
        except ValueError:
            print("Invalid Input! Try again.")
            self.choose_installment()

    def display_receipt(self):
        print("\n<=======RECEIPT=======>")
        print(f"Chosen Car: {self.car_brand} {self.car_model}")
        print(f"Total Amount: PHP {self.car_price:,}")
        if self.payment_mode == "Installment":
            monthly_payment = round(self.car_price / self.months, 2)
            print(f"Installment Period: {self.months} months")
            print(f"Monthly Payment: PHP {monthly_payment:,}")
        print("<=======RECEIPT=======>\n")

def main():
    while True:
        user = User()
        user.choose_brand()
        user.choose_model()
        user.choose_payment()
        user.display_receipt()
        try:
            another = int(input("Make another transaction? (1. Yes, 2. No): "))
            if another != 1:
                print("\nThank you for visiting ABC Dealership!")
                break
        except ValueError:
            print("\nInvalid Input! Exiting.")
            break

if __name__ == "__main__":
    main()
