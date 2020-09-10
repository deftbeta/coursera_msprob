def count_wins(dice1, dice2):
    assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins, dice2_wins = 0, 0

    i = 0
    k = 0

    for i in dice1:
      for k in dice2:
        if i > k:
            dice1_wins = dice1_wins + 1
        elif i < k:
            dice2_wins = dice2_wins + 1
        k = k + 1
      i = i + 1
    return (dice1_wins, dice2_wins)
dice1=[1, 2, 3, 4, 5, 6]
dice2=[1, 2, 3, 4, 5, 6]

count_wins(dice1, dice2)
