
##             Yugioh: JR (Joshua Rowe)
##                  Version 0.1
##
##      Author: Joshua Rowe - September 2012
##
##  Written while learning Python from: http://learnpythonthehardway.org,
##  Core Python Programming, Invent Your Own Computer Games with Python and
##  Making Games with Python & Pygame
##
##  A video game version of the Yugioh trading card game. Currently text-based
##  but will be graphical in the future.
##  My plan is for the architecture to be made so that I can apply the backend
##  to different platforms via webservice, and handle graphics on that platform
##  
##  This is my first game in Python and programming in general. Please give me
##  advice on my coding and engineering of the game.
##
################################################################################


# Errors:
# ImportError
# ConversionError

from random import randint

from errors import *



# Test mode:
test_mode = False   # Bypass usual gameplay to test specific features.
# See down below after phasecycle() to find the associated block.
# That is where the code you want tested is placed.


#test_answers = ["set","1","activate","1"]
test_answers = ["","1"]
test_current_element = 0



# Creates an object instance of class ErrorHandler()
error_handler = ErrorHandler()


#class ImportError(Exception):
    #eprint(string, on_color = "on_red")
    #pass


# Tests the ErrorHandler class.
# Final Game Build: Omitted
try:
    import lolztest
except ImportError:
    error_handler.raise_error("Import", "lolztest")

# Turns graphics on or off
# True = Graphics on / False = Graphics off
if graphics_setting == True:
    try:
        import pygame
    except ImportError:
        error_handler.raise_error("Import", "pygame")
        graphics_setting == False

    
#if graphics_setting == True:
 #   import pygame
 #   from pygame.locals import *
    #pygame.init()
    #screen = pygame.display.set_mode((468, 60))
    #pygame.display.set_caption('Yugioh Game')



# Converts a string into an integer.
def convert_int(string, error_print=True):
    try:
        return int(string)
    except ValueError:
        if error_print == True:
            eprint("ConversionError: %s could not be converted to an integer." % string, on_color = "on_red")
        return None 
    
def load_image(name, colorkey=None):    # Loads an image for use.
    # Status: Unknown
    # To do:
    # 1. Start implementing graphics into game before this is utilised.
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

def current_players():
    return players


# This function is shit and needs to be looked at or reimplemented
def destroy(players, area, both_players=True):  # Destroy a card - This should be implemented into
                                                # parser functionality at some point.
    if area == "all":
        cprint("(Enter: 'my' or 'enemy' + 'mf' or 'stf' + the corresponding number)", "yellow")
        cprint("(E.g. 'my mf 2')", "yellow")
        cprint("Player1:", "magenta")
        cprint ("Monster Field:", "cyan")
        players[0].mfield.list(False, print_names=True)
        cprint ("Spell & Trap Field:", "cyan")
        players[0].stfield.list(False, print_names=True)
        cprint("Player2:", "magenta")
        cprint ("Monster Field:", "cyan")
        players[1].mfield.list(False, print_names=True)
        cprint ("Spell & Trap Field:", "cyan")
        players[1].stfield.list(False, print_names=True)
        choice = parser.parse(raw_input("> "),players)
        print choice.parameter[0][1]
        print choice.parameter[1][0]
        if choice.parameter[0][1] == "mf" and isinstance(choice.parameter[1][1], int):
            #print "YOEJHAGBEFMSF"
            x = choice.parameter[1][1] - 1
            print x
            choice.determiner.mfield.removecard(choice.determiner.mfield.spaces[0][2])
        cprint("AFTER:", "green")
        cprint ("Monster Field:", "cyan")
        players[0].mfield.list(False, print_names=True)
        cprint ("Spell & Trap Field:", "cyan")
        players[0].stfield.list(False, print_names=True)
        cprint("Player2:", "magenta")
        cprint ("Monster Field:", "cyan")
        players[1].mfield.list(False, print_names=True)
        cprint ("Spell & Trap Field:", "cyan")
        players[1].stfield.list(False, print_names=True)
    if area == "stf":
        cprint("(Enter: 'my' or 'enemy' + the corresponding number)", "yellow")
        cprint("(E.g. 'my 2')", "yellow")
        
        cprint ("Spell & Trap Field:", "cyan")
        players[0].stfield.list(False, print_names=True)
        
        cprint ("Spell & Trap Field:", "cyan")
        players[1].stfield.list(False, print_names=True)
        choice = parser.parse(raw_input("> "),players)
        if choice.parameter[0][1] != None:
            cprint("Error", "red")
            return
        #print choice.parameter[0][1]
        print choice.parameter[1][0]
        #if choice.parameter[0][1] == "mf" and isinstance(choice.parameter[1][1], int):
            #print "YOEJHAGBEFMSF"
        x = choice.parameter[1][1] - 1
        print x
        choice.determiner.stfield.removecard(choice.determiner.stfield.spaces[0][2])
        cprint("AFTER:", "green")
        
        cprint ("Spell & Trap Field:", "cyan")
        players[0].stfield.list(False, print_names=True)
        
        cprint ("Spell & Trap Field:", "cyan")
        players[1].stfield.list(False, print_names=True)




        #card1 = players[0].mfield.spaces[0][2].name
        #print len(card1)
        #if len(card1) > 7:
        #    print "sjkbfnsef"
        #    card1.join('hfsef')
        #line = players[0].mfield.spaces[0][2].name
        #n = 7
        #card1 = [line[i:i+n] for i in range(0, len(line), n)]
        #part1 = card1[0]
        #part2 = card1[1]
        #part2.split
        #part3 = "       "
        #if card1[2]:
        #    part3 = card1[2]
        #else:
        #    part3 = "      "
        #print card1
        #part1 = "Monster"
        #part2 = "Card 2 "
        #part3 = "" + " " + " " + " " + " " + " " + " " + " "
        #print """
 #-------   -------   -------   -------   -------
