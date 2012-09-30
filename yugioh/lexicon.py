def scan(word):
    m_list = []
    leximes = {'north': 'direction', 'south': 'direction', 
                'east': 'direction', 'west': 'direction', 
                'down': 'direction', 'up': 'direction', 
                'left': 'direction', 'right': 'direction', 'back':'direction', 
                'go': 'verb', 'stop': 'verb', 'kill': 'verb', 'eat': 'verb',
                'the': 'stop', 'in': 'stop', 'of': 'stop', 
                'from': 'stop', 'at': 'stop', 'it': 'stop',
                'door': 'noun', 'bear': 'noun', 'princess': 'noun', 'cabinet': 'noun'
                }
    words = word.split()
    for word in words:
        temp = convert_number(word)
        if isinstance(temp, int):
            num_tuple = ('number', temp)
            m_list.append(num_tuple)
        else:
            word_type = leximes.get(word, 'error')
            m_list.append((word_type, word))
    return m_list

def convert_number(string):
    try:
        return int(string)
    except ValueError:
        return None 
        
class ParserError(Exception):
    pass


class Sentence(object):

    def __init__(self, subject, verb, object):
        # remember we take ('noun','princess') tuples and convert them
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = object[1]


def peek(word_list):
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None


def match(word_list, expecting):
    if word_list:
        word = word_list.pop(0)

        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None


def skip(word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list, word_type)


def parse_verb(word_list):
    skip(word_list, 'stop')

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next.")


def parse_object(word_list):
    skip(word_list, 'stop')
    next = peek(word_list)

    if next == 'noun':
        return match(word_list, 'noun')
    if next == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or direction next.")


def parse_subject(word_list, subj):
    verb = parse_verb(word_list)
    obj = parse_object(word_list)

    return Sentence(subj, verb, obj)


def parse_sentence(word_list):
    skip(word_list, 'stop')

    start = peek(word_list)

    if start == 'noun':
        subj = match(word_list, 'noun')
        return parse_subject(word_list, subj)
    elif start == 'verb':
        # assume the subject is the player then
        return parse_subject(word_list, ('noun', 'player'))
    else:
        raise ParserError("Must start with subject, object, or verb not: %s" % start)

game_running = True
while game_running:
    parse_sentence(scan(raw_input("> ")))
    
