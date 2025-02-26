from dessert import DessertItem, Candy, Cookie, IceCream, Sundae, Order

if __name__ == "__main__":
    new_order = Order()

    candycorn = Candy("Candy Corn", 1.5, .25)
    bears = Candy("Gummy Bears", .25, .35)
    cookie = Cookie("Chocolate Chip", 6, 3.99)
    icecream = IceCream("Pistachio", 2, .79)
    sundae = Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29)
    cookie2 = Cookie("Oatmeal Raisin", 2, 3.45)

    new_order.add_item(candycorn)
    new_order.add_item(bears)   
    new_order.add_item(cookie)
    new_order.add_item(icecream)
    new_order.add_item(sundae)
    new_order.add_item(cookie2)

    for item in new_order.order:
        print(item.name)

    print(f"Total number of items in order: " + str(new_order.__len__()))