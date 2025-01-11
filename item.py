
class Item:
    def __init__(self, name, description, weight):
        """
        Initialise un objet Item avec les attributs suivants : name, description et weight.

        name:param name: str, le nom de l'objet
        description:param description: str, la description de l'objet
        weight:param weight: int ou float, le poids de l'objet en kilogrammes
        """
        self.name = name
        self.description = description
        self.weight = weight

    def __str__(self):
        """
        On redéfinit la méthode __str__() pour qu'elle nous retourne une représentation textuelle de l'objet.
        :return: str, représentation de l'objet
        """
        return f"{self.name} : {self.description} ({self.weight} kg)"


