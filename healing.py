from decorator import Decorator

class Healing(Decorator):
    """Decorator class for adding Healing ability to a character."""

    def abilities(self):
        """
        Add the Healing ability to the character.

        Returns:
            dict: A copy of the abilities dictionary with the added ability.
        """
        abilities_copy = self.character.abilities().copy()
        abilities_copy["Healing"] += 1
        return abilities_copy

    def constitution(self):
        """
        Override the constitution method to modify constitution attribute.

        Returns:
            int: The modified constitution stat of the character.
        """
        return super().constitution() + 3

    def strength(self):
        """
        Override the strength method to modify strength attribute.

        Returns:
            int: The modified strength stat of the character.
        """
        return super().strength() - 4

    def wisdom(self):
        """
        Override the wisdom method to modify wisdom attribute.

        Returns:
            int: The modified wisdom stat of the character.
        """
        return super().wisdom() + 2
