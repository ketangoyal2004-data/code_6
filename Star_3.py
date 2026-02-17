rows = 5
b = 0

for i in range(rows,0,-1):
    b += 1
    for j in range(1,i + 1):
        print(b,end="")
    print("\r")

class cal:
    def add(self,a,b):
        return a + b
    
    def sub(self,a,b):
        return a - b
    
    def mul(self,a,b):
        return a * b
    
    def div(self,a,b):
        return a / b 
    
    def exp(self,a,b):
        return a ** b


obj = cal()
print("a + b = ",obj.add(10,5))
print("a - b = ",obj.sub(10,5))
print("a * b = ",obj.mul(10,5)) 
print("a / b =",obj.div(10,5))
print("a ** b =",obj.exp(10,5))