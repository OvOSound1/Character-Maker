from abc import ABC, abstractmethod

class Character(ABC):
    """Abstract base class representing a character."""

    def __init__(self, n):
        """
        Initialize a character.

        Args:
            n (str): The name of the character.
        """
        self._name = n

    @property
    def name(self):
        """
        Get the name of the character.

        Returns:
            str: The name of the character.
        """
        return self._name

    @abstractmethod
    def abilities(self):
        """
        Abstract method to get the abilities of the character.

        Returns:
            dict: A dictionary containing the abilities of the character.
        """
        pass

    @abstractmethod
    def constitution(self):
        """
        Abstract method to get the constitution stat of the character.

        Returns:
            int: The constitution stat of the character.
        """
        pass

    @abstractmethod
    def strength(self):
        """
        Abstract method to get the strength stat of the character.

        Returns:
            int: The strength stat of the character.
        """
        pass

    @abstractmethod
    def wisdom(self):
        """
        Abstract method to get the wisdom stat of the character.

        Returns:
            int: The wisdom stat of the character.
        """
        pass

    def __str__(self):
        """
        Get a string representation of the character.

        Returns:
            str: A string representation of the character.
        """
        abilities_str = "\n".join([f"{ability}: Level {level}" for ability, level in self.abilities().items()])
        return f"{self.name}\n-Abilities-\n{abilities_str}\n-Stats-\nCon: {self.constitution()}\nStr: {self.strength()}\nWis: {self.wisdom()}"
