rows = 5
for i in range(rows):
    for j in range(1, i + 1):
        print(j,end="")
    print("")

class details:
    def __init__(self,name,course,branch,age):
        self.name = name
        self.course = course
        self.branch = branch
        self.age = age
        print(f"Name: {self.name}\nCourse: {self.course}\nBranch: {self.branch} \nage: {self.age}")

obj = details("John Doe","B.Tech","Computer Science")   