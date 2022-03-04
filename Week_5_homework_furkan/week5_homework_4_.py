class İtems():
   end_price=0
   def __init__(self,items=0, total_price=0, discount=0, price_tobe_paid=0, qty=0,item_price=0):
       self.items = items
       self.total_price = total_price
       self.discount = discount
       self.price_tobe_price = price_tobe_paid
       self.qty =qty
       self.item_price = item_price
       self.shop_list = []
   def calculate_discount(self):
         
        if self.total_price >= 4000:
            self.discount = 25
        elif self.total_price >= 2000:
            self.discount = 15 
        elif self.total_price < 2000:
            self.discount = 10
   def shopping_cart(self):
      
       while True:
            self.items = input("Please enter items name:")
            try:
                self.item_price= int(input("Please enter item price:"))
                self.qty = int(input("Please enter how many want you buy:"))
                self.shop_list.append([self.items, self.qty, self.item_price])
            except ValueError:
                print("Please enter with number")
            a = input("Do you want to continue? Y/N")
            self.total_price = self.item_price * self.qty
            İtems.end_price = İtems.end_price + self.total_price
            if a == "Y" or a== "y":
                continue
            else : 
                print("Thank You")
            #print(f"Your product is{self.shop_list[0]}\nYour product quantity is{self.shop_list[1]}\nYour total price is {İtems.end_price}")
                break
   def get_total_amount(self):
       self.price_tobe_price =İtems.end_price -( İtems.end_price * (self.discount/100 ))
       return self.price_tobe_price
   def __str__(self):
       print(f"Your shop list is {self.shop_list}\nYour discount is {self.discount}\nYou should pay {self.price_tobe_price}")
class Customer():  
    def __init__(self, cus_name='', cus_lname='', cus_id='') :
        self.cust_name = cus_name
        self.cus_lname= cus_lname
        self.cus_id= cus_id
        self.cus_info = []
    def get_cust_info(self):
        self.cust_name = input("Please enter your name:")
        self.cus_lname = input("Please enter your last name:")
        self.cus_id = input("Please enter your id")
        self.cus_info.append([self.cust_name,self.cus_lname,self.cus_id])
    def __str__(self):
        print(f"Customer name is {self.cust_name}\nCustomer last name is {self.cus_lname}\nCustomer id is {self.cus_id}")
per = Customer()        
per.get_cust_info()
a = İtems()
a.calculate_discount()
a.shopping_cart()
a.get_total_amount()
print(a.__str__())
print(per.__str__())