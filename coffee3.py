class Coffee:
    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    def keyin(self, key):
        if key == '1':
            if self.water < 250:
                print('Sorry, not enough water!')
                return
            elif self.beans < 16:
                print('Sorry, not enough beans!')
                return
            elif self.cups < 1:
                print('Sorry, not enough cups')
                return
            else:
                print('I have enough resources, making you a coffee!')
                self.water -= 250
                self.beans -= 16
                self.cups -= 1
                self.money += 4

        elif key == '2':
            if self.water < 350:
                print('Sorry, not enough water!')
                return
            elif self.milk < 75:
                print('Sorry, not enough milk')
                return
            elif self.beans < 20:
                print('Sorry, not enough beans!')
                return
            elif self.cups < 1:
                print('Sorry, not enough cups')
                return
            else:
                print('I have enough resources, making you a coffee!')
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.cups -= 1
                self.money += 7

        elif key == '3':
            if self.water < 200:
                print('Sorry, not enough water!')
                return
            elif self.milk < 100:
                print('Sorry, not enough milk')
                return
            elif self.beans < 12:
                print('Sorry, not enough beans!')
                return
            elif self.cups < 1:
                print('Sorry, not enough cups')
                return
            else:
                print('I have enough resources, making you a coffee!')
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.cups -= 1
                self.money += 6

        elif key == 'take':
            print('I gave you $' + str(self.money))
            self.money = 0

        elif key == 'remaining':
            print()
            print('The coffee machine has:')
            print(self.water, 'of water')
            print(self.milk, 'of milk')
            print(self.beans, 'of coffee beans')
            print(self.cups, 'of disposable cups')
            print('$' + str(self.money), 'of money')
        elif key == 'fill':
            global add_water
            global add_milk
            global add_beans
            global add_cups
            self.water += add_water
            self.milk += add_milk
            self.beans += add_beans
            self.cups += add_cups

button = Coffee(400, 540, 120, 9, 550)
while True:
    print()
    print('Write action (buy, fill, take, remaining, exit):')
    action = input()
    if action == 'buy':
        print()
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
        coffee_type = input()
        button.keyin(coffee_type)
    elif action == 'fill':
        print('Write how many ml of water do you want to add:')
        add_water = int(input())
        print('Write how many ml of milk do you want to add:')
        add_milk = int(input())
        print('Write how many grams of coffee beans do you want to add:')
        add_beans = int(input())
        print('Write how many disposable cups of coffee do you want to add:')
        add_cups = int(input())
        button.keyin('fill')

    elif action == 'take':
        button.keyin('take')
    elif action == 'remaining':
        button.keyin('remaining')
    elif action == 'exit':
        quit()