#|monster| |monster| |monster| |monster| |monster|
#|zone 1 | |zone 2 | |zone 3 | |zone 4 | |zone 5 |
#|%s| |       | |       | |       | |       |
#|%s| |       | |       | |       | |       |
#|%s| |       | |       | |       | |       |
# -------   -------   -------   -------   -------
# -------   -------   -------   -------   -------
#|       | |       | |       | |       | |       |
#|       | |       | |       | |       | |       |
#|       | |       | |       | |       | |       |
#|       | |       | |       | |       | |       |
#|       | |       | |       | |       | |       |
#-------   -------   -------   -------   -------
#""" % (part1, part2, part3)


class ParsedCommand():
    def __init__(self, parameter, command=False, determiner=False):
        self.command = command
        self.determiner = determiner
        #if command != False:
        #    self.command = command
        #if determiner != False:

           # self.determiner = determiner

        self.parameter = parameter

class ParserError(Exception):
    pass


# Parser class. More to be written on this soon.
class Parser():
    def __init__(self):
        self.lexemes = {'set': 'command', 'activate': 'command',
                        'attack': 'command', 'check': 'command',
                        'summon': 'command', 'exit': 'command',
                        'eval': 'command',
                        'my': 'determiner', 'your': 'determiner', 'enemy': 'determiner',

                        'mf': 'field', 'mfield': 'field', 'stf': 'field', 'stfield': 'field',
                        'yes': 'option', 'no': 'option',

        'trap': 'type',
        'spell': 'type',
        'monster': 'type'
        }
        self.temp_lexemes = {}
    def query_field(self):
        pass   
    def temp_lexemes_update(self, players):     # Updates self.temp_lexemes which is the variable which holds the
                                                # current cards in your hand. This is so that you can pass a Card
                                                # name as a parameter and it will for example summon that card.
        player_cards = []
        for card in players[0].hand:
            player_cards.append(card.name)
        for card in player_cards:
            self.temp_lexemes[card] = "card"    
            # Adds a new key:value into self.temp_lexemes with each card in your hand.
        print self.temp_lexemes # Being used for testing purposes. Will be deleted later.
    def add_lexeme(self, word, type):
        self.lexemes[word] = type
    def scan(self, sentence):
        words = sentence.split()
        word_list = []
        for word in words:
            temp = convert_int(word, False)
            if isinstance(temp, int):
                num_tuple = ('number', temp)
                word_list.append(num_tuple)
            else:
                word_type = self.lexemes.get(word, 'error')
                word_list.append((word_type, word))
        print word_list
        return word_list

    def peek(self, word_list):  # returns the type of the next word in word_list
        if word_list:
            word = word_list[0]
            #print word[0]
            return word[0]
        else:
            return None

    def match(self, word_list, expecting):  # Deletes the word in word_list which is next.
        if word_list:
            word = word_list.pop(0)

            if word[0] == expecting:
                return word
            else:
                return None
        else:
            return None

    def parse_parameters(self, word_list, command):
        parameters = []
        parameters_remaining = 0
        print "Getting parameters for this command:"
        print command
        if command[1] == "set":
            #print self.peek(word_list)
            if self.peek(word_list) == 'type':
                print "This command is followed by a card type, which is:"
                card_type = self.match(word_list, 'type')
                print card_type
                parameters.append(card_type)
        if command[1] == "activate":
            #print self.peek(word_list)
            if self.peek(word_list) == 'type':
                print "This command is followed by a cardd type, which is:"
                card_type = self.match(word_list, 'type')
                print card_type
                parameters.append(card_type)
        if command[1] == "summon":
            print "Summon command."
            if self.peek(word_list) == "error":

                cards_in_hand = []

                print self.peek(word_list)
                for cards in self.temp_lexemes:
                    print cards
                    cards_in_hand.append(cards)
                if cards_in_hand:
                    parameters.append(cards_in_hand)


        return parameters

    def parse_command(self, word_list, command):

       
        parameters = self.parse_parameters(word_list, command)
        command_object = ParsedCommand(parameters, command=command)
        return command_object

    def parse_choice(self, players, word_list):
        
        #player_determiner = None
        parameters = []
        start = self.peek(word_list)
        print start
        if start == 'determiner':
            player = []
            player_determiner = self.match(word_list, 'determiner')
            print player_determiner
            
            if player_determiner[1] == "my":
                player = players[0]
            elif player_determiner[1] == "enemy":
                player = players[1]

            first_parameter = self.peek(word_list)
            print first_parameter

            if first_parameter == 'field':
                para1 = self.match(word_list, 'field')
                
                #print para1

                parameters.append(para1)

            if first_parameter == 'area':
                para1 = self.match(word_list, 'area')

                parameters.append(para1)
            if first_parameter == 'number':

                para2 = self.match(word_list, 'number')
                para1 = None
                parameters.append(para1)
                parameters.append(para2)






            second_parameter = self.peek(word_list)
            

            if second_parameter:
                if second_parameter == 'number':
                    para2 = self.match(word_list, 'number')
                    
                    parameters.append(para2)



        choice_object = ParsedCommand(parameters, determiner=player)
        print choice_object.determiner
        print choice_object.command
        print choice_object.parameter
        return choice_object


    def parse_sentence(self, word_list, players):
        start = self.peek(word_list)
        #print start

        if start == 'command':
            command = self.match(word_list, 'command')
            return self.parse_command(word_list, command)
        elif start == 'determiner':
            return self.parse_choice(players, word_list)
        #else:
            #return self.parse_choice(players, word_list)
        else:
            #raise ParserError('This is not a valid command.')
            #print "You must start with a command."
            return

    def parse(self, string, players):   # Parses a sentence and returns a ParserCommand object
        self.temp_lexemes_update(players)
        if string == "":
            return None
        else:
            word_list = self.scan(string)
            returned_object = self.parse_sentence(word_list, players)
        if returned_object:
            if len(returned_object.parameter) != 0:
                print "1 or more parameters"
            elif len(returned_object.parameter) == 0:
                print "no parameters given"
            elif returned_object.command:
                print "there was no parameters or a command"
            
            if returned_object.command:
                print "Passing parsed object to input_handler..."
                input_handler.input(players, string, parser_object=returned_object)
            else:
                return returned_object
            print "All handled."
        else:
            cprint ("Failed to return a parsed object.\nPlan B: Passing the string to input_handler.", "red")
            input_handler.input(players, string)

        
            
            
    #def check(self, players, string):

        
