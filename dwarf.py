from character import Character

class Dwarf(Character):
    """Class representing a Dwarf character."""

    def __init__(self, n):
        """
        Initialize a Dwarf character.

        Args:
            n (str): The name of the Dwarf.
        """
        super().__init__(f"\n{n} the Dwarf")
        self.abilities_dict = {"Archery": 0, "Fighting": 1, "Fire Magic": 0, "Healing": 0}
        self.constitution_stat = 13
        self.strength_stat = 15
        self.wisdom_stat = 10

    def abilities(self):
        """
        Get the abilities of the Dwarf.

        Returns:
            dict: A dictionary containing the abilities of the Dwarf.
        """
        return self.abilities_dict

    def constitution(self):
        """
        Get the constitution stat of the Dwarf.

        Returns:
            int: The constitution stat of the Dwarf.
        """
        return self.constitution_stat

    def strength(self):
        """
        Get the strength stat of the Dwarf.

        Returns:
            int: The strength stat of the Dwarf.
        """
        return self.strength_stat

    def wisdom(self):
        """
        Get the wisdom stat of the Dwarf.

        Returns:
            int: The wisdom stat of the Dwarf.
        """
        return self.wisdom_stat
