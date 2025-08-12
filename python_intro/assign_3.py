def calculate_discount(price, discount_percent):
    """ Applies a discount if discount_percent is 20 or higher """
    if (discount_percent >= 20):
        price *= (1 - discount_percent/100)
    return price

item_price = float(input("Enter original price: "))
item_discount = float(input("Enter discount percentage (1-49): "))
item_price = calculate_discount(item_price, item_discount)
print(item_price)
