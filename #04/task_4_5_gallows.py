'''
    The basic premise of the game Gallows is to follow two rules:

    First character of next word must match last character of previous word.
    The word must not have already been said.
    Below is an example of a Gallows game:

    ['word', 'dowry', 'yodel', 'leader', 'righteous', 'serpent']  #valid!

    ['motive', 'beach']  # invalid! - beach should start with "e"

    ['hive', 'eh', 'hive']  # invalid! - "hive" has already been said
    Write a Gallows class that has two instance variables:

    words: a list of words already said.
    game_over: a boolean that is true if the game is over.
    and two instance methods:

    play: a method that takes in a word as an argument and checks if it is valid
    (the word should follow rules #1 and #2 above).

    If it is valid, it adds the word to the words list, and returns the words list.
    If it is invalid (either rule is broken), it returns "game over" and sets the game_over
    boolean to true.
    restart: a method that sets the words list to an empty one [] and sets the game_over boolean
    to false. It should return "game restarted".
'''

# VAR1
class Gallows:

    words = []
    game_over = False

    def __init__(self, words=words, game_over=game_over):
        self.words = words
        self.game_over = game_over

    def play(self, words):

        if len(self.words) > 0:
            # слово збігається по буквах
            condition1 = words[0] == self.words[-1][-1]
            # список немаєє однакових слів
            condition2 = len([words for i in self.words if words == i]) == 0
            #print(condition1, condition2)
        else:
            pass

        if len(self.words) > 0 and condition1 and condition2:
            self.words.append(words)
            return self.words
        elif len(self.words) == 0:
            self.words.append(words)
            return self.words
        else:
            self.game_over = True
            print('game over')
            return self.game_over

    def restart(self):
        self.game_over = False
        self.words.clear()
        print('game restarted')
        return self.game_over, self.words


my_gallows = Gallows()


# SET Soft Serve
## block1 - independent

my_gallows.play('apple')  # ok
print(my_gallows.words)
my_gallows.play('ear')  # ok
print(my_gallows.words)
my_gallows.play('rhino')  # ok
print(my_gallows.words)
# # Words should be accessible.
# game_over - still False, as all words where added in correct order
print(my_gallows.game_over)
# now we're gonna restartthe game:
# it'll pussh game_over to true

my_gallows.restart()
# Words list should be set back to empty.
# print(my_gallows.words) # ok
# ok ### game_over - should be setup to False and list will be clered
print(my_gallows.game_over)
# ok game_over setup to False and the list of items was cleared to an empty one
print(my_gallows.words)


##block2 - independent
my_gallows.play('hostess')  # ok
print(my_gallows.words)
my_gallows.play('stash')  # ok
print(my_gallows.words)
# ok - hostes will not be added to the words as it is incompatible with rules
my_gallows.play('hostess')
print(my_gallows.words)


# block3 - not independent
####
my_gallows.restart()  # SHOULD BE RESTARTED OTHERWISE APLLE WILL NOT GET TO WORDS  # (list is not empty, words should be accessible wfter game over)
####
# # # Words cannot have already been said.
my_gallows.play('apple')  # NOT OK ## ERROR
my_gallows.play('ear')  # NOT OK ## ERROR
my_gallows.play('rhino')  # NOT OK ## ERROR
print(my_gallows.words)  # NOT OK ## ERROR

# block4 - not independent
# Corn does not start with an "o".
my_gallows.play('corn')
print(my_gallows.words)  # OK
my_gallows.restart()
my_gallows.words
print(my_gallows.words)


# VAR2 -DOES NOT COMPLY TO THE TASK, AS IT
'''
    DOES NOT COMPLY TO THE TASK, AS IT ADDS EVERY WORD TO THE LIST
    AND THEN REMOVE IT WHEN A WORD DOESN'T GO THROUGH THE FILTER

    filter is a liitle bit sophisticated, however tried to ocncentrate 
    on satysfying conditions
'''


class Gallows:

    words = []
    game_over = False

    def __init__(self, words=words, game_over=game_over):
        self.words = words
        self.game_over = game_over

    def play(self, words):
        self.words.extend([words])

        # condition1 = comparing equal words
        check_list = [False for i in range(
            (len(self.words) - len(set(self.words))))]

        # condition2 = comparing first and last digits
        compare_zip = list(zip([i[-1] for i in [i[-1] for i in self.words[:-1]]], [
                           i[0] for i in [i[0] for i in self.words[1:]]]))
        check_list.extend([x == y for x, y in compare_zip if x != y])

        if check_list.count(False) < 1:
            return self.words

        else:
            self.game_over = True
            self.words = self.words[:-1]
            print('game over')
            # return Gallows(self.game_over)
            return self.words

    def restart(self):
        self.game_over = False
        self.words = []
        print('game restarted')
        return self.words


my_gallows = Gallows()

# SET Soft Serve
# block1
my_gallows.play('apple')  # ok --> ['apple']
print(my_gallows.words)
my_gallows.play('ear')  # ok --> ['apple', 'ear']
print(my_gallows.words)
my_gallows.play('rhino')  # ok --> ['apple', 'ear', 'rhino']
print(my_gallows.words)  # ok --> ['apple', 'ear', 'rhino']
# # # Words should be accessible.
# game_over - still False, as all words where added in correct order
print(my_gallows.game_over)
# ### now we're gonna restartthe game:
# ## it'll pussh game_over to true

my_gallows.restart()
# # Words list should be set back to empty.
print(my_gallows.words)  # ok ---> []
print(my_gallows.game_over)  # ok --->

# block2
my_gallows.play('hostess')  # ok
my_gallows.play('stash')  # ok
my_gallows.play('hostess')  # ok --> game over
print(my_gallows.words)  # --> ['hostess', 'stash']
print(my_gallows.game_over)  # ok ---> turned to true


# #my_gallows.restart() #should be restarted # otherwise error
# # # Words cannot have already been said.
# NOT OK --> game_over ## does no comply to condition2
my_gallows.play('apple')
my_gallows.play('ear')  # NOT OK --> game_over ## does no comply to condition2
# NOT OK --> game_over ## does no comply to condition2
my_gallows.play('rhino')
# NOT OK ## ERROR --> the same list  ['hostess', 'stash']
print(my_gallows.words)

# # # Corn does not start with an "o".
my_gallows.play('corn')  # OK --> game_over
print(my_gallows.words)  # NOT OK -->['apple', 'ear', 'rhino']
my_gallows.restart()  # OK --> game restarted
print(my_gallows.words)  # OK ---> []
