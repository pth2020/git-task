from tabulate import tabulate

class Student:

    def __init__(self,name,grades):
        self.name = name
        self.grades = grades
        
    def getAverage(self):
        return round(sum(self.grades)/len(self.grades),1)
    
student1 = Student("Peter",[80,70,90])
student2 = Student("Emily",[90,88,100])
student3 = Student("Simon",[96,82,90])
student4 = Student("Toby",[45,50,90])
student5 = Student("Sasha",[100,98,90])

data = []

data.append([student1.name,student1.grades[0],student1.grades[1],student1.grades[2],student1.get_average()])
data.append([student2.name,student2.grades[0],student2.grades[1],student2.grades[2],student2.get_average()])
data.append([student3.name,student3.grades[0],student3.grades[1],student3.grades[2],student3.get_average()])
data.append([student4.name,student4.grades[0],student4.grades[1],student4.grades[2],student4.get_average()])
data.append([student5.name,student5.grades[0],student5.grades[1],student5.grades[2],student5.get_average()])

headers = ["Name","English","Maths","Science","Average"]

table1 = tabulate(data,headers = headers)

print(table1)
