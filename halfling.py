from character import Character

class Halfling(Character):
    """Class representing a Halfling character."""

    def __init__(self, n):
        """
        Initialize a Halfling character.

        Args:
            n (str): The name of the Halfling.
        """
        super().__init__(f"\n{n} the Halfling")
        self.abilities_dict = {"Archery": 0, "Fighting": 0, "Fire Magic": 0, "Healing": 1}
        self.constitution_stat = 15
        self.strength_stat = 10
        self.wisdom_stat = 13

    def abilities(self):
        """
        Get the abilities of the Halfling.

        Returns:
            dict: A dictionary containing the abilities of the Halfling.
        """
        return self.abilities_dict

    def constitution(self):
        """
        Get the constitution stat of the Halfling.

        Returns:
            int: The constitution stat of the Halfling.
        """
        return self.constitution_stat

    def strength(self):
        """
        Get the strength stat of the Halfling.

        Returns:
            int: The strength stat of the Halfling.
        """
        return self.strength_stat

    def wisdom(self):
        """
        Get the wisdom stat of the Halfling.

        Returns:
            int: The wisdom stat of the Halfling.
        """
        return self.wisdom_stat
