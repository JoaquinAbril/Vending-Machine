# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 18:44:21 2023

@author: hp
"""


class VendingMachine:
    def __init__(self):
        self.products = {
            'A1': {'name': 'Kangkong Chips 🍃', 
                   'price': 14.99, 
                   'quantity': 999, 
                   'description': '"Kangkong Chips ni Josh Mojica!"'},
            'A2': {'name': 'Kwek Kwek 🥚',
                   'price': 2.50, 
                   'quantity': 43, 
                   'description': '"Egg Waffles So Good!"'},
            'B1': {'name': 'Heaven Tsokolit 🍫', 
                   'price': 3.00, 
                   'quantity': 50, 
                   'description': '"Unang Kagat, langit agad!"'},
            'B2': {'name': 'Redhorse 🍺', 
                   'price': 12.99, 
                   'quantity': 34, 
                   'description': '"Redhorse! Extra Strong!"'},
            'C1': {'name': 'Lechon 🐖',
                   'price': 75.00, 
                   'quantity': 12, 
                   'description': '"Unang Subo, Highblood Agad! RAAAH!"'},
            'C2': {'name': 'McLaren 720s 🏎️', 
                   'price': 9980.00, 
                   'quantity': 3, 
                   'description': '"Prepare, Commit, Belong!"'},
            'D1': {'name': 'KathNiel CB 👩‍❤️‍👨',
                   'price': 9999.00, 
                   'quantity': 1, 
                   'description': '"She\'s Dating the Gangster 2"'},
            'D2': {'name': 'Spotify Premium 🎶', 
                   'price': 21.99, 
                   'quantity': 20, 
                   'description': '"Music Wherever You Go!"'},
            'E1': {'name': 'iPhone 15 Pro Max 📱', 
                   'price': 5499.00, 
                   'quantity': 6, 
                   'description': '"Think Different!"'}
        }
        self.balance = 0.0

    def display_products(self):
        print("\n👾👾👾 WELCOME TO WACKY'S BOGART VENDING MACHINE!👾👾👾")
        print("=========================================================")
        print("   Code    |       Product       |  Price  |  Quantity  ")
        print("---------------------------------------------------------")
        for code, product in self.products.items():
            print(f"    {code}      | {product['name']:<20} |  AED {product['price']:.2f}  |   {product['quantity']}")
            print("            | -------------------------------------------")
            print(f"            | {product['description']:<42} |")
            print("---------------------------------------------------------")

    def insert_money(self):
        while True:
            try:
                amount = float(input("Insert your money you broke ahh college student! (in dirhams pls 😓): "))
                if amount > 0:
                    self.balance += amount
                    print(f"Inserted AED {amount}. Current balance: AED {self.balance}")
                    break
                else:
                    print("Please insert a positive amount.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def purchase_product(self):
        self.display_products()
        code = input("Enter the product code to purchase: ").upper()

        if code in self.products:
            product = self.products[code]
            if product['quantity'] > 0 and self.balance >= product['price']:
                self.balance -= product['price']
                product['quantity'] -= 1
                print(f"Dispensing {product['name']}. Remaining balance: AED {self.balance}")
                self.give_change()
            else:
                print("YOU BROKE BRO!.")
        else:
            print("Invalid product code.")

    def give_change(self):
        if self.balance > 0:
            print(f"Returning change: AED {self.balance}")
            self.balance = 0.0
        else:
            print("No change to return, homie.")

def run_vending_machine():
    vm = VendingMachine()

    while True:
        print("\n🤪👉👉 WELCOME TO WACKY'S BOGART VENDING MACHINE! 👈👈🤪")
        print("1. Display Products 🛒")
        print("2. Insert Money 💵")
        print("3. Purchase Product 🛒")
        print("4. Exit ❌")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            vm.display_products()
        elif choice == '2':
            vm.insert_money()
        elif choice == '3':
            vm.purchase_product()
        elif choice == '4':
            print("🎉🎉🎉 Arigato so much for using Wacky's Bogart Vending Machine! 🎉🎉🎉")
            print("             Pls come again and give all your money to me!")
            print("    🤪👉👉 YOU! YOU! YOU! YOU! YOU! YOU! YOU! YOU! YOU! YOU! ✋✋🤪")
            break
        else:
            print("Are you dumb bro? I said choose a number from 1 to 4!")

if __name__ == "__main__":
    run_vending_machine()
    


