class User:
    def __init__(self, name, lastname, age, tel, email):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.phone = tel
        self.mail = email
        
    def name(self):
        return self.name
    
    def lastname(self):
        return self.lastname
    
    def full_name(self):
        return f"{self.name} {self.lastname}"
        
    def get_info(self):
        return f"{self.name} {self.lastname} {self.age} yoshda. Tel: {self.phone}. Email: {self.mail}"
        
user1 = User("Nodir", 'Komilov', 36, '906334451', 'nodir36@.com')
    
   