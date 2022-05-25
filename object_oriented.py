# import pandas as pd 

# pd.DataFrame()


# class RailwayForm:
#     formtype = 'Railway form'
#     def printData(self):
#         print(f"My Name is {self.name}")
#         print(f"My train is {self.train}")

# abhishektrain = RailwayForm()
# abhishektrain.name = "Abhishek"
# abhishektrain.train = 'Shatabdhi_Express'
# abhishektrain.printData()

class Mobile:
    def __init__(self, model, camera):
        self.model = model
        self.camera= camera
    def make_call(self,number):
        print("calling..{}".format(number))

mobile_obj1 = Mobile("iPhone 12 Pro", "12 MP")
print(mobile_obj1)
mobile_obj2 = Mobile("Galaxy M51", "64 MP")
print(mobile_obj2)
mobile_obj1.make_call(9798752028)
print(type(mobile_obj1))

class Mobile:
    def __init__(self, model, storage):
        self.model = model
        self.storage = storage

    def get_model(self):
        print(self.model)

obj = Mobile("iphone_12", "20GB")
print(obj.model)
print(obj.storage)
obj.get_model()