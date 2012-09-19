from nose.tools import *
from yugioh.cards import Monster, Spell, Trap, Deck

def test_monster():
	# def __init__(self, name, type, level, attack, defense):
	card1 = Monster("Celtic Guardian", "monster", 4, 1500, 1200)
	assert_equal(card1.name, "Celtic Guardian")

def test_spell():
	# def __init__(self, name, type, description, effect):
	card2 = Spell("Pot of Greed", "spell", "Draw 2 cards.", "print 'not implemented yet'")
	assert_equal(card2.name, "Pot of Greed")
	assert_equal(card2.description, "Draw 2 cards.")

def test_trap():
	# def __init__(self, name, type, description, effect):
	card3 = Trap("Trap Hole", "trap", "Destroy 1 monster with less than 1500 attack.", "print 'not implemented yet'")
	assert_equal(card3.name, "Trap Hole")
	assert_equal(card3.description, "Destroy 1 monster with less than 1500 attack.")
	assert_equal(card3.effect, "print 'not implemented yet'")

def test_deck():
	card1 = Monster("Celtic Guardian", "monster", 4, 1500, 1200)
	card2 = Spell("Pot of Greed", "spell", "Draw 2 cards.", "print 'not implemented yet'")
	card3 = Trap("Trap Hole", "trap", "Destroy 1 monster with less than 1500 attack.", "print 'not implemented yet'")
	deck1_list = [card1, card2, card3]
	deck1 = Deck(deck1_list)
	assert_equal(deck1.deck_count(), 3)
	assert_equal(deck1.draw(1), card2)
