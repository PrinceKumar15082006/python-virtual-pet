from pet import Pet
from player import Player

def main():
    player_name = input("Enter your name: ")
    pet_name = input("Choose a name for your pet: ")

    player = Player(player_name)
    pet = Pet(pet_name)

    player.adopt_pet(pet)

    print(f"Welcome, {player.name} and {player.pet.name}!")

    player.interact()

if __name__ == "__main__":
    main()
