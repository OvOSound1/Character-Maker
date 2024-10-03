from character import Character

class Elf(Character):
    """Class representing an Elf character."""

    def __init__(self, n):
        """
        Initialize an Elf character.

        Args:
            n (str): The name of the Elf.
        """
        super().__init__(f"\n{n} the Elf")
        self.abilities_dict = {"Archery": 1, "Fighting": 0, "Fire Magic": 0, "Healing": 0}
        self.constitution_stat = 13
        self.strength_stat = 10
        self.wisdom_stat = 15

    def abilities(self):
        """
        Get the abilities of the Elf.

        Returns:
            dict: A dictionary containing the abilities of the Elf.
        """
        return self.abilities_dict

    def constitution(self):
        """
        Get the constitution stat of the Elf.

        Returns:
            int: The constitution stat of the Elf.
        """
        return self.constitution_stat

    def strength(self):
        """
        Get the strength stat of the Elf.

        Returns:
            int: The strength stat of the Elf.
        """
        return self.strength_stat

    def wisdom(self):
        """
        Get the wisdom stat of the Elf.

        Returns:
            int: The wisdom stat of the Elf.
        """
        return self.wisdom_stat
