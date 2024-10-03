# Names: Francisco Fausto, Tiffany Nguyen, Nick Breeding 
# Assignment: Lab 11, Group 8
# Course: CECS 277 Sec 04
# Date: April 23th, 2024
# Desc: You're creating a role-playing character creation program with the Decorator pattern. It involves three base character types (Dwarf, Elf, Halfling) that can be decorated with four abilities (Archery, Fighting, Fire, Healing) to display updated stats for the created character.

from character import Character
from decorator import Decorator
from dwarf import Dwarf
from elf import Elf
from halfling import Halfling
from archery import Archery
from fighting import Fighting
from fire import Fire
from healing import Healing

def main():
    """Main function to create a character with abilities."""
    print("Character Maker!")
    print("Choose your character:")
    print("1. Dwarf")
    print("2. Elf")
    print("3. Halfling")
    choice = int(input("Enter choice: "))  # Get user's choice for character type
    name = input("\nWhat is your character's name? ")  # Get user's input for character name

    # Create character based on user's choice
    if choice == 1:
        character = Dwarf(name)
    elif choice == 2:
        character = Elf(name)
    else:
        character = Halfling(name)

    print(character)  # Print character information

    # Allow the player to choose abilities for the character
    for i in range(5):
        print("\nYou have", 5 - i, "points to spend:")
        print("Add an ability:")
        print("1. Archery")
        print("2. Fighting")
        print("3. Fire Magic")
        print("4. Healing")
        ability = int(input("\nEnter ability: "))  # Get user's choice for ability

        # Add the selected ability to the character
        if ability == 1:
            character = Archery(character)
        elif ability == 2:
            character = Fighting(character)
        elif ability == 3:
            character = Fire(character)
        else:
            character = Healing(character)

        print(character)  # Print character information with added ability

    # Check if any of the character's attributes have fallen to 0 or below
    if character.constitution() <= 0 or character.strength() <= 0 or character.wisdom() <= 0:
        print("\nYou failed making a character.")
    else:
        print("\nCongratulations! You have created your character.")

if __name__ == "__main__":
    main()
