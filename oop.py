# class syneffo:
#     def python():
#         print('python')
#     def javascript():
#         print('javascript') 

# std1 = syneffo
# std1.python()
# std1.javascript()


class student:
    school='ABC public school'  #class variables
    def __init__(self,name,age): #parameterized constructor
        self.name=name #instance variables
        self.age=age
    def getDetails(self):
        print(f"Name is{self.name}.\nAge is {self.age}.")
    @staticmethod
    def great():
        print('hello')
        
    @classmethod
    def change_school(cls,name):
        cls.school=name
p1 = student('mishal',23)

print(p1.name)
print(p1.age)
# print(p1.phone)
p1.getDetails()
student.great()

print(student.school)
student.change_school('carmal rani public school')
print(student.school)