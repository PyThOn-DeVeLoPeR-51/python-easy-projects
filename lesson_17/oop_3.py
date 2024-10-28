class Student:
    def __init__(self, name, lastname, age, ID):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.ID = ID
        self.fan = []
        
    def name(self):
        return self.name
    
    def lastname(self):
        return self.lastname
    
    def fullname(self):
        return f"{self.name} {self.lastname}"
    
    def age(self):
        return self.age
    
    def student_id(self):
        return self.ID
    

class Fan:
    def __init__(self, matem, adabiyot, geometriya):
        self.math = matem
        self.literature = adabiyot
        self.geometry = geometriya
        
    def math(self):
        return self.math
    
    def literature(self):
        return self.literature
    
    def geometry(self):
        return self.geometry
    
    
    
        
        
    