#Question 1

class Cart():
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.cart = []

    def add_to_cart(self, new_item):
        self.cart.append(new_item)
    
    def remove_from_cart(self, new_item):
        if new_item in my_cart:     
            del new_item
            print(f"{new_item} has been removed.")
        else:
            print(f"You dont have any {new_item}s.")
    
    def show_cart(self, new_item):
        for new_item in my_cart.items():
            print(f'\t{new_item}')
    
# class Product:
#     def __init__(self, name, quanity, price):
#         self.name = name
#         self.quantity = quantity
#         self.price = price
        
#     def get_product_total(self):
#         return self.quantity * self.price
    
    
def run():
    cust_name = input('Welcome. What is your name? ')
    my_cart = Cart(cust_name)
    while True:
        ask = input('What would you like to do? Add/Remove/Show/Quit ').lower()
        if ask == 'quit':
            break
        elif ask == 'add':
            item = input('What would you like to add? ')
            my_cart.add_to_cart(item)
        elif ask == 'remove':
            item = input('What would you like to remove')
            my_cart.remove_from_cart(item)
        elif ask == 'show':
            show_cart(item)
            
            
            
    
run()


#Question 2

class Animal:
    
    def __init__(self, name, energy_level=50):
        self.name = name
        self.energy_level = energy_level
        
    def play(self, num):
        unit_decrease = num // 5
        self.energy_level -= unit_decrease # self.gas_level = self.gas_level - unit_decrease
        print(f"{self.name} is playing for {num} minutes. His energy level is now {self.energy_level}")
        
    def eat(self, fuel):
        unit_increase = fuel * 10
        self.energy_level += unit_increase
        print(f"{self.name} is eating for {fuel} minutes. His energy level is now {self.energy_level}")
        
    def sleep(self, fuel):
        unit_increase = fuel * 10
        self.energy_level += unit_increase
        print(f"{self.name} is sleeping for {fuel} minutes. His energy level is now {self.energy_level}")
        
buddy1 = Animal('Snake')
buddy2 = Animal('Frog')
buddy3 = Animal('Gecko')


buddy1.play(25)
buddy1.sleep(3)

buddy2.eat(2)