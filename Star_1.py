rows = 6

for i in range(rows):
    for j in range(i):
        print(i,end="")
    print("")

class cal:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print("a + b = ",self.a + self.b)
        print("a - b = ",self.a - self.b)
        print("a * b = ",self.a * self.b)
        print("a / b =",self.a / self.b)

obj = cal(10,5)