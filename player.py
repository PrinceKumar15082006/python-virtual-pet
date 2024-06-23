class Player:
    def __init__(self, name):
        self.name = name
        self.pet = None
    
    def adopt_pet(self, pet):
        self.pet = pet
    
    def interact(self):
        while not self.pet.is_dead():
            action = input("Choose an action: [feed, play, sleep, check, quit]\n").lower()
            if action == 'feed':
                self.pet.feed()
            elif action == 'play':
                self.pet.play()
            elif action == 'sleep':
                self.pet.sleep()
            elif action == 'check':
                print(self.pet.get_status())
            elif action == 'quit':
                break
            else:
                print("Invalid action.")
            
            self.pet.pass_time()
        
        print("Game over!")
        print(f"Your pet lived for {self.pet.get_age()} days.")
