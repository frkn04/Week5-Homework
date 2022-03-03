"""Question 1:
Create the class Society with following information:
society_name,house_no_of_mem, flat, income

Methods :
An __init__ method to assign initial values of society_name,house_no_of_mem, flat, income
input_data() To read information from members
allocate_flat() To allocate flat according to income using the below table.
show_data() to display the details of the entire class.
![h5](https://user-images.githubusercontent.com/98665012/155852098-3b9c4c90-149e-4685-8cb1-44001a6088bc.png"""

class Society():
#I created a class called Society.
    def __init__(self, society_name, house_no, flat, income):
        #I started it as requested in the question.
        self.society_name = mem_soc_name
        self.house_no= mem_house_no
        self.flat = flat
        self.income = mem_income
        

    def showdata():
#I created a new function to show what range it is in.
            if mem_income < 15000:
                flat = "D"
                print(f"Your Society name is {mem_soc_name}\nYour house no is {mem_house_no}\nYour income {mem_income}\nAnd your statu is {flat}")
            elif mem_income >= 15000 and mem_income < 20000 :
                flat = "C"
                print(f"Your Society name is {mem_soc_name}\nYour house no is {mem_house_no}\nYour income {mem_income}\nAnd your statu is {flat}")
            elif mem_income >= 2000 and mem_income < 25000 :
                flat = "C"
                print(f"Your Society name is {mem_soc_name}\nYour house no is {mem_house_no}\nYour income {mem_income}\nAnd your statu is {flat}")
            elif mem_income >= 2500 :
                flat = "C"
                print(f"Your Society name is {mem_soc_name}\nYour house no is {mem_house_no}\nYour income {mem_income}\nAnd your statu is {flat}")
                
            
mem_soc_name = input("Please enter the society name")
mem_house_no= input("Please enter the house number")
mem_income= int(input("Plese enter your income"))
#I created 3 different entries. I also synced them to the partition I initialized inside the first class.
Society.showdata()
#I called the show data function inside the society class I created.
print("Thank you")







