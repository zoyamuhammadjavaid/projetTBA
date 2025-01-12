# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from character import Character
from secured import SecuredRoom
class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.valid_directions = {"N", "S", "E", "O", "U", "D"}
        self.direction_names = { "N": "N", "NORD": "N", "nord" : "N", "Nord" : "N",
            "O": "O", "OUEST": "O", "Ouest": "O", "ouest" : "O",
            "S": "S", "SUD": "S", "Sud": "S", "sud": "S",
            "E": "E", "EST": "E", "Est": "E", "est": "E",
            "U": "U", "HAUT": "U", "UP": "U", "up": "U",
            "D": "D", "BAS": "D", "DOWN": "D", "down" : "D",}

    # Setup the game
    def setup(self):

        # Setup commands

        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O, U, D)", Actions.go, 1)
        self.commands["go"] = go
        back = Command("back", " : revenir en arrière", Actions.back, 0)
        self.commands["back"] = back
        look = Command("look", " : regarder les objets dans la pièce", Actions.look, 0)
        self.commands["look"] = look
        take = Command("take", " <item> : prendre un objet", Actions.take, 1)
        self.commands["take"] = take
        drop = Command("drop", " <item> : déposer un objet", Actions.drop, 1)
        self.commands["drop"] = drop
        check = Command("check", " : vérifier le contenu de votre inventaire", Actions.check, 0)
        self.commands["check"] = check
        talk = Command("talk", " <someone> : parler avec quelqu'un", Actions.talk, 1)
        self.commands["talk"] = talk
        give = Command("give", " <item> <someone> : donner un objet à quelqu'un", Actions.give, 2)
        self.commands["give"] = give
        password = Command("password", "<code> : entrer le code secret", Actions.try_password,1)
        self.commands["password"] = password

        self.history = []

        # Setup rooms

        forest = Room("Forest", "dans une forêt enchantée. Vous entendez une brise légère à travers la cime des arbres.")
        self.rooms.append(forest)
        tower = Room("Tower", "dans une immense tour en pierre qui s'élève au dessus des nuages.")
        self.rooms.append(tower)
        cave = Room("Cave", "dans une grotte profonde et sombre. Des voix semblent provenir des profondeurs.")
        self.rooms.append(cave)
        cottage = Room("Cottage", "dans un petit chalet pittoresque avec un toit de chaume. Une épaisse fumée verte sort de la cheminée.")
        self.rooms.append(cottage)
        swamp = Room("Swamp", "dans un marécage sombre et ténébreux. L'eau bouillonne, les abords sont vaseux.")
        self.rooms.append(swamp)
        castle = SecuredRoom("Castle", "dans un énorme château fort avec des douves et un pont levis. Sur les tours, des flèches en or massif.")
        self.rooms.append(castle)
        clockhouse = Room("Clockhouse", "devant une boutique en forme d'horloge. Elle est prête à faire des échanges mystérieux.")
        self.rooms.append(clockhouse)
        bridge = Room("Bridge", "sur un pont enchanté. Sur l'autre côté du pont se trouve Nigel, celui échange les secrets.")
        self.rooms.append(bridge)
        lodges = Room("Lodges", "dans les merveilleux appartenants des joueurs de Caraval.")
        self.rooms.append(lodges)
        tunnels = Room("Tunnels","dans les tunnels envoûtants. Ils renferment les secrets de Caraval.")
        self.rooms.append(tunnels)
        clouds = Room("Clouds","dans les nuages. Ce véritable labyrinthe désoriente et bloque l'avancé de l'aventure." )
        self.rooms.append(clouds)
        fountain = Room("Fountain","sur la fontaine des voeux. Elle vous rapprochera de la victoire ou vous en éloignera." )
        self.rooms.append(fountain)

        #Setup items

        sword = Item("épée", "une épée magique qui brille d'une lueur bleue", 2)
        book = Item("grimoire", "un ancien livre de sorts poussiéreux", 0.5)
        key = Item("clé", "une clé en or massif finement ciselée", 0.1)
        potion = Item("potion", "une fiole contenant un liquide verdâtre bouillonnant", 0.3)
        crystal = Item("cristal", "un cristal qui pulse d'une étrange énergie", 0.5)
        stone = Item("pierre", "la pierre rouge de la famille Dragna", 1.5)
        bag = Item("sac", "le fameux sac de Scarlette, un sac infini", 0.9)
        butterfly = Item("papillon" , "le papillon vert est le symbole du jeu de cette année" , 0.1)
        mirror = Item("miroir" , "Le miroir murmure des fragments du passé, teintés de mystère. " , 1.7)
        dress = Item("robe" , "La robe offerte par Legend à Scarlette à son arrivée. " , 1.8)

        # Ajouter les items dans les rooms
        cottage.inventory = {book, potion}
        tower.inventory = {sword, stone}
        castle.inventory = {key}
        fountain.inventory = {crystal, bag}
        bridge.inventory = {butterfly}
        lodges.inventory = {mirror}
        forest.inventory = {dress}

        #Setup PNJs
        julian = Character("Julian", "le marin/navigateur", tower, ["Penses-tu être digne de la récompense ?" , "Je suis un connaisseur de Caraval, je peux t'aider" , "Rapporte moi le sac de Scarlette"])
        nigel = Character("Nigel", "le maître des secrets", bridge, ["Voulez-vous connaître un secret ?", "J'échange des secrets contre des objets précieux...", "Apportez-moi le cristal de la fontaine, et je vous révélerai un secret important.", "Le temps presse, les secrets ne durent pas éternellement...", "Je peux vous dire comment gagner Caraval... pour le bon prix.","Chaque objet a une histoire, chaque histoire a un prix."])
        scarlette = Character("Scarlette", "l'ancienne gagnante de Caraval", clockhouse, ["Comment puis-je t'aider ?" , "Je peux te proposer un marché intéréssant" , "Apporte moi la pièrre rouge et je pourrai te donner une information utile"])
        jovan = Character("Jovan", "l'artiste principale de Caraval", cave, ["Souviens-toi, rien ici n’est ce qu’il semble être. Trouve le papillon vert, et peut-être que je pourrai t'en dire plus"])
        aiko = Character("Aiko", "l'artiste qui documente les événements de Caraval", fountain, ["Les pages racontent beaucoup d'histoires, mais aucune ne donne toutes les réponses.", "Rien ici n’est gratuit, pas même les réponses. Si tu veux le code, cherche le miroir et la robe."])

        # Ajout des personnages dans les pièces
        tower.characters["julian"] = julian
        bridge.characters["nigel"] = nigel
        clockhouse.characters["scarlette"] = scarlette
        cave.characters["jovan"] = jovan
        fountain.characters["aiko"] = aiko

        #Setup wanted items
        #nigel = Character("Nigel", "le maître des secrets", bridge, ["Voulez-vous connaître un secret ?", "J'échange des secrets contre des objets précieux..."])
        nigel.wanted_items = {"cristal": "Ah ! Le cristal magique ! Voici un secret en échange : le premier chiffre du code est 7.", "grimoire": "Un ancien grimoire ! Je peux vous dire que Julian a un rôle bien différent des autres."}
        julian.wanted_items = {"sac": "Maintenant ce que je peux te dire c'est que le chiffre 5 est le chiffre fétiche de Legend."}
        scarlette.wanted_items = {"pierre": "Legend aime beaucoup les trèfles à 4 feuilles."}
        jovan.wanted_items = {"papillon": "Aiko connait les secrets de Caraval, elle pourra te donner la fin du code!"}
        aiko.wanted_items = {"miroir": "Le château de Caraval n'est pas un simple lieu, il donne accès à la destiné de Scarlette." , "robe" : "Le deuxième chiffre est 3."}

        #bridge.characters[nigel.name.lower()]= nigel

        # Create exits for rooms

        forest.exits = {"N" : None, "E" : swamp, "S" : tower, "O" : cottage, "U" : clouds, "D" :None }
        tower.exits = {"N" : forest, "E" : bridge, "S" : cave, "O" : lodges, "U" : clouds, "D" : None}
        cave.exits = {"N" : tower, "E" : clockhouse, "S" : castle, "O" : fountain, "U" : None, "D" : tunnels}
        cottage.exits = {"N" : None, "E" : forest, "S" : lodges, "O" : None, "U" : None, "D" : tunnels}
        swamp.exits = {"N" : None, "E" : None, "S" : bridge, "O" : forest, "U" : None, "D" :None}
        castle.exits = {"N" : cave, "E" : None, "S" : None, "O" : None, "U" : None, "D" :None}
        clockhouse.exits = {"N" : bridge, "E" : None, "S" : None, "O" : cave, "U" : None, "D" :None}
        bridge.exits = {"N" : swamp, "E" : None, "S" : clockhouse, "O" : tower, "U" : clouds, "D" : None}
        lodges.exits = {"N" : cottage, "E" : tower, "S" : fountain, "O" : None, "U" : None, "D" : clouds}
        tunnels.exits = {"N" : None, "S" : None, "O" : None, "E" : None, "U" : clockhouse, "D" : None}
        clouds.exits = {"N" : None, "S" : None, "O" : None, "E" : None, "U" : None, "D" : swamp}
        fountain.exits = {"N" : lodges, "S" : None, "O" : None, "E" : cave, "U" : tunnels, "D" : clouds}

        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = forest


    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
        return None
    
    #deplacer les pnj
    def move_pnj(self):
        for room in self.rooms:
            characters = list(room.characters.values())

            for character in characters:
                character.move()


    # Process the command entered by the player
    def process_command(self, command_string) -> None:
        if not command_string:
            return

    # Split the command string into a list of words
        list_of_words = command_string.split(" ")
        command_word = list_of_words[0].lower()

    # Normalize direction if present
        if len(list_of_words) > 1:
            normalized_directions = list_of_words[1].upper()
            if normalized_directions in self.direction_names:
                list_of_words[1] = self.direction_names[normalized_directions]
            elif command_word == "go":
                print(f"\n'{list_of_words[1]}' n'est pas une direction valide")
                return

    # Check if the command exists
        if command_word not in self.commands:
            print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
            return

    # Execute the command
        command = self.commands[command_word]
        command.action(self, list_of_words, command.number_of_parameters)
   
        if command_word == "go":
            self.move_pnj()

    # On print le welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans Caraval, où rien n'est ce qu'il parait être !")
        print("N'oubliez pas que ce n'est qu'un jeu... Ne vous y perdez pas")
        print("\nLe château murmure son secret à ceux qui écoutent. Le mot de passe est la clé, mais attention : il se cache dans les lieux où le réel et l’imaginaire se rencontrent. Trouve-le avant que la nuit ne s’achève.\n")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())
    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()

