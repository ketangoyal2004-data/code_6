rows = 5
for i in range(rows):
    for j in range(1, i + 1):
        print(j,end="")
    print("")

class std:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print(f"Name: {self.name}, Age: {self.age}")

obj = std("Ketan Goyal", 20)