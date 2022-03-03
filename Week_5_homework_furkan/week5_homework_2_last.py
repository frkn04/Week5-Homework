"""Question 2:
Define a class named ``ItemInfo` with the following description:
item_code(Item Code), item(item name), price(Price of each item), qty(quantity in stock), discount(Discount percentage on the item), net_price(Price after discount)

Methods :
A member method calculate_discount() to calculate discount as per the following rules:
If qty <= 10 —> discount is 0
If qty (11 to 20 inclusive) —> discount is 15
If qty >= 20 —> discount is 20
A constructor init method to assign the initial values for item_code to 0 and price, qty, net_price and discount to null
A function called buy() to allow user to enter values for item_code, item, price, qty. Then call function calculate_discount() to calculate the discount and net_price(price * qty - discount).
A function show_all() or similar name to allow user to view the content of all the data members."""

class ItemInfo():
#I created the class as requested in the question.
    def __init__(self):
        self.item_code = 0
        self.price= 0
        self.qty= 0
        self.net_price= 0
        self.discount= 0

    def calculate_discount(self):
 #I created a method as requested in the question to find the discount rate.
 #I specified the range of the ratio with if elif in it.
        if self.qty <=10:
            self.discount = 0
        elif self.qty > 10 and self.qty < 20:
            self.discount =15
        elif self.qty >= 20:
            self.discount =20
    
    def buy(self):
#I created a new method and requested the inputs.
        self.item_code = input("Please enter item code:")
        self.price = int(input("Please enter price:"))    
        self.qty = int(input("Please enter quantity in stock"))
#It wanted me to call the method I created earlier in the question and find the net price. I did. 
        self.calculate_discount()
        self.net_price = (self.price * self.qty ) - self.discount/100
    
    def show_all(self):
#I created a new method that displays all of them. 
        print(f"Your item code is {self.item_code}")
        print(f"Your item's price is {self.price}")
        print(f"Your item's quantity in stock {self.qty}")
        print(f"Your item's discount is {self.discount}")
        print(f"Your item's net price is {self.net_price}")

x = ItemInfo()
x.buy()
x.calculate_discount()
print(x.show_all())
    