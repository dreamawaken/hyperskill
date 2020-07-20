class CoffeeMachine:

    espresso = {"water": 250, "milk": 0, "beans": 16, "price": 4}
    latte = {"water": 350, "milk": 75, "beans": 20, "price": 7}
    cappuccino = {"water": 200, "milk": 100, "beans": 12, "price": 6}
    machine_status = {"water": 400, "milk": 540, "beans": 120, "cups": 9, "money": 550}

    def __init__(self):
        self.user_action()

    def user_action(self):
        print()
        while True:
            action = input("Write action (buy, fill, take, remaining, exit): ")
            if action == "buy":
                print()
                choice = input("What do you want to buy? 1 - espresso, "
                               "2 - latte, 3 - cappuccino, back - to main menu: ")
                self.buy_coffee(choice)
            elif action == "fill":
                self.fill_machine()
            elif action == "remaining":
                self.current_state()
            elif action == "take":
                self.take_money()
            elif action == "exit":
                exit()

    def current_state(self):
        print()
        print("The coffee machine has:")
        print(f"{self.machine_status['water']} of water")
        print(f"{self.machine_status['milk']} of milk")
        print(f"{self.machine_status['beans']} of coffee beans")
        print(f"{self.machine_status['cups']} of disposable cups")
        print(f"${self.machine_status['money']} of money")
        print()

    def make_coffee(self, coffee):
        for key in self.machine_status:
            if coffee.get(key) > self.machine_status.get(key):
                print(f"Sorry, not enough {key}!")
                print()
                if key == "cups" and self.machine_status.get(key) < 1:
                    print("Sorry, not enough disposable cups!")
                    print()
                    break
                break
            else:
                print("I have enough resources, making you a coffee!")
                print()
                break
                
        self.machine_status["water"] = self.machine_status.get("water") - coffee.get("water")
        self.machine_status["beans"] = self.machine_status.get("beans") - coffee.get("beans")
        self.machine_status["cups"] = self.machine_status.get("cups") - 1
        self.machine_status["money"] = self.machine_status.get("money") + coffee.get("price")
        return self.machine_status

    def buy_coffee(self, choice):

        if choice == "1":
            self.make_coffee(self.espresso)
        elif choice == "2":
            self.make_coffee(self.latte)
        elif choice == "3":
            self.make_coffee(self.cappuccino)
        elif choice == "back":
            self.user_action()
        else:
            print("No such choice! Returning to main menu.")
            self.user_action()

    def fill_machine(self):
        print()
        self.machine_status["water"] = self.machine_status.get("water") + int(input("Write how many ml of water do you want to add: "))
        self.machine_status["milk"] = self.machine_status.get("milk") + int(input("Write how many ml of milk do you want add: "))
        self.machine_status["beans"] = self.machine_status.get("beans") + int(input("Write how many grams of coffee beans do you want to add: "))
        self.machine_status["cups"] = self.machine_status.get("cups") + int(input("Write how many disposable cups of coffee do you want to add: "))
        return self.machine_status

    def take_money(self):
        print(f"I gave you ${self.machine_status['money']}")
        print()
        self.machine_status["money"] = 0
        return self.machine_status


CoffeeMachine()
