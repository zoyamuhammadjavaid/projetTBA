
class Command:
    """
    Cette classe répresente la commande. Une commande est composée d'un mot command,un str, une action et un nombres de parametres.

    Attributes:
        command_word (str): le mot command.
        help_string (str): le help str.
        action (function): l'action a exécutée lorsque la commande est demandée.
        number_of_parameters (int): Le nombre de parametres attendu par la commande.

    Methods:
        __init__(self, command_word, help_string, action, number_of_parameters) : Le constructor.
        __str__(self) : la representation string.

    Examples:

    >>> from actions import go
    >>> command = Command("go", "Permet de se déplacer dans une direction.", go, 1)
    >>> command.command_word
    'go'
    >>> command.help_string
    'Permet de se déplacer dans une direction.'
    >>> type(command.action)
    <class 'function'>
    >>> command.number_of_parameters
    1

    """

    # The constructor.
    def __init__(self, command_word, help_string, action, number_of_parameters):
        self.command_word = command_word
        self.help_string = help_string
        self.action = action
        self.number_of_parameters = number_of_parameters
    
    # The string representation of the command.
    def __str__(self):
        return  self.command_word \
                + self.help_string
    
