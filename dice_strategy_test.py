input = [[1, 1, 4, 6, 7, 8], [2, 2, 2, 6, 7, 7], [3, 3, 3, 5, 5, 8]]
#input = [[4, 4, 4, 4, 0, 0], [7, 7, 3, 3, 3, 3], [6, 6, 2, 2, 2, 2], [5, 5, 5, 1, 1, 1]]

def compute_strategy(dices):
    assert all(len(dice) == 6 for dice in dices)

    strategy = dict()
    strategy["choose_first"] = True
    strategy["first_dice"] = 0
    for i in range(len(dices)):
        strategy[i] = (i + 1) % len(dices)



    print (strategy)

compute_strategy(input)