class RoutineController():

    def __init__(self):
        cprint("Initialised RoutineController", "green")



class Lifepoints(): # Handles lifepoints for players
    # methods:
    # increase(self, amount):
    # decrease(self, amount):
    # activate(self, type)

    def __init__(self):
        self.lifepoints = 8000
    def increase(self, amount):
        self.lifepoints += amount
    def decrease(self, amount):
        self.lifepoints -= amount
      
class Area():   # Class for handling other areas for players e.g. graveyard, can be used for any stack type area.

    def __init__(self, name):
        self.name = name
        self.list = []

    def addcard(self, card):
        self.list.append(card)
        cprint("Added %s to %s successfully." % (card.name, self.name), "green")

    def removecard(self, card):
        self.list.remove(card)
        cprint("Removed %s from %s successfully." % (card.name, self.name), "green")

    def listnames(self):
        for card in self.list:
            print card.name

    def select(self):
        for card in self.list:
            print card.name
        selected_card = input_handler.input_get("Which card? ")




class Player():     # Player class which holds data
    # Methods:

    # summon(self, cardname=None)
    # battle(self)
    # set(self, type)
    # activate(self, type)
    # activate_trap(self)
    # hand_count(self)
    # draw(self, card=False)

    def __init__(self, name, decklist):
        self.name = name
        #self.hand = []
        self.hand = Area("%s's Hand" % self.name)

        self.deck = Deck(decklist)
        self.mfield = Field("monster")
        self.stfield = Field("spelltrap")
        self.lifepoints = Lifepoints()
        self.graveyard = Area("%s's graveyard" % self.name)

    def summon(self, cardname=None):    # summon function, working on taking a cardname and summoning that monster
        print "Summon function of %s" % self.name

        if cardname:
            print "Sent Summon function a card name"

        # Gets all monster cards in hand, prints their names, and then adds it to monster_cards
        monster_cards = []

        for card in self.hand.list:
            if card.type == "monster":
                print card.name
                monster_cards.append(card)


        # If you have no monster cards in your hand it prints and error and ends the function
        if len(monster_cards) == 0:
            cprint("Error: You have no monster cards in your hand.", "red")
            return

        # gets input from player expecting a number corresponding to the monsters names which were printed
        # if it doesn't convert into an integer, it prints an error message and exits the function
        result = input_handler.input_get("Which monster would you like to summon? ")
        result = convert_int(result)
        if result == None:
            cprint("This is not a valid option.", "red")
            return 

        result -= 1 # subtracts 1 so that it will work with the array index'
        card = monster_cards[result]    # This is the card the player chose.
        print "You chose %s " % card.name   # prints name of chosen card


        # Choose monsters to tribute if monster level >= 4

        # If the monster level if 4 just default it to 0 tributes
        tribute_number = 0

        # if card is 5-6 or 7-8, set tribute number to 1 or 2 respectively
        if card.level == 5 or card.level == 6:
            tribute_number = 1
        elif card.level == 7 or card.level == 8:
            tribute_number = 2

        if tribute_number > 0:
            print "You must tribute %s monster to summon this monster." % tribute_number

            # While loop: decrement tribute_number for every tribute until 0

            while tribute_number > 0:

                tribute_card = 0

                input_handler.execute("mf", players)
                result = input_handler.input_get("Which monster do you want to tribute? ")
                result = convert_int(result) 
                result -= 1

                monsterfield_cards = self.mfield.list("monster")
                tribute_card = monsterfield_cards[result]

                # Move chosen tribute card to graveyard.
                self.mfield.removecard(tribute_card)
                self.graveyard.addcard(tribute_card)

                tribute_number -= 1



        # Choose position to summon monster in
        monster_position = convert_int(input_handler.input_get("[0 = Face-up attack, 2 = Face-down defense]\nWhat position do you want to summon it in? "))

        # Remove card from hand
        self.hand.removecard(card)

        # Add card to monsterfield
        self.mfield.addcard(card, monster_position)

        # Print success message
        cprint("You have successfully summoned: %s" % card.name, "green")


        # TODO:
        # Implement error handling if you don't have monsters on the field, it will also need to look ahead if it's a
        # double tribute.


    def battle(self):
        print "Battle function of %s" % self.name
        enemy_player = current_players()[1]
        monster_list = self.mfield.list("monster")
        enemy_monster_list = enemy_player.mfield.list("monster", print_names=True)
        if len(monster_list) == 0:
            cprint("Error: You have no cards on the monsterfield.", "red")
            
            return
        for monster_card in monster_list:
            print monster_card.name
        while True:    
            result_player = input_handler.input_get("Which monster do do you want to use?\n> ")
            try:
                result_player = int(result_player)
                result_player -= 1
                #print result_player
                break
            except:
                cprint("You need to pass a number which corresponds to a card.", "red")
        if len(enemy_monster_list) == 0:
            cprint("Error: Your opponent has no cards on the monsterfield.", "red")
            
            return
        while True:    
            result_enemy = input_handler.input_get("Which monster do do you want to fight?\n> ")
            try:
                result_enemy = int(result_enemy)
                result_enemy -= 1
                #print result_enemy
                break
            except:
                cprint("You need to pass a number which corresponds to a card.", "red")
                
        outcome = enemy_monster_list[result_enemy].attack - monster_list[result_player].attack
        #print outcome
        if outcome == 0:
            cprint("The battle was a draw!", "cyan")
            enemy_player.mfield.removecard(enemy_monster_list[result_enemy])
            self.mfield.removecard(monster_list[result_player])
        if outcome < 0:
            cprint("You won the battle!", "green")
            enemy_player.mfield.removecard(enemy_monster_list[result_enemy])
            enemy_player.lifepoints.increase(outcome) # increase by a negative means they lose lifepoints :P
        if outcome > 0:
            cprint("You lost the battle :(", "red")
            self.mfield.removecard(monster_list[result_player])    
            self.lifepoints.increase(outcome)          # increase by a negative means they lose lifepoints :P
            
    def set(self, type):    # set a trap OR spell depending on what type you send to it
        card_type_list = []

        for card in self.hand:
            if card.type == type:
                print card.name
                card_type_list.append(card)
        if len(card_type_list) == 0:
            cprint("You don't have any %s cards in your hand." % type, "red")
            return

        result = input_handler.input_get("Which %s would you like to set? " % type)
        result = convert_int(result)
        if result == None:
            cprint("Not a valid option.", "red")
            return
        result -= 1
        card = card_type_list[result]
        print "You chose %s " % card.name
        self.hand.remove(card)
        self.stfield.addcard(card, 3)
    def activate(self, type):   # activate a spell card
        
        activate_type = input_handler.input_get("Would you like to activate from hand or field:\n> ")
        if activate_type == "hand":
            area = self.hand.list
        elif activate_type == "field":
            area = self.stfield.list("spell") 
        else:
            cprint("This is not a valid option.", "red")
            return
        card_type_list = []
        for card in area:
            if card.type == type:
                print card.name
                card_type_list.append(card)

        if len(area) == 0:
            cprint("You have no spells to activate.", "red")
            return
        result = input_handler.input_get("Which %s would you like to activate? " % type)
        result = convert_int(result) - 1
        if result == None:
            cprint("This is not a valid option.", "red")
        card = card_type_list[result]
        if activate_type == "hand":
            self.stfield.addcard(card, 4)
            self.hand.removecard(card)
            cprint("You have successfully activated: %s" % card.name, "green")
            exec card.effect
            self.stfield.removecard(card)
            self.graveyard.addcard(card)
        elif activate_type == "field":
            self.stfield.updatestate(card, 4)
            exec card.effect
            self.stfield.removecard(card)
    def activate_trap(self):    # activate a trap card
        
        trap_list = self.stfield.list("trap", print_names = True)
        if len(trap_list) == 0:
            cprint("You have no trap cards on the field to activate.", "red")
            return
        result = input_handler.input_get("Which trap would you like to activate?\n> ")
        result = convert_int(result)
        if result == None:
            cprint("This is not a valid option.", "red")
            return
        result -= 1
        card = trap_list[result]
        self.stfield.updatestate(card, 4)
        exec card.effect
        self.stfield.removecard(card)
        cprint("You have successfully activated: %s" % card.name, "green")
        self.graveyard.addcard(card)
    def hand_count(self):
        return len(self.hand)

    def draw(self, card=False):
        if card != False:
            hand_card = self.deck.draw(card)
            self.hand.addcard(hand_card)
            print "You drew the card %s" % hand_card.name
        else:
            deck_max = self.deck.deck_count()
            deck_max -= 1
            draw_card_number = randint(0, deck_max)
            print "Random integer between 0 and 1 less than deck count: %i" % draw_card_number
            hand_card = self.deck.draw(draw_card_number)
            #self.hand.append(hand_card)
            self.hand.addcard(hand_card)
            print "You drew the card %s" % hand_card.name
    # Archived Version:

    #def draw(self, card=False):
    #    if card != False:
    #        #print "Drawing specific cards has not been finished yet."
    #        hand_card = self.deck.draw(card)
    #        self.hand.append(hand_card)
    #        print "You drew the card %s" % hand_card.name


    #    else:
    #        
    #        deck_max = self.deck.deck_count()
    #        deck_max -= 1
    #        draw_card_number = randint(0, deck_max)
    #        print "Random integer between 0 and 1 less than deck count: %i" % draw_card_number
    #        hand_card = self.deck.draw(draw_card_number)
    #        self.hand.append(hand_card)
    #        print "You drew the card %s" % hand_card.name

