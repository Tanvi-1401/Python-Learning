class Student:
    
    #default constructor
    def __init__(self):
        pass
    
    #paramiterized constructor
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
        print("Adding Student Info")
    
    @staticmethod
    def hello(): # decorator
        print("Hello Student") 
          
    def welcome(self):
        print("Welcome, ", self.name)

    def get_marks(self):
        print("Marks: ", self.marks)        

s1 = Student("Tanvi", 19, 99)
s1.welcome()
print(s1.name, s1.age, s1.marks)  

s2 = Student("Tanishk", 19, 99)
s2.welcome()
  

