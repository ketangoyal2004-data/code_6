rows = 5
b = 0

for i in range(rows,0,-1):
    b += 1
    for j in range(1,i + 1):
        print(b,end="")
    print("\r")


class cal:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print("a + b = ",self.a + self.b)

obj = cal(10,5)