class GraphicsHandler():
    def __init__(self):
        # Player 1
        p1m1, p1m2, p1m3, p1m4, p1m5 = "", "", "", "", ""
        p1st1, p1st2, p1st3, p1st4, p1st5, p1fs = "", "", "", "", "", ""
        p1h_count = 0
        p1h = []
        self.p1_elements = [p1m1, p1m2, p1m3, p1m4, p1m5, p1st1, p1st2, p1st3, p1st4, p1st5, p1fs, p1h_count, p1h]
        # Player 2
        p2m1, p2m2, p2m3, p2m4, p2m5 = "", "", "", "", ""
        p2st1, p2st2, p2st3, p2st4, p2st5, p2fs = "", "", "", "", "", ""
        p2h_count = 0
        p2h = []
        self.p2_elements = [p2m1, p2m2, p2m3, p2m4, p2m5, p2st1, p2st2, p2st3, p2st4, p2st5, p2fs, p2h_count, p2h]
        
        
    def get_state(self, players):
        element_counter = 0 # counter for index of p1_elements to 
                            # cross reference with what variables ill be retrieving to fill p1_elements
        while element_counter < 13: # 12 values to fill so this is 13
            if element_counter <= 4:    # for first five elements do this:
                
                element_image = player1.mfield.spaces[element_counter][2]   # image string is equal to the corresponding
                                                                            # card data in the monsterfield space with the
                                                                            # selected index
                if element_image == 0:    # if the data is equal to 0 (aka empty) then:
                    element_image = ""    # empty string = dont display image
                else:
                    element_image = element_image.name  # if data does exist element_image is equal to the string location
                                                        # for the card's image data
                self.p1_elements[element_counter] = element_image
                
            if element_counter > 4 and element_counter <= 9:    # if counter is above 4 and below or equal to 9
                                                                # aka next 5
                spelltrap_counter = element_counter - 5         # takes 5 off so that it corresponds with the list indices
                element_image = player1.stfield.spaces[spelltrap_counter][2]
                if element_image == 0:
                    element_image = "" # empty string = dont display image
                else:
                    element_image = element_image.name
                self.p1_elements[element_counter] = element_image
            element_counter += 1    # adds 1 to the counter
        #print self.p1_elements
                
