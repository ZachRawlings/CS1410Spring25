from dessert import DessertItem, Candy, Cookie, Icecream, Sundae, Order
from tabulate import tabulate
#from payable import Payable, PayType

class DessertShop:
    def get_input(self, prompt, value_type=str, min_value=None):
        """A simple reusable function for validating input."""
        while True:
            user_input = input(prompt).strip()
            if not user_input:
                print("Input cannot be empty. Try again.")
                continue
            try:
                value = value_type(user_input)
                if min_value is not None and value < min_value:
                    print(f"Value must be at least {min_value}. Try again.")
                else:
                    return value
            except ValueError:
                print(f"Please enter a valid {value_type.__name__}.")

    def user_prompt_candy(self):
        name = self.get_input("Enter name of candy: ")
        weight = self.get_input("Enter weight (lbs): ", float, 0.01)
        price_per_pound = self.get_input("Enter price per pound: ", float, 0.01)
        return Candy(name, weight, price_per_pound)

    def user_prompt_cookie(self):
        name = self.get_input("Enter name of cookie: ")
        quantity = self.get_input("Enter amount of cookies: ", int, 1)
        price_per_dozen = self.get_input("Enter price per dozen: ", float, 0.01)
        return Cookie(name, quantity, price_per_dozen)

    def user_prompt_icecream(self):
        name = self.get_input("Enter the type of ice cream: ")
        scoops = self.get_input("Enter the number of scoops: ", int, 1)
        price_per_scoop = self.get_input("Enter the price per scoop: ", float, 0.01)
        return Icecream(name, scoops, price_per_scoop)

    def user_prompt_sundae(self):
        name = self.get_input("Enter the type of ice cream: ")
        scoops = self.get_input("Enter the number of scoops: ", int, 1)
        price_per_scoop = self.get_input("Enter the price per scoop: ", float, 0.01)
        topping = self.get_input("Enter the topping: ")
        topping_price = self.get_input("Enter the price for topping: ", float, 0.0)  # Allows free toppings
        return Sundae(name, scoops, price_per_scoop, topping, topping_price)
    
    # def user_prompt_payment(self):
    #   while True:
    #     payment = input("Enter payment type (Cash, Card, Phone): ").strip().upper()
    #     if payment in PayType.__members__:
    #         return PayType[payment]  # Return a valid PayType enum
    #     print("Invalid payment type. Please enter Cash, Card, or Phone.")


def main():
    shop = DessertShop()
    order = Order()

    done = False
    prompt = '\n'.join([
        '\n',
        '1: Candy',
        '2: Cookie',
        '3: Ice Cream',
        '4: Sundae',
        '5: Payment'
        '\nWhat would you like to add to the order? (1-4, Enter for done): '
    ])

    while not done:
        choice = input(prompt).strip()
        match choice:
            case '':
                done = True
            case '1':
                item = shop.user_prompt_candy()
                order.add_item(item)
                print(f'{item.name} has been added to your order.')
            case '2':
                item = shop.user_prompt_cookie()
                order.add_item(item)
                print(f'{item.name} has been added to your order.')
            case '3':
                item = shop.user_prompt_icecream()
                order.add_item(item)
                print(f'{item.name} has been added to your order.')
            case '4':
                item = shop.user_prompt_sundae()
                order.add_item(item)
                print(f'{item.name} has been added to your order.')
            case '5':
                item = shop.user_prompt_payment()  # This returns a PayType enum
                order.set_pay_type(item)  # Pass it directly
                print(f'You will be paying with {order.get_pay_type().value}.')

            case _:
                print('Invalid response: Please enter a choice from the menu (1-4) or press Enter to finish.')

    # print("\nReceipt:\n")

    # table_data = []
    # subtotal = 0
    # total_tax = 0

    # for item in order.order:
    #     cost = item.calculate_cost()
    #     tax = cost * (item.tax_percent / 100)
    #     subtotal += cost
    #     total_tax += tax
    # #     table_data.append(item.__str__().split(", "))
    # #     # print(item)
    # #     # print(item.__str__().split(", "))
    
    # total_cost = subtotal + total_tax
    # total_items = len(order.order)
  

    # # Adding summary rows
    # table_data.append(["Total number of items in order:", "", total_items])
    # table_data.append(["Order Subtotal:", f"${subtotal:.2f}", f"${total_tax:.2f}"])
    # table_data.append(["Order Total:", "", f"${total_cost:.2f}"])
    
    
    # print(table_data)
    # # headers = ["Dessert", "Cost", "Tax"]
    print("done")
    print(tabulate(order.to_list(), tablefmt="fsql"))
    #print(tabulate(table_data, tablefmt="plain"))

    

main()