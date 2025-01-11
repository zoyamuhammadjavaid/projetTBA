# Description: The actions module.

# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.


# The error message is stored in the MSG0 and MSG1 variables and formatted with the command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"

from secured import SecuredRoom

class Actions:

    def go(game, list_of_words, number_of_parameters):
        """
        Move the player in the direction specified by the parameter.
        The parameter must be a cardinal direction (N, E, S, O).

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:
        
        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> go(game, ["go", "N"], 1)
        True
        >>> go(game, ["go", "N", "E"], 1)
        False
        >>> go(game, ["go"], 1)
        False

        """
        
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        #Get the direction from the list of words.

        #normalized_directions = game.direction_names.get(direction)

        #if not normalized_directions:
            #print("La direction est invalide. Utilisez une direction valide (N, S, E, O, U, D).")
            #return False

        #if normalized_directions not in game.direction_names.exits :
            #print("Un mur invisible bloque votre passage dans cette direction.")
            #return False

        direction = list_of_words[1].upper()

        # Move the player in the direction specified by the parameter.
        player.move(direction)
        return True

    def quit(game, list_of_words, number_of_parameters):
        """
        Quit the game.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> quit(game, ["quit"], 0)
        True
        >>> quit(game, ["quit", "N"], 0)
        False
        >>> quit(game, ["quit", "N", "E"], 0)
        False

        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Set the finished attribute of the game object to True.
        player = game.player
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True
    

    # Fonction pour exécuter la commande

    def help(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> help(game, ["help"], 0)
        True
        >>> help(game, ["help", "N"], 0)
        False
        >>> help(game, ["help", "N", "E"], 0)
        False

        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        
        # Print the list of available commands.
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True
    
    
    def back(game, list_of_words, number_of_parameters):
        """
        Autorise le joueur a retourner dans la pièce précédente

        Args:
            game (Game): The game object.
            list_of_words (list): la liste des mots
            number_of_parameters (int): Les nombres de parametres que la commande s'attend à avoir.

        Returns:
            bool: True si la commande a été exécutée correctement, False sinon.
        """
        # On vérifie si le nombres de parametres de la commande est correcte
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
    
        player = game.player

        # on vérifie s'il y a une chambre dans la historique
        if len(player.history) == 0:
            print("\nIl n'y a pas de retour en arrière possible.\n")
            return False
    
        player.undo()
        return True
    


    def look(game, list_of_words, number_of_parameters):
        """
        Affiche les objets et personnages présents dans la pièce courante.

        Args:
            game (Game): The game object.
            list_of_words (list): la liste des mots
            number_of_parameters (int): Les nombres de parametres que la commande s'attend à avoir.

        Returns:
            bool: True si la commande a été exécutée correctement, False sinon.
        """
        # Vérifier le nombre de paramètres
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # On récupérer la room courante et on affiche son contenu
        current_room = game.player.current_room
        print(current_room.get_inventory())
    
        return True
    


    def take(game, list_of_words, number_of_parameters):
        """
        Permet au joueur de prendre un objet dans la pièce courante.

        Args:
            game (Game): The game object.
            list_of_words (list): la liste des mots
            number_of_parameters (int): Les nombres de parametres que la commande s'attend à avoir.

        Returns:
            bool: True si la commande a été exécutée correctement, False sinon.
        """
        # On vérifie le nombre de paramètres
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
    
        # Récupérer le nom de l'item à prendre
        item_name = list_of_words[1].lower()
    
        # Vérifier si l'item existe dans la pièce
        room_inventory = game.player.current_room.inventory
        item_to_take = None
    
        for item in room_inventory:
            if item.name.lower() == item_name:
                item_to_take = item
                break
    
        if item_to_take is None:
            print(f"\nIl n'y a pas de '{item_name}' dans cette pièce.\n")
            return False
    
        # Retirer l'item de la pièce et l'ajouter à l'inventaire du joueur
        game.player.current_room.inventory.remove(item_to_take)
        game.player.inventory.append(item_to_take)
        print(f"\nVous avez pris: {item_to_take}\n")
    
        return True
    


    def drop(game, list_of_words, number_of_parameters):
        """
        Permet au joueur de déposer un objet de son inventaire dans la pièce courante.

        Args:
            game (Game): The game object.
            list_of_words (list): la liste des mots
            number_of_parameters (int): Les nombres de parametres que la commande s'attend à avoir.

        Returns:
            bool: True si la commande a été exécutée correctement, False sinon.
        """
        # Vérifier le nombre de paramètres
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Récupérer le nom de l'item à déposer
        item_name = list_of_words[1].lower()

        # Vérifier si l'item existe dans l'inventaire du joueur
        item_to_drop = None
        for item in game.player.inventory:
            if item.name.lower() == item_name:
                item_to_drop = item
                break

        if item_to_drop is None:
            print(f"\nVous n'avez pas de '{item_name}' dans votre inventaire.\n")
            return False

        # Retirer l'item de l'inventaire du joueur et l'ajouter à la pièce
        game.player.inventory.remove(item_to_drop)
        game.player.current_room.inventory.add(item_to_drop)
        print(f"\nVous avez déposé : {item_to_drop}\n")

        return True
    


    def check(game, list_of_words, number_of_parameters):
        """
        Affiche le contenu de l'inventaire du joueur.

        Args:
            game (Game): The game object.
            list_of_words (list): la liste des mots
            number_of_parameters (int): Les nombres de parametres que la commande s'attend à avoir.

        Returns:
            bool: True si la commande a été exécutée correctement, False sinon.
        """
        # On vérifie le nombre de paramètres
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # On regarde si l'inventaire est vide
        if not game.player.inventory:
            print("\nVotre inventaire est vide.\n")
            return True

        # On afficher les objets dans l'inventaire
        print("\nDans votre inventaire:")
        for item in game.player.inventory:
            print(f"\t- {item}")
        print()

        return True
    

    
    def talk(game, list_of_words, number_of_parameters):
        """
        Permet au joueur de parler avec un personnage présent dans la pièce.
        """
        # Vérifier le nombre de paramètres
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Récupérer le nom du personnage
        character_name = list_of_words[1].lower()

        # Vérifier si le personnage est dans la pièce courante
        current_room = game.player.current_room

        # Debug : Afficher les clés du dictionnaire characters
        #print(f"Personnages dans la pièce : {current_room.characters.keys()}")
        #print(f"Nom du PNJ recherché : {character_name}")

        if character_name not in current_room.characters:
            print(f"\nIl n'y a personne qui s'appelle '{list_of_words[1]}' ici.\n")
            return False

        # Obtenir et afficher le message du personnage
        character = current_room.characters[character_name]
        print(f"\n{character.get_msg()}\n")

        return True
    

    def give(game, list_of_words, number_of_parameters):
        """
        Permet au joueur de donner un objet à un personnage.
        """

        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print("\nLa commande 'give' prend 2 paramètres: l'objet et le destinataire.\n")
            return False
    
        # Récupérer le nom de l'item et du personnage
        item_name = list_of_words[1].lower()
        character_name = list_of_words[2].lower()

        # Vérifier si l'item est dans l'inventaire du joueur
        item_to_give = None
        for item in game.player.inventory:
            if item.name.lower() == item_name:
                item_to_give = item
                break
        
        if item_to_give is None:
            print(f"\nVous n'avez pas de '{item_name}' dans votre inventaire.\n")
            return False
    
        # Vérifier si le personnage est présent
        current_room = game.player.current_room
        character_found = None
        for name, character in current_room.characters.items():
            if name.lower() == character_name:
                character_found = character
                break
        
        if not character_found:
            print(f"\nIl n'y a personne qui s'appelle '{character_name}' ici.\n")
            return False
    
        # Donner l'objet et recevoir la réponse
        response = character_found.receive_items(item_to_give)  # Changé ici de receive_item à receive_items
        if response:
            game.player.inventory.remove(item_to_give)
            print(f"\nVous donnez {item_to_give.name} à {character_found.name}.")
            print(f"\n{character_found.name} dit: {response}\n")
            return True
        else:
            print(f"\n{character_found.name} n'est pas intéressé par cet objet.\n")
            return False



    @staticmethod #element important pour cette fonction
    def try_password(game, list_of_words, number_of_parameters):
        """
        Tente d'entrer un mot de passe pour déverrouiller le château.
        """
        if len(list_of_words) != number_of_parameters + 1:
            print("\nLa commande 'password' prend 1 paramètre : le code à essayer.\n")
            return False
        
        current_room = game.player.current_room
        if not isinstance(current_room, SecuredRoom):
            print("\nIl n'y a pas de mécanisme à code ici.\n")
            return False
        
        password = list_of_words[1]
        return current_room.unlock(password, game)
    
