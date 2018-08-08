# Create a class called  Car. In the __init__(), allow the user to specify the following attributes: price, speed, fuel, mileage. If the price is greater than 10,000, set the tax to be 15%. Otherwise, set the tax to be 12%.

# Create six different instances of the class Car. In the class have a method called display_all() that returns all the information about the car as a string. In your __init__(), call this display_all() method to display information about the car once the attributes have been defined.

# A sample output would be like this:

class Car:
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = .15
        if self.price < 10000:
            self.tax = .12
    def display_all(self):
        print(f"Price: {self.price}\nSpeed: {self.speed}\nFuel: {self.fuel}\nMilage: {self.mileage}mph\nTax: {self.tax}")
        return self


lotus = Car(21000, 35, 'full', 15)
farrari = Car(19000, 5, 'Not Full', 105)
lamborgini = Car(9000, 15, 'Kind of Full', 95)
tesla = Car(80000, 25, 'Full', 25)
porche = Car(10001, 25, 'Empty', 25)
mclearn =Car(10000000, 35, 'Empty', 15)

lotus.display_all()
farrari.display_all()
lamborgini.display_all()
tesla.display_all()
porche.display_all()
mclearn.display_all()

