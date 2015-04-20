from ps3a import *
import time
from perm import *


#
#
# Problem #6A: Computer chooses a word
#
#
def comp_choose_word(hand, word_list):
    """
	Given a hand and a word_dict, find the word that gives the maximum value score, and return it.
   	This word should be calculated by considering all possible permutations of lengths 1 to HAND_SIZE.

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    best_word = None
    best_score = 0
    for length in range(1, calculate_handlen(hand)+1):
        for perm in get_perms(hand, length):
            if perm in word_list:
                score = get_word_score(perm, HAND_SIZE)
                if score > best_score:
                    best_word = perm
                    best_score = score
    return best_word

#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed, 
       the remaining letters in the hand are displayed, and the computer 
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """
    total_score = 0
    display_hand(hand)
    word = comp_choose_word(hand, word_list)
    while word != None:
        hand = update_hand(hand, word)
        word_score = get_word_score(word, HAND_SIZE)
        total_score += word_score 
        print word, "earned", word_score, "points. Total:", total_score, "points"
        print
        display_hand(hand)
        word = comp_choose_word(hand, word_list)
    print "Total score:", total_score, "points."
        
    
#
# Problem #6C: Playing a game
#
#
def play_game(word_list):
    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    game_resp = raw_input("New/Repeat/Exit? ")
    hand = deal_hand(HAND_SIZE)
    while game_resp != 'e':
        if game_resp == "n":
            hand = deal_hand(HAND_SIZE)
            player_resp = raw_input("User/Computer? ")
            if player_resp == "u":
                play_hand(hand, word_list)
            else:
                comp_play_hand(hand, word_list)
        elif game_resp == "r":
            player_resp = raw_input("User/Computer? ")
            if player_resp == "u":
                play_hand(hand, word_list)
            else:
                comp_play_hand(hand, word_list)
        
        game_resp = raw_input("New/Repeat/Exit? ") 
        print
        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)

    
