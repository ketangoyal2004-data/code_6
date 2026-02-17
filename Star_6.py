rows = 5

for i in range(rows):
    for j in range(1, rows + 1):
        print(j,end="")
    print("")

class std:
    def __init__(self,name,course,branch):
        self.name = name
        self.course = course
        self.branch = branch
        print(f"Name:{self.name}\n Course:{self.course}\n Branch:{self.branch}")

obj = std("Ketan Goyal","BCA","Computer Science")
