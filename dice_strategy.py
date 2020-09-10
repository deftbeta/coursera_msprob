from itertools import combinations

#input = [[1, 1, 4, 6, 7, 8], [2, 2, 2, 6, 7, 7], [3, 3, 3, 5, 5, 8]]
#input = [[4, 4, 4, 4, 0, 0], [7, 7, 3, 3, 3, 3], [6, 6, 2, 2, 2, 2], [5, 5, 5, 1, 1, 1]]
#input = [[1, 1, 6, 6, 8, 8], [2, 2, 4, 4, 9, 9], [3, 3, 5, 5, 7, 7]]
#input = [[1, 2, 3, 4, 5, 6],[1, 1, 2, 4, 5, 7],[1, 2, 2, 3, 4, 7]]
#input = [[1, 1, 2, 4, 5, 7], [1, 2, 2, 3, 4, 7], [1, 2, 3, 4, 5, 6]]
input = [[4, 4, 4, 4, 0, 0], [3, 3, 3, 3, 3, 3], [6, 6, 2, 2, 2, 2], [5, 5, 5, 1, 1, 1]]

print ("input: ", input,"len: ", len(input))

def compute_strategy(dices):
    assert all(len(dice) == 6 for dice in dices)
    count = 0
    countsmax = 0
    count2 = 0
    idxmaxdice = 0
    idxmaxdice = 0
    dicepair = []
    diceidxpair = []
    dicescores = []
    scorelist = []
    listoloosers = []
    listowinners = []
    strategy = dict()
    strategyf = dict()
    strategyt = dict()

    for i in combinations(dices, 2):
        dice1 = i[0]
        dice2 = i[1]
        dicepair = [dice1,dice2]
        diceidxpair = [dices.index(dice1),dices.index(dice2)]
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
        mindicescore = min(dice1_wins,dice2_wins)
        scorelist.append(maxdicescore)
        idxmaxdicescore = dicescores.index(maxdicescore)
        idxmindicescore = dicescores.index(mindicescore)
        maxdice = dicepair[idxmaxdicescore]
        mindice = dicepair[idxmindicescore]
        idxmaxdice = dices.index(maxdice)
        idxmindice = dices.index(mindice)
        listoloosers.append(idxmindice)
        listowinners.append(idxmaxdice)
        mostwindice = max(listowinners,key=listowinners.count)
        count1 = listowinners.count(mostwindice)
        count2 = listowinners.count(idxmaxdice)
        count3 = scorelist.count(maxdicescore)
        #if dice1_wins == dice2_wins:
        #    count2 = listowinners.count(mostwindice)
        #    countsmax = count2
        #else:
        #    count2 = listowinners.count(idxmaxdice)
        #    countsmax = scorelist.count(maxdicescore)
        for n in listowinners:
            if n not in listoloosers:
                selectdice = n

        print(count,",",diceidxpair,",",dicescores,",", maxdicescore,",",idxmindice,"-->",idxmaxdice,",",listowinners,",", scorelist,",",mostwindice,",",count1,",",count2,",",count3)

        if count1 == len(dices)-1:
            strategyt["choose_first"] = True
            strategyt["first_dice"] = selectdice
            strategy = strategyt

        elif count1 < len(dices)-1:
            strategyf["choose_first"] = False
            o = 0
            while o < 1+(len(dices)*(len(dices)-1))/2:
                strategyf[idxmindice] = idxmaxdice
                strategyf.update()
                o = o + 1
            strategy = strategyf


    print(strategy)
    #return (strategy)

compute_strategy(input)
