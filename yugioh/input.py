import os, sys

class InputError(Exception):
    pass

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
    def input(self, players, string, parser_object=False):
        if parser_object:
            print "Gave this Input() a parser_object"
            self.authorise(players, parser_object=parser_object)
        else:
            self.authorise(players, string)

    def authorise(self, players, string="default", parser_object=False):
        if string != "default":
            for command in self.commands_list:
                if string == command:
                    self.execute(command, players)
                    break
        elif parser_object:
            print "Authorising parser_object."
            print "parser_object.command = "
            print parser_object.command[1]
            print "parser_object.parameter[0][0] = "
            if parser_object.parameter:

                print parser_object.parameter[0][0]
            else:
                print "No parameters were given"
                self.execute(parser_object.command[1], players)
            if parser_object.parameter:
                if parser_object.command[1] == 'set' and parser_object.parameter[0][0] == 'type':
                    players[0].set(parser_object.parameter[0][1])
                if parser_object.command[1] == 'activate' and parser_object.parameter[0][0] == 'type':
                    players[0].activate(parser_object.parameter[0][1])
            else:
                for command in self.commands_list:

                    if parser_object.command[1] == command:
                        print "Matched command to a command in commands_list."
                        try:
                            self.execute(parser_object.command[1], players)
                            break
                        except InputError:
                            print "INPUT ERROR BITCHES"

        else:
            print "Mr. Input() is confused :(" 

    def execute(self, string, players, parameters=False):
        if string == "summon":
            players[0].summon()
        elif string == "battle":
            players[0].battle()
        elif string == "spell":
            spell_command_type = self.input_get("Set or activate spell? ")
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
        else:
            return InputError