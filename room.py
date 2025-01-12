# Define the Room class.

class Room:

    """
    This class represents a room. A room has a name, it is either a place where the player can be located or a place where the player can head to.

    Attributes:
        self.name : the name of the place.
        self.description : the description of the room.
        self.exits : the exits where the player can take.

    Methods:
        __init__(self, name) : The constructor.
        get_exit(self, direction) : It returns the room in the given directions if it exists, otherwise it returns None.

     Examples:

    >>> from room import Room
    >>> forest = Room("Forest", "dans une forêt enchantée. Vous entendez une brise légère à travers la cime des arbres")
    >>> tower = Room("Tower", ""dans une immense tour en pierre qui s'élève au dessus des nuages.".")
    >>> forest.exits = {"N" : cave, "E" : tower, "S" : castle, "O" : None}
    >>> forest.get_exit("N")
    cave
    >>> forest.get_exit("E")
    tower
    >>> print(forest.get_exit_string())
    Sorties: N
    >>> print(forest.get_long_description())
    Vous êtes dans une forêt enchantée. Vous entendez une brise légère à travers la cime des arbres
    
    Sorties: N, E, S
    """

    # Define the constructor. 
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory = set()
        self.characters = dict()
 
    
    # Define the get_exit method.
    def get_exit(self, direction):

        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"

    def get_inventory(self):
        """Retourne une description du contenu de la pièce (objets et personnages)"""
        inventory_str = "\n"
    
        # On vérifier les objets
        if self.inventory:
            inventory_str += "Vous voyez les objets suivants:\n"
            for item in self.inventory:
                inventory_str += f"\t- {item}\n"
    
        # On vérifier les personnages
        if self.characters:
            inventory_str += "\nVous voyez les personnes suivantes:\n"
            for character in self.characters.values():
                inventory_str += f"\t- {character}\n"
            
        if not self.inventory and not self.characters:
            return "\nIl n'y a rien ni personne ici.\n"
        
        return inventory_str


    def get_characters_string(self):
        
        """Retourne une description des personnages présents dans la pièce."""
        if not self.characters:
            return ""
        
        chars_str = "\nPersonnages présents:\n"
        for character in self.characters.values():
            chars_str += f"\t- {character}\n"
        return chars_str

