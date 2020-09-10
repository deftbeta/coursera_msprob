from itertools import combinations
#input  =  [[1, 1, 6, 6, 8, 8], [2, 2, 4, 4, 9, 9], [3, 3, 5, 5, 7, 7]]
#input = [[1, 1, 2, 4, 5, 7], [1, 2, 2, 3, 4, 7], [1, 2, 3, 4, 5, 6]]
#input = [[3, 3, 3, 3, 3, 3], [6, 6, 2, 2, 2, 2], [4, 4, 4, 4, 0, 0], [5, 5, 5, 1, 1, 1]]
input = [[1, 1, 4, 6, 7, 8], [2, 2, 2, 6, 7, 7], [3, 3, 3, 5, 5, 8]]
#input = [[4, 4, 4, 4, 0, 0], [7, 7, 3, 3, 3, 3], [6, 6, 2, 2, 2, 2], [5, 5, 5, 1, 1, 1]]

print ("input: ", input,"len: ", len(input))
def find_the_best_dice(dices):
    assert all(len(dice) == 6 for dice in dices)

    count = 0

    dicepair = []
    diceidxpair = []
    selectpairs = dict()
    dicescores = []
    scorelist = []
    listoloosers = []
    listowinners = []
    countsmax = 0
    idxmaxdice = 0
    idxmaxdice = 0
    choose = 0
    select = 0

    for i in combinations(dices, 2):
        dice1 = i[0]
        dice2 = i[1]
        dicepair = [dice1,dice2]
        diceidxpair = [dices.index(dice1),dices.index(dice2)]
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
        mindicescore = min(dice1_wins,dice2_wins)
        scorelist.append(maxdicescore)
        idxmaxdicescore = dicescores.index(maxdicescore)
        idxmindicescore = dicescores.index(mindicescore)
        maxdice = dicepair[idxmaxdicescore]
        mindice = dicepair[idxmindicescore]
        idxmaxdice = input.index(maxdice)
        idxmindice = input.index(mindice)
        countsmax = scorelist.count(maxdicescore)
        listoloosers.append(idxmindice)
        listowinners.append(idxmaxdice)
        #print(listoloosers,",",listowinners)
        print(count,",",dicepair,",",diceidxpair,",",dicescores,",", maxdicescore,",",idxmaxdicescore,",", i,",", maxdice,",",idxmindice,"-->",idxmaxdice,",",scorelist,",", countsmax,",",listoloosers)

    if countsmax > 1:
        choose = True
        for l in listoloosers:
            for m in listowinners:
                #print(l,",",m)
                if m not in listoloosers:
                    #print("-->",m)
                    select = m
        print("choose first: ",choose," first_dice: ", select)

    else:
        choose = False
        for l in listoloosers:
            for m in listowinners:
                selectpairs[l] = m



        print ("choose first: ",choose,",",select)

find_the_best_dice(input)
#def count_wins(dice1, dice2):
#    assert len(dice1) == 6 and len(dice2) == 6
#    dice1_wins, dice2_wins = 0, 0
#    for i in dice1:
#      for j in dice2:
#        if i > j:
#            dice1_wins = dice1_wins + 1
#        elif i < j:
#            dice2_wins = dice2_wins + 1
#    print (dice1_wins, dice2_wins)
