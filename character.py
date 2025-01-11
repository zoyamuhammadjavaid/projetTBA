import random
class Character:
    """
    Cette classe représente un personnage dans le jeu.
    
    Attributes:
        name (str): Le nom du personnage
        description (str): La description du personnage
        current_room (Room): La pièce où se trouve le personnage
        dialogs (list): Liste des dialogues possibles du personnage
    """
    
    def __init__(self, name, description, current_room, message):
        """
        Initialise un personnage avec un nom, une description, une pièce et des dialogues.
        
        Args:
            name (str): Le nom du personnage
            description (str): La description du personnage
            current_room (Room): La pièce où se trouve le personnage
            message (list): Liste des messages possibles du personnage
        """
        self.name = name
        self.description = description
        self.current_room = current_room
        self.message = message

        self.original_messages = message.copy()

        self.wanted_items = {}
        self.has_given = set()

    def __str__(self):
        """
        Cette fonction permet de retourner une description textuelle du pnj.
        
        Return:
            str: La chaîne "{name} : {description}"
        """
        return f"{self.name} : {self.description}"
    
    def move(self):
        """
        Déplace le personnage aléatoirement vers une pièce adjacente avec une chance sur deux.
        
        Returns:
            bool: True si le personnage s'est déplacé, False sinon
        """
        # 50% de chance de se déplacer
        if random.random() < 0.5:
            # Récupérer toutes les sorties possibles (non None)
            possible_exits = [direction for direction, room in self.current_room.exits.items() 
                            if room is not None]
            
            # S'il n'y a pas de sortie possible, ne pas bouger
            if not possible_exits:
                return False
                
            # Choisir une direction au hasard
            chosen_direction = random.choice(possible_exits)
            
            # Retirer le personnage de la pièce actuelle
            character_key = None
            for key, char in self.current_room.characters.items():
                if char == self:  # Compare l'instance elle-même
                    character_key = key
                    break
                    
            if character_key is None:
                return False
                
            # Retirer le personnage de la pièce actuelle
            del self.current_room.characters[character_key]
            
            # Mettre à jour la pièce courante
            self.current_room = self.current_room.exits[chosen_direction]
            
            # Ajouter le personnage dans la nouvelle pièce avec la même clé
            self.current_room.characters[character_key] = self

            
            return True
            
        return False
    

    def get_msg(self):
        """
        Retourne le prochain message du personnage de façon cyclique.
        Quand tous les messages ont été affichés, on les réinitialise.
        
        Returns:
            str: Le prochain message du personnage
        """
        # Si la liste des messages est vide, on la réinitialise
        if not self.message:
            self.message = self.original_messages.copy()
        
        # Retourne et supprime le premier message de la liste
        return f"{self.name} dit : {self.message.pop(0)}"
    

    def receive_items(self, item):
        """Permet de donner un objet au pnj souhaité et celui-ci l'accepte si c'est l'objet qu'il souhaite"""

        if item.name.lower() in self.wanted_items and item.name.lower() not in self.has_given:
            self.has_given.add(item.name.lower())
            return self.wanted_items[item.name.lower()]
        return None
    

