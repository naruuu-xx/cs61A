
from dice import six_sided, four_sided, make_test_dice
from hog import always_roll, both, more_boar, next_player, roll_dice, silence, take_turn
import hog
GOAL_SCORE = 100
# def roll_dice(num_rolls, dice=six_sided):
#     """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
#     the outcomes unless any of the outcomes is 1. In that case, return 1.

#     num_rolls:  The number of dice rolls that will be made.
#     dice:       A function that simulates a single dice roll outcome.
#     """
#     # These assert statements ensure that num_rolls is a positive integer.
#     assert type(num_rolls) == int, 'num_rolls must be an integer.'
#     assert num_rolls > 0, 'Must roll at least once.'
#     # BEGIN PROBLEM 1
#     "*** YOUR CODE HERE ***"
#     cnt = 0
#     sum = 0
#     arr = []
#     while cnt < num_rolls:
#         arr.append(dice())  
#         cnt += 1
#         sum += arr[len(arr)-1] if 1 != arr[len(arr)-1] else 0
#         if 1 in arr :
#             continue
#     return sum if 1 not in arr else 1

# print(roll_dice(2, make_test_dice(4, 6, 1)))
# print(roll_dice(3, make_test_dice(4, 6, 1)))
# print(roll_dice(4, make_test_dice(2, 2, 3)))
# print(roll_dice(4, make_test_dice(1, 2, 3)))
# counted_dice = make_test_dice(4, 1, 2, 6)
# print(roll_dice(3, counted_dice))
# print(roll_dice(1, counted_dice))
# print(roll_dice(9, make_test_dice(6)))
# print(roll_dice(7, make_test_dice(2, 2, 2, 2, 2, 2, 1)))

# def piggy_points(score):
#     """Return the points scored from rolling 0 dice.

#     score:  The opponent's current score.
#     """
#     # BEGIN PROBLEM 2
#     "*** YOUR CODE HERE ***"
#     squar_score = score * score
#     min_dig = squar_score
#     if squar_score == 0 :
#         return 3
#     while squar_score != 0 :
#         dig = squar_score % 10
#         squar_score = squar_score // 10
#         min_dig = min(dig, min_dig)
#     return min_dig + 3

    # END PROBLEM 2
# print(piggy_points(4))
# print(piggy_points(10))
# print(piggy_points(94))
# print(piggy_points(0))
# print(piggy_points(24))

# def take_turn(num_rolls, opponent_score, dice=six_sided, goal=GOAL_SCORE):
#     """Simulate a turn rolling NUM_ROLLS dice, which may be 0 in the case
#     of a player using Piggy Points.
#     Return the points scored for the turn by the current player.

#     num_rolls:       The number of dice rolls that will be made.
#     opponent_score:  The total score of the opponent.
#     dice:            A function that simulates a single dice roll outcome.
#     goal:            The goal score of the game.
#     """
#     # Leave these assert statements here; they help check for errors.
#     assert type(num_rolls) == int, 'num_rolls must be an integer.'
#     assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
#     assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
#     assert opponent_score < goal, 'The game should be over.'
#     # BEGIN PROBLEM 3
#     "*** YOUR CODE HERE ***"
#     if num_rolls == 0:
#         return piggy_points(opponent_score) 
#     else:
#         my_score = roll_dice(num_rolls, dice)
#         return my_score if my_score > opponent_score else opponent_score

#     # END PROBLEM 3
# print(take_turn(2, 0, make_test_dice(4, 5, 1)))
# print(take_turn(3, 0, make_test_dice(4, 6, 1)))
# print(take_turn(0, 2))
# print(take_turn(0, 0))


# def more_boar(player_score, opponent_score):
#     """Return whether the player gets an extra turn.

#     player_score:   The total score of the current player.
#     opponent_score: The total score of the other player.

#     >>> more_boar(21, 43)
#     True
#     >>> more_boar(22, 43)
#     True
#     >>> more_boar(43, 21)
#     False
#     >>> more_boar(12, 12)
#     False
#     >>> more_boar(7, 8)
#     False
#     """
#     # BEGIN PROBLEM 4
#     "*** YOUR CODE HERE ***"
#     def find_digit(score):
#         arr = []
#         if score < 10:
#             arr.append(0)
#             arr.append(score)
#         else:
#             arr.append(int(str(score)[0]))
#             arr.append(int(str(score)[1]))
#         print(arr)
#         return arr
#     play_dight = find_digit(player_score)
#     opponent_dight = find_digit(opponent_score)
#     for i in range(len(play_dight)):
#         if play_dight[i] >= opponent_dight[i]:
#             return False
#     return True

