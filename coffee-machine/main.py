from coffee_menu import menu, resources

money = 0
water_source = resources["water"]
milk_source = resources["milk"]
coffee_source = resources["coffee"]


def coffee_order(order):
    amount = menu[order]

    water = amount["ingredients"]["water"]
    coffee = amount["ingredients"]["coffee"]
    milk = amount["ingredients"]["milk"]

    return water, milk, coffee


def payment(order):
    print("Please insert coins.")

    quarter = float(input('how many quarter? '))
    dime = float(input('how many dimes? '))
    nickle = float(input('how many nickles? '))
    penny = float(input('how many pennies? '))

    cost = menu[order]["cost"]
    pay = quarter*0.25 + dime*0.10 + nickle*0.05 + penny*0.01

    if pay >= cost:
        change = pay - cost
        global money
        money += cost
        return f'Here is ${round(change,2)} in change'
    else:
        return "Sorry that's not enough money. Money refunded."


def resources_left(order):

    global water_source, milk_source, coffee_source

    if water_source >= order[0]:
        if milk_source >= order[1]:
            if coffee_source >= order[2]:
                water_source -= order[0]
                milk_source -= order[1]
                coffee_source -= order[2]
                return True
            else:
                print('Sorry there is not enough coffee.')
                return False
        else:
            print('Sorry there is not enough milk.')
            return False
    else:
        print('Sorry there is not enough water.')
        return False


def report():
    print(f'Water: {water_source} ml')
    print(f'Milk: {milk_source} ml')
    print(f'Coffee: {coffee_source} g')
    print(f'Money: ${round(money,2)}')


def check_resource_unavailability():
    if water_source < 50:
        print('\nThe water is run out')
        return True
    elif milk_source < 100:
        print('\nThe milk is run out')
        return True
    elif coffee_source < 24:
        print('\nThe coffee is run out')
        return True
    else:
        return False


def main():
    # Loop coffee menu until not True
    is_stop = False
    while not is_stop:
        user_order = input('\tWhat would you like? (espresso/latte/cappuccino): ')

        if user_order == "report":
            report()

        elif user_order == "espresso" or user_order == "latte" or user_order == "cappuccino":
            order = coffee_order(user_order)
            # Check resources first before jump into payment access
            if resources_left(order):
                print(payment(user_order))
                print(f"Here is your {user_order} ☕ . Enjoy!")

        elif user_order == "off":
            is_stop = True

        else:
            continue

        if check_resource_unavailability():
            is_stop = True


if __name__ == '__main__':
    main()
