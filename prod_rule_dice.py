#input  =  [[1, 1, 6, 6, 8, 8], [2, 2, 4, 4, 9, 9], [3, 3, 5, 5, 7, 7]]
input = [[1, 1, 2, 4, 5, 7], [1, 2, 2, 3, 4, 7], [1, 2, 3, 4, 5, 6]]
#input = [[3, 3, 3, 3, 3, 3], [6, 6, 2, 2, 2, 2], [4, 4, 4, 4, 0, 0], [5, 5, 5, 1, 1, 1]]
from itertools import combinations

count = 0
dicewins = []
dicepair = []
dicescores = []
scorelist = []
countsmax = None
idxmaxdice = None
for i in combinations(input, 2):
    dice1 = i[0]
    dice2 = i[1]
    dicepair = [dice1,dice2]
    #print(dice1,"/",dice2)
    dice1_wins, dice2_wins = 0, 0
    for j in dice1:
        for k in dice2:
            if j > k:
                dice1_wins = dice1_wins + 1
            elif j < k:
                dice2_wins = dice2_wins + 1
    count = count + 1
    dicescores = [dice1_wins,dice2_wins]
    maxdicescore = max(dice1_wins,dice2_wins)
    scorelist.append(maxdicescore)
    idxmaxdicescore = dicescores.index(maxdicescore)
    maxdice = dicepair[idxmaxdicescore]
    idxmaxdice = input.index(maxdice)
    countsmax = scorelist.count(maxdicescore)

    #print(count, ",",dicepair,",",dicescores,",", maxdicescore,",",idxmaxdicescore,",", i,",", maxdice,",",idxmaxdice,",",scorelist,",", countsmax)
if countsmax > 1:
    print("-1")
else:
    print (idxmaxdice)
