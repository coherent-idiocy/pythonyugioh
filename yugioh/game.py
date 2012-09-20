
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

## TODO LIST - Global list of tasks (when I remember to update them!)
##
##  - Add a lexicon to deconstruct sentences and identify what wants to be done
##      - Split up commands e.g. "spell" and then identify a card "Pot of Greed"
##        so that game automatically figures out what you want to do.
##          - Prompts for "Is that what you wanted to do:" so that nothing bad
##            is executed accidently.
##  - Implement a help command/function to help people with playing the game
##  - Move Player class to another file
##  - Get get_input() function working properly
##
################################################################################

import os

from random import randint
from cards import Monster, Spell, Trap, Deck
from input import Input


graphics_setting = True
colour_text = True
test_mode = False

test_answers = ["set","1","activate","1"]
test_current_element = 0


if colour_text == True:
    try:
        from termcolor import *
        def eprint(text, on_color):
            cprint(text, on_color = on_color)
    except ImportError:
        def cprint(text, colour):
            print text
        def eprint(text, on_color):
            print text
        eprint("ImportError: termcolor could not be imported.", on_color = "on_red")
else:
    def cprint(text, colour):
        print text
    def eprint(text, on_color):
        print text
        
class InputError(Exception):
    pass

try:
    import lolztest
except ImportError:
    eprint("ImportError: lolztest could not be imported.", on_color = "on_red")
    
if graphics_setting == True:
    import pygame
    from pygame.locals import *
    #pygame.init()
    #screen = pygame.display.set_mode((468, 60))
    #pygame.display.set_caption('Yugioh Game')

def convert_int(string):
    try:
        result = int(string)
    except:
        eprint("ConversionError: %s could not be converted to an integer." % string, on_color = "on_red")
        result = None
    return result
   
    
def load_image(name, colorkey=None):
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


class Lifepoints():
    def __init__(self):
        self.lifepoints = 8000
    def increase(self, amount):
        self.lifepoints += amount
    def decrease(self, amount):
        self.lifepoints -= amount
      
# States: 0 = face-up attack, 1 = face-up defense , 2 = face-down defense, 
# 3 = face-down spell/trap , 4 = face-up spell/trap 
class Field():

    def __init__(self, field_type):
        self.type = field_type
        self.space1 = [0,0,0]
        self.space2 = [0,0,0]
        self.space3 = [0,0,0]
        self.space4 = [0,0,0]
        self.space5 = [0,0,0]
        self.spaces = [self.space1,self.space2,self.space3,self.space4,self.space5]
    def addcard(self, card, position):
        for space in self.spaces:
            if space[0] == 0:
                print "Found an open space"
                space[0], space[1], space[2] = 1, position, card
                print space
                print space[2].name
                break
        print "After break"
    def removecard(self, card):
        for space in self.spaces:
            if space[0] == 1:
                if space[2] == card:
                    space[0] = 0
                    space[1] = 0
                    space[2] = 0
    def updatestate(self, card, state):
        for space in self.spaces:
            if space[2] == card:
                space[1] == state
    def list(self, type, print_names=False):
        return_type = []
        if type == False:
            for space in self.spaces:
                if space[0] == 1:
                    print space[2].name
        elif type == "spell":
            for space in self.spaces:
                if space[0] == 1:
                    if space[2].type == "spell":
                        return_type.append(space[2])
            return return_type
        elif type == "monster":
            for space in self.spaces:
                if space[0] == 1:
                    if space[2].type == "monster":
                        return_type.append(space[2])
            return return_type
        elif type == "trap":
            for space in self.spaces:
                if space[0] == 1:
                    if space[2].type == "trap":
                        return_type.append(space[2])
                        if print_names == True:
                            print space[2].name
            return return_type

