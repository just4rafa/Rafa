
class Robot:
    def __init__(self, name, color, weight):  #Constructori
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):  #Functie
        print("My name is " + self.name)

# r1 = Robot()    #Crearea unui obiect fara constructori
# r1.name = "Alesca"
# r1.color = "red"
# r1.weight = ]23
# r1.introduce_self()   #Aplicarea Functiei

r1 = Robot("Alex,", "red", 90)   #Crearea unui obiect cu constructori
r1.introduce_self()


# I N H E R I T A N C E #

class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        pass