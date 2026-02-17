rows = 5
for i in range(rows):
    for j in range(1, i + 1):
        print(j,end="")
    print("")

class details:
    def __init__(self,name,course,branch,age,country):
        self.name = name
        self.course = course
        self.branch = branch
        self.age = age
        self.country = country
        print(f"Name: {self.name}\nCourse: {self.course}\nBranch: {self.branch}\nCountry: {self.country}")

obj = details("John Doe","B.Tech","Computer Science","20","USA")   