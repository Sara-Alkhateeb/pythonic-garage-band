from abc import ABC, abstractmethod

class Band:
    instances = []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.instances.append(self)
   
    
    def play_solos(self):
        solos = []
        for each_member in self.members:
            solos.append(each_member.play_solo())
        return solos
           
    
    def __str__(self): 
        return f'Band Name : {self.name}'
    
    def __repr__(self): 
        return f'I am a representation of {self.name}'
    
    @classmethod
    def to_list(cls):
        return cls.instances
    
    


class Musician: 

    def __init__(self , name) :
        self.name = name
    
    
    # def play_solos(self):
    #     return f''


class Guitarist(Musician): 


    def __init__(self , name) :
        self.name = name

    def __str__(self): 
        return f'My name is {self.name} and I play guitar'
    
    def __repr__(self): 
        return f'Guitarist instance. Name = {self.name}'
    
    def play_solo(self):
        return "face melting guitar solo"
    def get_instrument(self):
        return "guitar"



class Drummer(Musician): 

    def __init__(self , name) :
        self.name = name

    def __str__(self): 
        return f'My name is {self.name} and I play drums'
    
    def __repr__(self): 
        return f'Drummer instance. Name = {self.name}'
    
    def play_solo(self):
        return "rattle boom crash"
    def get_instrument(self):
        return "drums"


class Bassist(Musician): 

    def __init__(self , name) :
        self.name = name

    def __str__(self): 
        return f'My name is {self.name} and I play bass'
    
    def __repr__(self): 
        return f'Bassist instance. Name = {self.name}'
    def play_solo(self):
        return "bom bom buh bom" 
    def get_instrument(self):
        return "bass"
    


if __name__ == "__main__":
    pass