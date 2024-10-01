# 17) Define a class, called Lunch, with __init__() method should have two arguments, self and menu, where menu is a
# string. Add a method called menu_price. It will involve an if statement: if "menu 1" then print "Price 12.00",
# if "menu 2" then print "Price 13.40", else print "Error in menu". Test with Paul = Lunch("menu 1") and call
# Paul.menu_price().

class Lunch:

    def __init__(self, menu):
        self.menu = menu

    def menu_price(self):
        if self.menu == "menu 1":
            print("Price 12.00")
        elif self.menu == "menu 2":
            print("Price 13.40")
        else:
            print("Error in menu")


menu_in = input('Select menu (eg. menu 1): ')
Paul = Lunch(menu_in.lower())
Paul.menu_price()
