rows = 5
num = rows

for i in range(rows,0,-1):
    for j in range(0,i):
        print(num,end="")
    print("\r")

class college_details:
    def name(self,name):
        self.name = name
        print("Name: ",self.name)

    def course(self,course):
        self.course = course
        print("course: ",self.course)

obj = college_details()
obj.name("Apex University")
obj.course("B.Tech")