# Cards:
#card1 = Monster("Monster Card 1", "monster", "normal", 4, 1000, 500)
#card2 = Monster("Monster Card 2", "monster", "normal", 4, 2000, 300)
#card3 = Monster("Monster Card 3", "monster", "normal", 4, 1500, 450)
#card4 = Monster("Monster Card 4", "monster", "normal", 4, 600, 2000)
#card5 = Spell("Spell Card 1", "spell", "This is spell card 1", "print 'I am number 1'")
#card6 = Spell("Spell Card 2", "spell", "This is spell card 2", "print 'I am number 2'")
#card7 = Spell("Spell Card 3", "spell", "This is spell card 3", "print 'I am number 3'")
#card8 = Spell("Trap Card 1", "trap", "This is trap card 1", "print 'I am number 5'")
#card9 = Spell("Trap Card 2", "trap", "This is trap card 2", "print 'I am number 7'")
#card10 = Spell("Trap Card 3", "trap", "This is trap card 3", "print 'I am number 9'")
#card11 = Spell("Mystical Space Typhoon", "spell", "Destroy 1 Spell or Trap Card on the field.", "destroy(players, 'stf', both_players=True)")
card1 = Monster("Blue Eyes White Dragon", "monster", "normal", 8, 3000, 2500)
card2 = Spell("Blue Medicine", "spell", "Increase your lifepoints by 400.", "players[0].lifepoints.increase(400)")
card3 = Monster("Queen's Knight", "monster", "normal", 4, 1500, 1600)
card4 = Monster("Noble Knight Artorigus", "monster", "normal", 4, 1800, 1800)
card5 = Spell("Monster Reborn", "spell", "Select one monster in either player's graveyard and special summon it to your side of the field.", "")
card6 = Spell("Pot of Greed", "spell", "Draw 2 cards.", "players[0].draw()")
card7 = Monster("Joshua IS Awesome", "monster", "normal", 4, 2000, 1700)
card8 = Trap("Sakuretsu Armor", "trap", "Destroy an attacking monster.", "")

