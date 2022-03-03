"""Question 3:
Define a class named Product with the following specifications:
Data members:

product_id – A string to store product.
product_name - A string to store the name of the product.
product_purchase_price – A decimal to store the cost price of the product.
product_sale_price – A decimal to store Sale Price Margin - A decimal to be calculated as (product_sale_price - product_purchase_price)
Remarks - To store "Profit" if Margin is positive else "Loss" if Margin is negative.
Methods :

A constructor to intialize all the data members with valid default values.
A method set_remarks() that assigns Margin as (product_sale_price - product_purchase_price) and sets Remarks as mentioned below :
![h51](https://user-images.githubusercontent.com/98665012/155852165-694f473b-c1b2-4f35-8cac-74e1db4e6d86.png)

A method set_details() 
to accept values for (product_id. product_name, product_purchase_price, product_sale_price) and invokes SetRemarks() method.
A method get_details() 
that displays all the data members."""

class Product():
#I defined a class named Product    
 #product_id,product_name, product_purchase_price,product_sale_price   
    def __init__(self):
        self.product_id = ""
        self.product_name = ""
        self.product_purchase_price = 0.0
        self.product_sale_price = 0.0
        self.margin= 0.0
        self.remarks= ""
    
    def Set_remarks(self):
        self.margin = int(self.product_sale_price) - int(self.product_purchase_price)
#As it was requested in the question, I subtracted the purchase price from the product sales price and equated it to the margin.
        if self.margin < 0 :
            self.remarks = "Loss"
#If the result is negative, I defined the remark as "Loss". 
        elif self.margin> 0 :
            self.remarks ="Profit"
##If the result is positive, I defined the remark as "Profit".    
   
    def Set_details(self):
        self.product_id = input("Please enter product id")
        self.product_name= input("Please enter product name")
        self.product_purchase_price= input("Please enter product purchase price")
        self.product_sale_price = input("Please enter product sale price")
        self.Set_remarks()
 #I got the values as requested in the question and invoked Set_remarks().
    
    def Get_details(self):
       return f"Your product id is {self.product_id}\nYour product name is {self.product_name}\nYour purchase prise is {self.product_purchase_price}\nYour sale price is {self.product_sale_price}\nYour margin is {self.margin}\nYour earnin status is {self.remarks}"
       
    
# I created get_details() and showed all the data members.
x = Product()       
x.Set_remarks()
x.Set_details()
print(x.Get_details())