class Player():
    def __init__(self, name, decklist):
        self.name = name
        self.hand = []
        self.deck = Deck(decklist)
        self.mfield = Field("monster")
        self.stfield = Field("spelltrap")
        self.lifepoints = Lifepoints()
    def summon(self):
        print "Summon function of %s" % self.name
        monster_cards = []
        for card in self.hand:
            if card.type == "monster":
                print card.name
                monster_cards.append(card)
        if len(monster_cards) == 0:
            cprint("Error: You have no monster cards in your hand.", "red")
            return
        result = input_handler.input_get("Which monster would you like to summon? ")
        result = int(result)
        result -= 1
        card = monster_cards[result]
        print "You chose %s " % card.name
        if card.level <= 4:
            self.hand.remove(card)
            self.mfield.addcard(card, 0)
            cprint("You have successfully summoned: %s" % card.name, "green")
        elif card.level <= 6:
            while True:
                print "You must tribute a monster to summon this monster.\n"
                monsterfield_cards = self.mfield.list("monster", print_names=True)
                print monsterfield_cards.count
                if len(monsterfield_cards) == 0:
                    cprint("You have no monsters to tribute.", "red")
                    return
                result = input_handler.input_get("Which monster would you like to tribute?\n> ")
                result = convert_int(result)
                if result != None:
                    break
            result -= 1
            tribute_card = monsterfield_cards[result]
            self.mfield.removecard(tribute_card)
            self.hand.remove(card)
            self.mfield.addcard(card, 0)
            cprint("You have successfully summoned: %s" % card.name, "green")



        elif card.level <= 8:
            print "You must tribute 2 monsters to summon this monster.\n"
            print "This hasn't been implemented yet."



    def battle(self):
        print "Battle function of %s" % self.name
        enemy_player = current_players()[1]
        monster_list = self.mfield.list("monster")
        enemy_monster_list = enemy_player.mfield.list("monster")
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
            
    def set(self, type):
        card_type_list = []
        for card in self.hand:
            if card.type == type:
                print card.name
                card_type_list.append(card)
        result = input_handler.input_get("Which %s would you like to set? " % type)
        result = int(result)
        result -= 1
        card = card_type_list[result]
        print "You chose %s " % card.name
        self.hand.remove(card)
        self.stfield.addcard(card, 3)
    def activate(self, type):
        
        activate_type = input_handler.input_get("Would you like to activate from hand or field:\n> ")
        if activate_type == "hand":
            area = self.hand
        elif activate_type == "field":
            area = self.stfield.list("spell") 
        card_type_list = []
        for card in area:
            if card.type == type:
                print card.name
                card_type_list.append(card)
        result = input_handler.input_get("Which %s would you like to activate? " % type)
        result = int(result) - 1
        card = card_type_list[result]
        if activate_type == "hand":
            self.stfield.addcard(card, 4)
            self.hand.remove(card)
            cprint("You have successfully activated: %s" % card.name, "green")
            exec card.effect
            self.stfield.removecard(card)
        elif activate_type == "field":
            self.stfield.updatestate(card, 4)
            exec card.effect
            self.stfield.removecard(card)
    def activate_trap(self):
        
        trap_list = self.stfield.list("trap", print_names = True)
        result = input_handler.input_get("Which trap would you like to activate?\n> ")
        result = int(result)
        result -= 1
        card = trap_list[result]
        self.stfield.updatestate(card, 4)
        exec card.effect
        self.stfield.removecard(card)
        cprint("You have successfully activated: %s" % card.name, "green")
    def hand_count(self):
        return len(self.hand)
    def draw(self, card):
        if card != False:
            print "Drawing specific cards has not been implemented yet."
        else:
            
            deck_max = self.deck.deck_count()
            deck_max -= 1
            draw_card_number = randint(0, deck_max)
            #print "Random integer between 0 and 1 less than deck count: %i" % draw_card_number
            hand_card = self.deck.draw(draw_card_number)
            self.hand.append(hand_card)
            print "You drew the card %s" % hand_card.name

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
card1 = Monster("Monster Card 1", "monster", 4, 1000, 500)
card2 = Monster("Monster Card 2", "monster", 5, 2000, 300)
card3 = Monster("Monster Card 3", "monster", 6, 1500, 450)
card4 = Monster("Monster Card 4", "monster", 4, 600, 2000)
card5 = Spell("Spell Card 1", "spell", "This is spell card 1", "print 'I am number 1'")
card6 = Spell("Spell Card 2", "spell", "This is spell card 2", "print 'I am number 2'")
card7 = Spell("Spell Card 3", "spell", "This is spell card 3", "print 'I am number 3'")
card8 = Spell("Trap Card 1", "trap", "This is trap card 1", "print 'I am number 5'")
card9 = Spell("Trap Card 2", "trap", "This is trap card 2", "print 'I am number 7'")
card10 = Spell("Trap Card 2", "trap", "This is trap card 3", "print 'I am number 9'")

player1_decklist = [card1, card2, card3, card4, card5, card6, card7, card8, card9, card10]
player2_decklist = [card1, card2, card3, card4, card5, card6, card7, card8, card9, card10]
player1 = Player("Joshua", player1_decklist)
player2 = Player("Steven", player2_decklist)
test_details = [test_mode, test_answers]
input_handler = Input(test_details)
graphics_handler = GraphicsHandler()

player1.draw(False)
player1.draw(False)
player1.draw(False)
player1.draw(False)
player2.draw(False)
player2.draw(False)
player2.draw(False)
player2.draw(False)
#fieldimage, fieldrect = load_image('Field.jpg', -1)

def phasecycle():       # Cycles through each phase for the active player's turn
    print "Phasecycle:Start"
    print "Current player is: %s" % players[0].name
    active_phase = 1
    while active_phase == 1:
        print "Draw Phase"
        active_phase += 1
    while active_phase == 2:
        print "Standby Phase"
        active_phase += 1
    while active_phase == 3:
        print "Main Phase 1"
        input_handler.input(input_handler.input_get("What do you want to do: "), players)
        proceed_phase = input_handler.input_get("Would you like to end Main Phase 1? ")   # Ask user if they want to end the current phase
            
        if proceed_phase in ('yes', 'y', 'proceed', 'ok'):
            active_phase += 1
        
    while active_phase == 4:
        print "Battle Phase"
        active_phase += 1
    while active_phase == 5:
        print "Main Phase 2"
        
        proceed_phase = input_handler.input_get("Would you like to end Main Phase 2? ")
        if proceed_phase == "yes" or proceed_phase == "y":
            active_phase += 1
    while active_phase == 6:
        print "End Phase"
        proceed_phase = input_handler.input_get("Would you like to end your turn? ")
        if proceed_phase == "yes" or proceed_phase == "y":
            active_phase += 1
    print "Phasecycle:End"
    
players = [player1, player2]  
if test_mode:
    print "Test mode!"
    input_handler.input("trap", players)
    print "Test"
    input_handler.input("trap", players)
    
else:
    while True:
    
        graphics_handler.get_state(players)
        phasecycle()
    
        # Switch current player
        if players[0] == player1:
            players = [player2, player1]
        else:
            players = [player1, player2]
            #input_handler.input(input_handler.input_get("What do you want to do: "), players)
    