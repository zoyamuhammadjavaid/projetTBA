# Define the Player class.
class Player():

    """
    Cette class represente a player. A player has a name and a location where is, in what room he is.

    Attributes:
        self.name (str): The name of the player.
        self.current_room (str): It stores the current room where the player is located.

    Methods:
        __init__(self, name) : The constructor.
        move(self, direction) : The movement of the player from one room to another, based on the given directions.

     Examples:

    >>> from player import Player
    >>> from room import Room
    >>> player = Player("Lara")
     >>> forest = Room("Forest", "dans une forêt enchantée. Vous entendez une brise légère à travers la cime des arbres")
    >>> tower = Room("Tower", "dans une immense tour en pierre qui s'élève au dessus des nuages.")
    >>> forest.exits = {"N" : cave, "E" : tower, "S" : castle, "O" : None}
    >>> player.current_room = forest
    >>> player.move("N")
    Dans une immense tour en pierre qui s'élève au dessus des nuages
    True
    >>> player.move("E")
    tower

    """


    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.current_room = None
        self.history = [] #12/12 
        self.inventory = [] #16/12


    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        
        #add the place to the history
        self.history.append(self.current_room) #12/12

        # Set the current room to the next room.
        self.current_room = next_room
        print(self.current_room.get_long_description())

        print(self.get_history())

        return True

    def undo(self):
        if self.history:
            self.current_room = self.history.pop()
            print(self.current_room.get_long_description())
        else:
            print("\n Il n'y a pas de retour en arrière.\n")
        
    def get_history(self):

        if not self.history:
            return "\n Vous n'avez pas encore commencer l'aventure.\n"

        history_str = "\n Vous avez déjà visité les pièces suivantes:\n"
        for room in self.history:
            history_str +=f"\t - {room.description}\n"

        return history_str
    
    #La fonction get_history permet au joueur de voir son trajet jusqu'à l'endroit où il se trouve

    def get_inventory(self): #travail du 16/12
        
        if not self.inventory:
            return "\nVotre inventaire est vide.\n"
    
        inventory_str = "\nVous avez dans votre inventaire :\n"
        
        for item in self.inventory:
            inventory_str += f"\t - {item}\n"
    
        return inventory_str

