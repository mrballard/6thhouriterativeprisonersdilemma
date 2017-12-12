####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Blue Team' # Only 10 chars displayed.
strategy_name = 'on a limb'
strategy_description = '''
on the first five rounds I collude, after that, it is all randomly picked between collude and betray.
'''
 
import random
       
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    cblist = ['c', 'b']
    if len(their_history) <= 5:
        if 'b' in their_history[-1]: # If the other player has betrayed in past 2 rounds
            return 'b'
        else:
            return 'c'
    else:
        finalMove = random.choice(cblist)
        return finalMove

    