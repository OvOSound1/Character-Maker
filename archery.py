from decorator import Decorator

class Archery(Decorator):
    """Decorator class for adding Archery ability to a character."""

    def abilities(self):
        """
        Add the Archery ability to the character.

        Returns:
            dict: A copy of the abilities dictionary with the added ability.
        """
        abilities_copy = self.character.abilities().copy()
        abilities_copy["Archery"] += 1
        return abilities_copy

    def constitution(self):
        """
        Override the constitution method to modify constitution attribute.

        Returns:
            int: The modified constitution stat of the character.
        """
        return super().constitution() - 2

    def strength(self):
        """
        Override the strength method to modify strength attribute.

        Returns:
            int: The modified strength stat of the character.
        """
        return super().strength() + 5

    def wisdom(self):
        """
        Override the wisdom method to modify wisdom attribute.

        Returns:
            int: The modified wisdom stat of the character.
        """
        return super().wisdom() - 2
