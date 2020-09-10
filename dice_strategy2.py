def compute_strategy(dices):
    assert all(len(dice) == 6 for dice in dices)

    strategy = dict()
    strategy["choose_first"] = True
    strategy["first_dice"] = 0
    for i in range(len(dices)):
        strategy[i] = (i + 1) % len(dices)

    dice_1 = 0
    dice_2 = 0
    winner = []
    loser = []
    winner_return = -1
        for i in range(len(dices)):
            for j in range(len(dices)):
                if i >= j:
                    pass
                else:

                    for ele_1 in dices[i]:
                        for ele_2 in dices[j]:
                            if ele_1 > ele_2:
                                dice_1 += 1
                            elif ele_2 > ele_1:
                                dice_2 += 1
                            else:
                                pass
                    if dice_1 > dice_2:
                        winner.append(i)
                        loser.append(j)
                    elif dice_2 > dice_1:
                        winner.append(j)
                        loser.append(i)
                        else:
                            pass
                        dice_1 = 0
                        dice_2 = 0
            if len(winner) == 1 and winner[0] != '':
                winner_return = winner[0]
            elif len(winner) > 1:
                for i in range(len(winner)):
                    if loser.count(winner[i]) != 0:
                        i += 1
                    elif loser.count(winner[i]) == 0:
                        winner_return = winner[i]
                        i += 1
            else:
                winner_return == -1

            if winner_return != -1:
                strategy.clear()
                strategy["choose_first"] = True
                strategy["first_dice"] = winner_return
                return strategy
            elif winner_return == -1:
                strategy.clear()
                strategy["choose_first"] = False
                for j in range(len(dices)):
                      strategy.update({loser[j]: winner[j]})


        return strategy
