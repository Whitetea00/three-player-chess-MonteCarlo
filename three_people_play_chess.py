# coding:utf-8 

# ------------------------------------------------------------------
# FileName:         three_people_play_chess.py
# Author:           whittea00
# Version:          V 0.9beta
# Created:          2021-11-19
# Description:      Monte Carlo method simulates chess
# License:          MIT
# History:
#          2021-11-15    whitetea00  :Create the file
#          2021-11-25    whitetea00  :add notes
# ------------------------------------------------------------------

# 蒙特卡罗方法模拟下棋，比赛策略使用递归的方式来选出胜者
# Monte Carlo method simulates chess, the game strategy uses recursion to select the winner.
import random

# 初始化数据
# Initialization data
playA = [0, 'playerA']
playB = [0, 'playerB']
playC = [0, 'playerC']
aWinTimes = 0
bWinTimes = 0
cWinTimes = 0
# times 为比赛的场次
# times is the number of matches
times = 100000

# chess函数：计算每局下棋的获胜情况。
# 获胜的玩家派在第一位并记1个点数，输的玩家排在第二位且点数清零。
# chess function: calculates the winning situation of each chess game.
# The winning player is placed in the first place and counts 1 point, and the losing player is placed in second place and the points are cleared.
def chess(ai, bi):
    player1 = random.random()
    player2 = random.random()
    if player1 > player2:
        ai[0] += 1
        bi[0] = 0
        return ai, bi
    elif player1 < player2:
        bi[0] += 1
        ai[0] = 0
        return bi, ai
    else:
        return chess(ai,bi)

# games函数：如果出现连续赢两次的情况，则返回游戏最终胜者。
# 如没有，则新的胜者与上一局输者重新下棋，直至出现连续赢两次的玩家。
# games function: If there are two consecutive wins, the final winner of the game is returned.
# If not, the new winner and the previous loser will replay chess until there is a player who has won twice in a row.
def games(aii, bii, cii):
    win, lose = chess(aii, bii)
    if win[0] == 2:
        return win;
    else:
        return games (win, cii, lose)

for i in range(times):
    lostwin = games(playA, playB, playC)

    playA = [0, 'playerA']
    playB = [0, 'playerB']
    playC = [0, 'playerC']
    name = lostwin[1]
    if name == 'playerA':
        aWinTimes += 1
    elif name == 'playerB':
        bWinTimes += 1
    elif name == 'playerC':
        cWinTimes += 1
    else:
        print('error')

print('ABC三个玩家，其中A和B先下，')
print('共进行了{}次循环'.format(times))
print('玩家A获胜的概率为：{}'.format(aWinTimes/times))
print('玩家B获胜的概率为：{}'.format(bWinTimes/times))
print('玩家C获胜的概率为：{}'.format(cWinTimes/times))
print('_____________________________')
print('ABC three players, A and B play first,')
print('A total of {} cycles.'.format(times))
print('The probability of player A winning is:{}'.format(aWinTimes/times))
print('The probability of player B winning is:{}'.format(bWinTimes/times))
print('The probability of player C winning is:{}'.format(cWinTimes/times))


