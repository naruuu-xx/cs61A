# hog
主要用于记录项目阅读和编写过程中的一些问题和解法。

我的代码不是唯一解，如果有更好的可以issue提出。
笔者之前用 java 比较多，因此代码相对网络上其他人的要繁琐一些。
再者这个 project 比较微妙的地方就在于：
有时候可能你前面写的方法测试用例能全都pass，但是后续你在别的方法内调用该方法时，可能会出现一定的bug，因此代码需要经常修改。最开始想到的解决问题的方法不一定是最优解。代码是需要不断进行优化的。

同时请允许自己犯错，学习就是不断纠错并进行修改的过程。


--------------------------------
## 规则
关于规则，笔者在此不再多说，因为 CS61A 官网其实做出了非常全面的解释，笔者很难做出不繁琐且简单的翻译，因此我将采用：在编写代码的过程中不断重复强调我们所用到或需要的规则以此让自己以及阅读本文的读者深入了解该 project 的内在。

## problem 0

该问题主要用于让开发者了解项目的大概，不需要进行任何代码的编写。
思路其实非常清晰，既然我们要摇骰子，那么这意味着我们应该先行对骰子模块（dice.py）进行了解。
至少要清楚 make_test_dice() 的用法。

## problem 1

初次引入骰子游戏规则 Sow Sad 。
该规则的定义：
如果任何一个骰子投出 1 ，那么当前玩家的分数将直接变为 1.其余情况下玩家分数为骰子点数累加和。
> If any of the dice outcomes is a 1, the current player's score for the turn is 1.

代码：
```python
def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.

    num_rolls:  The number of dice rolls that will be made.
    dice:       A function that simulates a single dice roll outcome.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    """ 
    先不看代码首先思考一下，投骰子过程中我们需要考虑：
    投几次，投的总点数是多少。其次我们再考虑额外规则：
    当我在投骰子过程中投出一个1，本局我将得分1
    否则我只需要将骰子的点数叠加起来就可以了。
    这里我引入一个列表[]，用来存放骰子每次的点数，
    当点数列表中存在1时，我将返回1.否则直接将列表内的点数进行叠加即可。
    """
    cnt = 0
    sum = 0
    arr = []
    while cnt < num_rolls:
        arr.append(dice())  
        cnt += 1
        sum += arr[len(arr)-1] if 1 != arr[len(arr)-1] else 0
        if 1 in arr :
            continue
    return sum if 1 not in arr else 1 
    # END PROBLEM 1
```

## problem 2
引入 Piggy Points 规则。
规则介绍：
掷零骰子的玩家本局得 k+3 分，其中 k 是对手得分各个位数中最小值的平方数字。
本题有额外要求不使用 for 循环以及列表[] 。

代码：
```python
def piggy_points(score):
    """Return the points scored from rolling 0 dice.

    score:  The opponent's current score.
    """
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    '''
    思路非常简单，只需要求解平方score的每一位数字，
    然后选出其中最小的加上3即为最终答案
    '''
    squar_score = score * score
    min_dig = squar_score
    if squar_score == 0 :
        return 3
    while squar_score != 0 :
        dig = squar_score % 10
        squar_score = squar_score // 10
        min_dig = min(dig, min_dig)
    return min_dig + 3
    # END PROBLEM 2
```


