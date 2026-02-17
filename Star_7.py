class cal:
    @staticmethod
    def add(a,b):
        return a + b
    
    @staticmethod
    def sub(a,b):
        return a - b
    
    @staticmethod
    def mul(a,b):
        return a * b
    
obj = cal()
print("a + b = ",obj.add(10,5))
print("a - b = ",obj.sub(10,5)) 
print("a * b = ",obj.mul(10,5)) 