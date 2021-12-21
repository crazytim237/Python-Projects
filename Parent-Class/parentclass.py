#Parent Class User
class User:
    name = "Mark"
    email = "mark@gmail.com"
    password = "1234abcd"
    def getLoginInfo (self):
       entry_name = input ("Enter your name: ")
       entry_email = input ("Enter your email: ")
       entry_password = input ("Enter you password: ")
       if (entry_email == self.email and entry_password == self.password):
            print ("Welcome back, {}!".format (entry_name))
       else:
            print ("The password or email is incorrect. ")
#Child Class Employee
class Employee (User):
    base_pay = 11.00
    department = "General"
    pin_number = "3980"
# This is the same method in the parent class "User".
    def getLoginInfo (self):
        entry_name = input ("Enter your name: ")
        entry_email = input ("Enter your email: ")
        entry_pin = input ("Enter your pin: ")
        if (entry_email == self.email and entry_pin == self.pin_number):
            print ("Welcome back, {}!".format (entry_name))
        else:
            print ("The pin or email is incorrect")

#Parent class Vehicle
class Vehicle:
    Energy siurce = Gasoline engine
    Physucal form = Pickup truck
    Number of doors: 2

class Brand (Vehicle)
    Company: Ford
