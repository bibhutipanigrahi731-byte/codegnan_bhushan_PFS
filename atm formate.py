#ATM
'''
'''
class ATM:

    def __init__(self):
        self.user_information = {
            "Name": "Mohith_Ram",
            "contact": "",
            "ATM PIN": "2435",
            "Balance": 1200000,
            "Transaction history": []
        }

    def check_balance(self):
        print(f"Current Balance : {self.user_information['Balance']}")

    def withdraw_money(self):
        amount = int(input("Enter amount to withdraw: "))

        if amount <= self.user_information["Balance"]:
            if amount >= 100 and amount % 100 == 0:
                self.user_information["Balance"] -= amount
                self.user_information["Transaction history"].append(
                    f"Withdraw : {amount}"
                )
                print("Please collect your cash")
                print(
                    f"Remaining Balance : {self.user_information['Balance']}"
                )
            else:
                print("Enter amount in multiples of 100")
        else:
            print("Insufficient Balance")

    def deposit_money(self):
        amount = int(input("Enter amount to deposit: "))

        if amount > 0:
            self.user_information["Balance"] += amount
            self.user_information["Transaction history"].append(
                f"Deposited : {amount}"
            )
            print("Amount Deposited Successfully")
            print(
                f"Updated Balance : {self.user_information['Balance']}"
            )
        else:
            print("Invalid Amount")

    def mini_statement(self):
        print("\n----- MINI STATEMENT -----")

        if not self.user_information["Transaction history"]:
            print("No transactions available")
        else:
            for transaction in self.user_information["Transaction history"]:
                print(transaction)

        print(
            f"Available Balance : {self.user_information['Balance']}"
        )

    def change_pin(self):
        old_pin = input("Enter Old PIN: ")

        if old_pin == self.user_information["ATM PIN"]:
            new_pin = input("Enter New 4-Digit PIN: ")

            if len(new_pin) == 4 and new_pin.isdigit():
                confirm_pin = input("Confirm New PIN: ")

                if new_pin == confirm_pin:
                    self.user_information["ATM PIN"] = new_pin
                    print("PIN Changed Successfully")
                else:
                    print("PIN Mismatch")
            else:
                print("PIN must contain exactly 4 digits")
        else:
            print("Incorrect Old PIN")

    def menu(self):
        while True:
            print("\n------ ATM MENU ------")
            print("1. Check Balance")
            print("2. Withdraw Money")
            print("3. Deposit Money")
            print("4. Mini Statement")
            print("5. Change PIN")
            print("6. Exit")

            choice = int(input("Enter Choice: "))

            if choice == 1:
                self.check_balance()

            elif choice == 2:
                self.withdraw_money()

            elif choice == 3:
                self.deposit_money()

            elif choice == 4:
                self.mini_statement()

            elif choice == 5:
                self.change_pin()

            elif choice == 6:
                print("Thank you for using ATM")
                break

            else:
                print("Invalid Choice")

    def verify_pin(self):
        attempts = 3

        while attempts > 0:
            pin = input("Enter ATM PIN: ")

            if pin == self.user_information["ATM PIN"]:
                print("Login Successful")
                self.menu()
                return

            attempts -= 1

            if attempts > 0:
                print(f"Invalid PIN! Attempts Left: {attempts}")
            else:
                print("Your Card Has Been BLOCKED")


# Main Program
print("-----* PLEASE INSERT YOUR CARD *-----")

atm = ATM()
atm.verify_pin()








