from abc import ABC, abstractmethod
#from packaging import Packaging
#from payable import Payable, PayType
#from tabulate import tabulate, SEPARATING_LINE

from typing import Protocol
from enum import Enum

class PayType(Enum):
    CASH = "CASH"
    CARD = "CARD"
    PHONE = "PHONE"

class Payable(Protocol):
    def get_pay_type(self) -> PayType:
        ...
    
    def set_pay_type(self, payment_method: PayType) -> None:
        ...
class Packaging(Protocol):
    packaging: str
class DessertItem(ABC, Packaging):
    def __init__(self, name: str = "", tax_percent: float = 7.25):
        self.name = name
        self.tax_percent = tax_percent

    @abstractmethod
    def calculate_cost(self):
        pass  # To be implemented in subclasses

    def calculate_tax(self):
        return round(self.calculate_cost() * (self.tax_percent / 100), 2)


class Candy(DessertItem):
    def __init__(self, name: str = "", candy_weight: float = 0.0, price_per_pound: float = 0.0,
                 tax_percent: float = 7.25, packaging = "Bag"):
        super().__init__(name, tax_percent)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound

    def calculate_cost(self):
        return round(self.candy_weight * self.price_per_pound, 2)

    def __str__(self):
        total_cost = self.calculate_cost()
        tax = self.calculate_tax()
        return (f"{self.name} (Bag)\n"
                f"-    {self.candy_weight} lbs. @ ${self.price_per_pound:.2f}/lb:, "
                f"${total_cost:.2f}, [Tax: ${tax:.2f}]")


class Cookie(DessertItem):
    def __init__(self, name: str = "", cookie_quantity: int = 0, price_per_dozen: float = 0.0,
                 tax_percent: float = 7.25, packaging = "Box"):
        super().__init__(name, tax_percent)
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen

    def calculate_cost(self):
        return round((self.cookie_quantity / 12) * self.price_per_dozen, 2)

    def __str__(self):
        total_cost = self.calculate_cost()
        tax = self.calculate_tax()
        return (f"{self.name} Cookies (Box)\n"
                f"-    {self.cookie_quantity} cookies @ ${self.price_per_dozen:.2f}/dozen: "
                f"${total_cost:.2f}, [Tax: ${tax:.2f}]")


class Icecream(DessertItem):
    def __init__(self, name: str = "", scoop_count: int = 0, price_per_scoop: float = 0.0,
                 tax_percent: float = 7.25, packaging = "Bowl"):
        super().__init__(name, tax_percent)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop

    def calculate_cost(self):
        return round(self.scoop_count * self.price_per_scoop, 2)

    def __str__(self):
        total_cost = self.calculate_cost()
        tax = self.calculate_tax()
        return f"{self.name} Ice Cream (Bowl)\n-    {self.scoop_count} scoops @ ${self.price_per_scoop:.2f}/scoop: ${total_cost:.2f}, [Tax: ${tax:.2f}]"
        #return f"{self.name} Ice Cream (Bowl)\n-{" "*4}{self.scoop_count} scoops @ ${self.price_per_scoop:.2f}/scoop:, ${total_cost:.2f}, [Tax: ${tax:.2f}]"


class Sundae(Icecream):
    def __init__(self, name: str = "", scoop_count: int = 0, price_per_scoop: float = 0.0,
                 topping_name: str = "", topping_price: float = 0.0, tax_percent: float = 7.25, packaging = "boat"):
        super().__init__(name, scoop_count, price_per_scoop, tax_percent)
        self.topping_name = topping_name
        self.topping_price = topping_price

    def calculate_cost(self):
        return round(super().calculate_cost() + self.topping_price, 2)

    def __str__(self):
        total_cost = self.calculate_cost()
        tax = self.calculate_tax()
        return (f"{self.name} Sundae with {self.topping_name} (Boat)\n"
                f"-    {self.scoop_count} scoops @ ${self.price_per_scoop:.2f}/scoop,  "
                f"${self.topping_price:.2f} topping: ${total_cost:.2f}, [Tax: ${tax:.2f}]")




class Order(Payable):
    def __init__(self, payment_method="Cash"):
        self.order = []
        self.payment_method = PayType.CASH  # Default to PayType.CASH
        self.set_pay_type(payment_method)  # Validate and set payment method, can accept 'Cash', 'Card', 'Phone'

    def add_item(self, item):
        self.order.append(item)

    def __len__(self):
        return len(self.order)

    def order_cost(self):
        return round(sum(item.calculate_cost() for item in self.order), 2)

    def order_tax(self):
        return round(sum(item.calculate_tax() for item in self.order), 2)
    
    def get_pay_type(self) -> PayType:
        return self.payment_method

    def set_pay_type(self, payment_method: PayType | str) -> None:
        """ Set the payment method based on the input."""
        if isinstance(payment_method, str):
            payment_method = payment_method.strip().upper()
            if payment_method in PayType.__members__:
                self.payment_method = PayType[payment_method]
            else:
                raise ValueError("Invalid payment method entered. Please enter CASH, CARD, or PHONE.")
        elif isinstance(payment_method, PayType):
            self.payment_method = payment_method
        else:
            raise ValueError("Invalid payment method type. Please enter a valid PayType value or a string.")
    
    def get_totals(self):
        table_data = []
        subtotal = 0
        total_tax = 0

        for item in self.order:
            cost = item.calculate_cost()
            tax = cost * (item.tax_percent / 100)
            subtotal += cost
            total_tax += tax
    
        total_cost = subtotal + total_tax
        total_items = len(self.order)

        table_data.append(["Total number of items in order:", "", total_items])
        table_data.append(["Order Subtotal:", f"${subtotal:.2f}", f"${total_tax:.2f}"])
        table_data.append(["Order Total:", "", f"${total_cost:.2f}"])
        return tabulate(table_data, tablefmt="plain")

    def to_list(self):
        result = []
        for item in self.order:
          inter_list= f"{str(item)}".split("\n")
          print(inter_list)
          final_list = [inter_list.split(", ") for i in inter_list]
          print(final_list)
          for item_i in final_list:
            result.append(item_i)
       

        '''
        for item in self.order:
            result.append(item.__str__())
            
        # if result:  # Add separator if there are items
        #     result.append("---------------------------")  # Ensure only one separator at the top

        totals = self.get_totals().strip()  # Strip unnecessary newlines from totals
        if totals:
            result.append(totals)

        #result.append("---------------------------")  # Ensure only one at the bottom

        return "\n".join(result) + f"\nPaid with {self.payment_method.value}"
'''
    def __str__ (self):
        return [self.to_list()]  # Using __str__ method directly
