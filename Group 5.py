import pandas as pd

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

brands = pd.Series(list(car_data.keys()))
carDfMap = {
    brand: pd.DataFrame({"Model": models, "Price": prices})
    for brand, (models, prices) in car_data.items()
}

class Cart:
    def __init__(self):
        self.items = []

    def add(self, car_brand, car_model, car_price, payment_mode, months=None):
        self.items.append({
            "brand": car_brand,
            "model": car_model,
            "price": car_price,
            "payment_mode": payment_mode,
            "months": months
        })

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print("\n======= CART =======\n")
        if self.is_empty():
            print("Cart is empty.")
        else:
            for count, item in enumerate(self.items, 1):
                print(f"{count}. {item['brand']} {item['model']} - PHP {item['price']:,} ({item['payment_mode']})")
                if item['payment_mode'] == "Installment":
                    monthly_payment = round(item['price'] / item['months'], 2)
                    print(f"   Installment Period: {item['months']} months")
                    print(f"   Monthly Payment: PHP {monthly_payment:,}")

    def display_receipt(self):
        print("\n======== RECEIPT ========")
        total = 0
        for count, item in enumerate(self.items, 1):
            print(f"{count}. {item['brand']} {item['model']} - PHP {item['price']:,} ({item['payment_mode']})")
            if item['payment_mode'] == "Installment":
                monthly_payment = round(item['price'] / item['months'], 2)
                print(f"   Installment Period: {item['months']} months")
                print(f"   Monthly Payment: PHP {monthly_payment:,}")
            total += item['price']
        print(f"\nTotal Amount: PHP {total:,}")
        print("=========================\n")

    def remove(self, index):
        if 0 <= index < len(self.items):
            removed = self.items.pop(index)
            print(f"Removed {removed['brand']} {removed['model']} from cart.")
        else:
            print("Invalid car number.")

class User:
    def __init__(self):
        self.cart = None

    def choose_brand(self):
        print("\nWELCOME TO ABC DEALERSHIP")
        print("   CHOOSE CAR BRAND:")
        for idx, brand in brands.items():
            print(f"   {idx + 1}. {brand}")
        try:
            choice = int(input("\nCHOSEN BRAND: "))
            if 1 <= choice <= len(brands):
                self.car_brand = brands.iloc[choice - 1]
            else:
                raise ValueError
        except ValueError:
            print("Invalid Input! Try again.")
            return self.choose_brand()

    def choose_model(self):
        df = carDfMap[self.car_brand]
        print(f"\nCHOOSE CAR MODEL FROM {self.car_brand}:")
        for i, row in df.iterrows():
            print(f"   {i + 1}. {self.car_brand} {row['Model']} - PHP {row['Price']:,}")
        try:
            choice = int(input("\nCHOSEN MODEL: "))
            if 1 <= choice <= len(df):
                selected = df.iloc[choice - 1]
                self.car_model = selected['Model']
                self.car_price = selected['Price']
            else:
                raise ValueError
        except ValueError:
            print("Invalid Input! Try again.")
            return self.choose_model()

    def choose_payment(self):
        print("\nCHOOSE MODE OF PAYMENT:")
        print("   1. Cash (10% Discount)")
        print("   2. Installment (5% Interest annually)")
        try:
            choice = int(input("\nCHOSEN PAYMENT: "))
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
        print("\nCHOOSE INSTALLMENT PERIOD (MONTHS):")
        print("12, 24, or 36")
        try:
            self.months = int(input("\nCHOSEN MONTHS: "))
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

    def add_to_cart(self):
        if self.payment_mode == "Installment":
            self.cart.add(self.car_brand, self.car_model, self.car_price, self.payment_mode, self.months)
        else:
            self.cart.add(self.car_brand, self.car_model, self.car_price, self.payment_mode)

def main():
    cart = Cart()
    while True:
        user = User()
        user.cart = cart
        user.choose_brand()
        user.choose_model()
        user.choose_payment()
        user.add_to_cart()
        while True:
            print("\n=====================")
            print("\n1. Add another car")
            print("2. View cart")
            print("3. Remove car from cart")
            print("4. Checkout")
            try:
                action = int(input("\nCHOSEN ACTION: "))
                if action == 1:
                    break  # Add another car
                elif action == 2:
                    cart.display()
                elif action == 3:
                    if cart.is_empty():
                        print("Cart is empty. Nothing to remove.")
                    else:
                        cart.display()
                        try:
                            num = int(input("Enter car number to remove: "))
                            cart.remove(num - 1)
                        except ValueError:
                            print("Invalid input.")
                elif action == 4:
                    if cart.is_empty():
                        print("Cart is empty. Add a car first!")
                    else:
                        cart.display_receipt()
                        print("\nThank you for visiting ABC Dealership!")
                        return
                else:
                    print("Invalid Input! Try again.")
            except ValueError:
                print("Invalid Input! Try again.")

if __name__ == "__main__":
    main()
