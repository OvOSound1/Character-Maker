from character import Character
from abc import ABC, abstractmethod

class Decorator(Character, ABC):
    """Abstract base class for character decorators."""

    def __init__(self, c):
        """
        Initialize a character decorator.

        Args:
            c (Character): The character to be decorated.
        """
        super().__init__(c.name)
        self.character = c
        self.abilities_dict = self.character.abilities_dict

    def abilities(self):
        """
        Get the abilities of the decorated character.

        Returns:
            dict: A dictionary containing the abilities of the decorated character.
        """
        return self.character.abilities()

    def constitution(self):
        """
        Get the constitution stat of the decorated character.

        Returns:
            int: The constitution stat of the decorated character.
        """
        return self.character.constitution()

    def strength(self):
        """
        Get the strength stat of the decorated character.

        Returns:
            int: The strength stat of the decorated character.
        """
        return self.character.strength()

    def wisdom(self):
        """
        Get the wisdom stat of the decorated character.

        Returns:
            int: The wisdom stat of the decorated character.
        """
        return self.character.wisdom()

    def __str__(self):
        """
        Get a string representation of the decorated character.

        Returns:
            str: A string representation of the decorated character.
        """
        abilities_str = "\n".join([f"{ability}: Level {level}" for ability, level in self.abilities().items()])
        return f"{self.character.name}\n-Abilities-\n{abilities_str}\n-Stats-\nCon: {self.constitution()}\nStr: {self.strength()}\nWis: {self.wisdom()}"
