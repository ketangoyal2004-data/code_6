rows = 5

for i in range(rows,0,-1):
    num = i
    for j in range(0,i):
        print(num,end="")
    print("\r")

class carName:
    def car_Name1(self,name):
        self.name = name
        print("car name: ",self.name)

    def car_Name2(self,name):
        self.name = name
        print("car name: ",self.name)

obj = carName()
obj.car_Name1("BMW")
obj.car_Name2("Audi")