# class Student :
#     school = "AkiraChix"
#     def __init__(self, name, age, code):
#      self.name = name
#      self.age = age
#      self.code = code
     
class Student :
    school = "AkiraChix"
    def __init__(self, first_name, last_name, age, code):
     self.name = first_name
     self.last_name = last_name
     self.age = age
     self.code = code
     
    def greet_student(self):
         greeting = f"Hello {self.first_name}, welcome to {self.school}. Your code is {self.code}"
         return greeting
    
    def year_of_birth(self):
        return f"{self.first_name} was born in {2024 - self.age}"
    
    def full_names(self):
        return f"{self.first_name} {self.last_name}"
    