# print(more_boar(21, 43))
# print(more_boar(22, 43))
# print(more_boar(43, 21))
# print(more_boar(12, 12))
# print(more_boar(6, 18))
# print(more_boar(21, 43))
# print(more_boar(91, 106))
    # END PROBLEM 4
def play(strategy0, strategy1, score0=0, score1=0, dice=six_sided,
         goal=GOAL_SCORE, say=silence):
    """Simulate a game and return the final scores of both players, with Player
    0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments (the
    current player's score, and the opponent's score), and returns a number of
    dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first.
    strategy1:  The strategy function for Player 1, who plays second.
    score0:     Starting score for Player 0
    score1:     Starting score for Player 1
    dice:       A function of zero arguments that simulates a dice roll.
    goal:       The game ends and someone wins when this score is reached.
    say:        The commentary function to call at the end of the first turn.
    """
    who = 0  # Who is about to take a turn, 0 (first) or 1 (second)
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    while score0 < goal and score1 < goal:
        if who == 0:
            score0 += take_turn(strategy0(score0,score1), score1, dice, goal)
            if not more_boar(score0, score1):
                who = next_player(who)
        else:
            score1 += take_turn(strategy1(score1,score0), score0, dice, goal)
            if not more_boar(score1, score0):
                who = next_player(who)

# always_three = hog.make_test_dice(3)
# always = hog.always_roll
# print(hog.play(always(6), always(2), goal=25, dice=always_three))

def total(s0, s1):
    print(s0 + s1)
    return echo

def echo(s0, s1):
    print(s0, s1)
    return total
# strat0 = lambda score, opponent: 1 - opponent // 10
# strat1 = always_roll(3)
# print(hog.play(strat0, strat1, dice=make_test_dice(4, 2, 6), goal=15, say=echo))
# print(hog.play(always_roll(1), always_roll(1), dice=make_test_dice(8, 2), goal=20, say=echo))

# def echo_0(s0, s1):
#     print('*', s0)
#     return echo_0
# def echo_1(s0, s1):
#     print('**', s1)
#     return echo_1
# print(hog.play(always_roll(1), always_roll(1), dice=make_test_dice(2), goal=3, say=both(echo_0, echo_1)))
# def announce_highest(who, last_score=0, running_high=0):
#     """Return a commentary function that announces when WHO's score
#     increases by more than ever before in the game.
   
#     NOTE: the following game is not possible under the rules, it's just
#     an example for the sake of the doctest


    # >>> f0 = announce_highest(1) # Only announce Player 1 score gains
    # >>> f1 = f0(12, 0)
    # >>> f2 = f1(12, 9)
    # Player 1 has reached a new maximum point gain. 9 point(s)!
    # >>> f3 = f2(20, 9)
    # >>> f4 = f3(20, 30)
    # Player 1 has reached a new maximum point gain. 21 point(s)!
    # >>> f5 = f4(20, 47) # Player 1 gets 17 points; not enough for a new high
    # >>> f6 = f5(21, 47)
    # >>> f7 = f6(21, 77)
    # Player 1 has reached a new maximum point gain. 30 point(s)!
    # """
    # assert who == 0 or who == 1, 'The who argument should indicate a player.'
    # # BEGIN PROBLEM 7
    # "*** YOUR CODE HERE ***"
    # def say(score0, score1):
    #     score = score0 if who == 0 else score1
    #     high_number = running_high
    #     if score > last_score:
    #         temp = score - last_score
    #         if temp > high_number:
    #             high_number = temp
    #             print ('Player',who,'has reached a new maximum point gain.', high_number, 'point(s)!')
    #     return announce_highest(who, score, high_number)
    # return say
    # # END PROBLEM 7

def make_averaged(original_function, trials_count=1000):
    """Return a function that returns the average value of ORIGINAL_FUNCTION
    when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(4, 2, 5, 1)
    >>> averaged_dice = make_averaged(roll_dice, 1000)
    >>> averaged_dice(1, dice)
    3.0
    """
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    def f(*args):
        ans = 0
        for i in range (trials_count):
            ans += original_function(*args)
        return ans / trials_count
    return f


# from hog import *
# dice = make_test_dice(3, 1, 5, 6)
# averaged_dice = make_averaged(dice, 1000)
# print(averaged_dice())>>> dice = make_test_dice(3, 1, 5, 6)
# averaged_roll_dice = make_averaged(roll_dice, 1000)
#  # Enter a float (e.g. 1.0) instead of an integer
# averaged_roll_dice(2, dice)
from hog import *
dice = make_test_dice(3, 1, 5, 6)
averaged_roll_dice = make_averaged(roll_dice, 1000)
print(averaged_roll_dice(2, dice))
