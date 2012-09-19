import os, sys

class Input():
    def __init__(self, test_details):
        self.commands_list = ["summon", "spell", "exit", "trap", "hc", "gv", "rp", "hand", "mf", "stf", "save",
                               "help", "battle", "report", "settings", "test"]
        self.test_mode = test_details[0]
        self.test_answers = test_details[1]
        self.test_current_element = 0
    def input_get(self,prompt):
        if self.test_mode == True:
            print prompt,
            
            print self.test_answers[self.test_current_element]
            string = self.test_answers[self.test_current_element]
            self.test_current_element += 1
        else:
            string = raw_input(prompt)
        return string
    def input(self, string, players):
        self.authorise(string, players)

    def authorise(self, string, players):
        for command in self.commands_list:
            if string == command:
                self.execute(command, players)
                break

    def execute(self, string, players):
        if string == "summon":
            print "Summon command currently in development."
            players[0].summon()
        elif string == "battle":
            players[0].battle()
        elif string == "spell":
            spell_command_type = input_get("Set or activate spell? ")
            if spell_command_type == "set":
                players[0].set("spell")
            elif spell_command_type == "activate":
                players[0].activate("spell")
        elif string == "exit":
            print "Exiting Game..."
            sys.exit()
        elif string == "trap":
            print "yo"
            trap_command_type = self.input_get("Set or activate trap? ")
            if trap_command_type == "set":
                players[0].set("trap")
            elif trap_command_type == "activate":
                players[0].activate_trap()
        elif string == "hc":
            print "Hand Count command is currently in development."
            print players[0].hand_count()
        elif string == "gv":
            print "Graveyard command in development."
        elif string == "rp":
            print "Removed from Play command in development."
        elif string == "hand":
            print "Your hand:"
            for card in players[0].hand:
                print card.name,
                print ",",
            print ""
        elif string == "lp":
            print player1.lifepoints
            print player[0].lifepoints.lifepoints
        elif string == "mf":
            #print "Monsterfield command in development."
            print "Monster Field:"
            players[0].mfield.list(False)
        elif string == "stf":
            #print "Spelltrapfield command in development."
            print "Spell and Trap Field:"
            players[0].stfield.list(False)
        elif string == "save":
            print "Save command in development."
        elif string == "help":
            print "Help command in development."
        elif string == "report":
            print "Report command in development."
        elif string == "settings":
            print "Settings command in development."
        elif string == "test":
            print "Test command: Currently testing the Draw method"
            players[0].draw(False)