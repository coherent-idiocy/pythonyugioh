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