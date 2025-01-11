from room import Room
from item import Item

class SecuredRoom(Room):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.is_locked = True
        self.password = "7354"  # Voici le mdp à trouver via des échanges avec les PNj
        self.legend = Item("Légend", "Légend, le maître du Caraval, peut répondre à n'importe quel de vos questions", 0.1)
        self.key = Item("clé_dorée", "une clé en or massif qui brille d'une lueur mystérieuse", 0.1)
        self.wrong_attemps = 0


    def unlock(self, password, game):
        if password == self.password:
            self.is_locked = False
            print("\nLe château s'ouvre dans un grondement sourd...")
            print("Le maître de Caraval, Legend, apparaît devant vous dans un tourbillon d'étincelles dorées !")
            print("\n*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*")
            print("Les murs du château se mettent à scintiller de mille feux,")
            print("des étoiles dansent autour de vous alors que la magie de Caraval")
            print("vous enveloppe. Une voix mystérieuse résonne :")
            print('\n"Félicitations, aventurier intrépide !"')
            print('"Vous avez percé les mystères de Caraval et prouvé votre valeur."')
            print('"Le jeu est terminé, mais la magie perdurera dans vos souvenirs..."')
            print("\nVotre quête est achevée. Vous pouvez désormais quitter le jeu")
            print("en tapant 'quit', emportant avec vous les secrets de Caraval.")
            print("*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*\n")
            self.inventory.add(self.legend)
            self.inventory.add(self.key)
            game.finished = True
            return True
        else:
            self.wrong_attemps +=1

            if self.wrong_attemps >= 2:
                print("\n*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*")
                print("Une onde de choc magique vous traverse alors que le château")
                print("rejette violemment votre dernière tentative !")
                print('\n"Vous avez échoué trop de fois", tonne la voix de Legend.')
                print('"Les secrets de Caraval resteront à jamais hors de votre portée..."')
                print("\nGAME OVER - Vous avez perdu")
                print("*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*\n")
                game.finished = True  
                return False
            
            else:
                print("\nUn frisson glacé parcourt votre échine tandis que le château")
                print("refuse de vous livrer ses secrets. Le code entré n'est pas le bon...")
                print("La voix de Legend semble murmurer : 'Cherchez les indices, ils sont")
                print("dispersés dans le monde de Caraval...'\n")
                return False