# Setup player variables
player1_decklist = [card1, card2, card3, card4, card5, card6, card7]#, card8, card9, card10,card11]
player2_decklist = [card1, card2, card3, card4, card5, card6, card7]#, card8, card9, card10]
player1 = Player("Joshua", player1_decklist)
player2 = Player("Sean", player2_decklist)
test_details = [test_mode, test_answers]
input_handler = Input(test_details)
graphics_handler = GraphicsHandler()
parser = Parser()
routine_controller = RoutineController()


# Draws specific cards

player1.draw(card1)
player1.draw(card2)
player1.draw(card3)
player1.draw(card4)
player1.draw(card5)
player1.draw(card6)

player2.draw(card1)
player2.draw(card2)
player2.draw(card3)
player2.draw(card4)
player2.draw(card5)
player2.draw(card6)

#fieldimage, fieldrect = load_image('Field.jpg', -1)

# Cycles through each phase for the active player's turn
def phasecycle():
    # Phase Order:
    # 1) Draw Phase
    #   - 1) Routine check
    #   - 2) Draw a card for current player. STATUS: Not Started
    #   - 3) Routine check
    # 2) Standby Phase
    # 3) Main Phase 1
    # 4) Battle Phase
    # 5) Main Phase 2
    # 6) End Phase
    print "Phasecycle:Start"    # Start of turn.
    print "Current player is: %s" % players[0].name # Prints current player' name
    active_phase = 1 # Sets active_phase to draw phase.
    while active_phase == 1: # Draw Phase
        print "Draw Phase"
        active_phase += 1
    while active_phase == 2: # Standby Phase
        print "Standby Phase"
        active_phase += 1
    while active_phase == 3: # Main Phase 1
        print "Main Phase 1"

        # Testing stuff:
        #input_handler.input(players, input_handler.input_get("What do you want to do: "))
        #input_string = input_handler.input_get("What to do bru: ")
        #parser.parse(input_string,players)

        input_handler.input(players, input_handler.input_get("This is the command prompt: "))
        proceed_phase = input_handler.input_get("Would you like to end Main Phase 1? ")   # Ask user if they want to end the current phase
            
        if proceed_phase in ('yes', 'y', 'proceed', 'ok'):
            active_phase += 1
        
    # Battle Phase  
    while active_phase == 4: 
        print "Battle Phase"
        active_phase += 1

    # Main Phase 2
    while active_phase == 5: 
        print "Main Phase 2"
        
        proceed_phase = input_handler.input_get("Would you like to end Main Phase 2? ")
        # If you respond with "yes" or "y" it will continue to End Phase
        if proceed_phase == "yes" or proceed_phase == "y":
            active_phase += 1
    while active_phase == 6:
        print "End Phase"
        #proceed_phase = input_handler.input_get("Would you like to end your turn? ")
        #if proceed_phase == "yes" or proceed_phase == "y":
        active_phase += 1
    print "Phasecycle:End"  # End of turn.
    
players = [player1, player2]



# Test mode:
# Bypass usual gameplay to test specific features.
if test_mode:
    print "Test mode!"
    print "Test 1:"
    parser.parse("summon Monster Card 1", players)


    
    


    
else:
    cprint("Test mode not engaged.", "yellow")
    while True:
    
        graphics_handler.get_state(players)
        phasecycle()
    
        # Switch current player
        if players[0] == player1:
            players = [player2, player1]
        else:
            players = [player1, player2]
            #input_handler.input(input_handler.input_get("What do you want to do: "), players)
    