rows = 5

for i in range(rows):
    for j in range(1, rows + 1):
        print(j,end="")
    print("")

class std:
    def __init__(self,name,course,branch,age):
        self.name = name
        self.course = course
        self.branch = branch
        self.age = age
        print(f"Name:{self.name}\n Course:{self.course}\n Branch:{self.branch}\n age:{self.age}")


class std2(std):
    def __init__(self,name,course,country):
        self.name = name
        self.course = course
        self.country = country
        print(f"Name:{self.name}\n Course:{self.course}\n Country:{self.country}")

obj = std("Ketan Goyal","BCA","Computer Science",20)
obj2 = std2("Ketan Goyal","BCA","India")