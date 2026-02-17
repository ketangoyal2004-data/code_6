class std:
    def name1(self,name):
        self.name = name
        print(f"Name: {self.name}")

    def name2(self,name):
        self.name = name
        print(f"Name: {self.name}")

class std2(std):
    def name3(self,name):
        self.name = name
        print(f"Name: {self.name}")

obj = std2()
obj.name1("Ketan Goyal")
obj.name2("Mann Soni")
obj.name3("Harry")