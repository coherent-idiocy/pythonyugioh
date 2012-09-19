class Monster():
    def __init__(self, name, type, level, attack, defense):
        self.name = name
        self.type = type
        self.level = level
        self.attack = attack
        self.defense = defense

class Spell():
    def __init__(self, name, type, description, effect):
        self.name = name
        self.type = type
        self.description = description
        self.effect = effect

class Trap():
    def __init__(self, name, type, description, effect):
        self.name = name
        self.type = type
        self.description = description
        self.effect = effect

class Deck():
    def __init__(self, deck_list):
        self.deck = deck_list
    def deck_count(self):
        return len(self.deck)
    def draw(self, draw_card):
        if isinstance(draw_card, int):
            #print "You gave me an integer"
            card = self.deck[draw_card]
            self.deck.remove(card)
            return card