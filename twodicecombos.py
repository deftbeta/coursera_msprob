def count_wins(dice1, dice2):
    assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins, dice2_wins = 0, 0

    for i in dice1:
      for k in dice2:
        if i > k:
            dice1_wins = dice1_wins + 1
        elif i < k:
            dice2_wins = dice2_wins + 1

    print (dice1_wins, dice2_wins)

dice1=[3, 3, 3, 3, 3, 3]
dice2=[6, 6, 2, 2, 2, 2]

count_wins(dice1, dice2)
