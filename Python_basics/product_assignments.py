class Product:
    def __init__(self, price, itemName, weight, brand):
        self.price = price
        self.itemName = itemName
        self.weight = weight
        self.brand = brand
        self.status = "for sale"

    def sell(self):
        self.status = "sold"
        return self

    def addTax(self, tax):
        self.price += self.price*tax
        return self.price
    
    def returnItem(self, reason_for_return):
        if reason_for_return == "defective":
            self.status = "defective"
            self.price = 0
        if reason_for_return == "like new":
            self.status = "sale"
            self.price = 0
        if reason_for_return == "opened":
            self.status = "used"
            self.price -= self.price *.2
        return self, reason_for_return


    def display_Output(self):
        print(f"Price: {self.price}\nItem Name: {self.itemName}\nWeight: {self.weight}\nBrand: {self.brand}\nStatus: {self.status}" )

phone1 = Product(1000, " Apple phone ", 10,"Iphone")
phone2 = Product(800, " Samsung phone ", 10,"Galaxy")
phone3 = Product(7000, " LG phone ", 10,"G3")
phone4 = Product(1000, " phone ", 10,"G4")

phone1.addTax(.2)
print(phone1.price)

print(phone1.brand)
print(phone3.itemName)

# phone3.returnItem()
# print(phone3)