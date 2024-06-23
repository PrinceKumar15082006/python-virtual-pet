import random

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = random.randint(0, 10)
        self.happiness = random.randint(5, 10)
        self.energy = random.randint(5, 10)
        self.age = 0
        self.is_alive = True
    
    def feed(self):
        if self.hunger > 0:
            self.hunger -= 1
        self.happiness += 1
    
    def play(self):
        if self.energy > 0:
            self.energy -= 1
        self.happiness += 2
    
    def sleep(self):
        self.energy += 2
    
    def get_status(self):
        return f"{self.name}:\nHunger: {self.hunger}\nHappiness: {self.happiness}\nEnergy: {self.energy}"
    
    def pass_time(self):
        self.hunger += 1
        self.happiness -= 1
        self.energy -= 1
        self.age += 1
        
        if self.hunger >= 10 or self.energy <= 0:
            self.is_alive = False

    def is_dead(self):
        return not self.is_alive

    def get_age(self):
        return self.age
