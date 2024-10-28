class Avto:
    def __init__(self, company, model, color, price):
        self.company = company
        self.model = model
        self.color = color
        self.price = price
        self.km = 0
        self.transmission = 'AT'
        self.year = 2023
        
        
    def get_company(self):
        return self.company
    
    def get_model(self):
        return self.model
    
    def get_color(self):
        return self.color
    
    def get_price(self):
        return self.price
    
    def get_transmission(self):
        return self.transmission
    
    def get_year(self):
        return self.year
    
    def set_km(self, km):
        self.km = km
        
    def set_update(self):
        self.km += 1
        
    def name_lastname(self):
        return f"{self.color} {self.model}"
    
    def get_info(self):
        return f"{self.company} kompaniyasi {self.year}-yilda {self.color} rangli {self.model}({self.transmission})ni ${self.price} dan ishlab chiqarmoqda!"
        
avto1 = Avto('GM', 'Nexi3', 'oq', 10000)        
avto2 = Avto('GM', 'Colabt', 'oq', 12000) 
avto3 = Avto('GM', 'Gentra', 'oq', 16000) 
avto4 = Avto('GM', 'Tracker', 'oq', 25000) 
avto5 = Avto('GM', 'Malibu', 'oq', 38000) 


class Avtosalon:
    def __init__(self, salon_name, address):
        self.name = salon_name
        self.address = address
        self.avtos = []
        self.new_avto = 0
        
    def add_avto(self, avto):
        self.avtos.append(avto)
        self.new_avto += 1
        
    def get_new_avtos(self):
        return [avto.name_lastname() for avto in self.avtos]
    
avtosalon = Avtosalon("Bunyodkor", "Farg'ona shahar") 


def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__') is False]
        
        