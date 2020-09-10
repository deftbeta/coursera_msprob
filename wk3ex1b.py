entry = input('Enter a number between 24 and 1000:')
amount = int(entry)
def change(amount):
    if amount == 24:
        return [5, 5, 7, 7]
    elif amount == 25:
        return [5, 5, 5, 5, 5]
    elif amount == 26:
        return [7, 7, 7, 5]
    elif amount == 27:
        return [7, 5, 5, 5, 5]
    elif amount == 28:
        return [7, 7, 7, 7]
    elif amount % 5 == 0:
        iterations = amount / 5
        i = 0
        amount = [5]
        addtolist = [5]
        while i < iterations - 1:
            amount = amount + addtolist
            i += 1
        return amount
    elif amount % 7 == 0:
        iterations = amount / 7
        i = 0
        amount = [7]
        addtolist = [7]
        while i < iterations -1 :
            amount = amount + addtolist
            i += 1
        return amount
    elif (amount - 7) % 5 == 0:
        iterations = (amount - 7)/5
        i = 0
        amount = [7]
        addtolist = [5]
        while i < iterations:
            amount = amount + addtolist
            i += 1
        return amount
    elif (amount - 14) % 5 == 0:
        iterations = (amount - 14)/5
        i = 0
        amount = [7, 7]
        addtolist = [5]
        while i < iterations:
            amount = amount + addtolist
            i += 1
        return amount
    elif (amount - 21) % 5 == 0:
        iterations = (amount - 21)/5
        i = 0
        amount = [7, 7, 7]
        addtolist = [5]
        while i < iterations:
            amount = amount + addtolist
            i += 1
        return amount
    elif (amount - 28) % 5 == 0:
        iterations = (amount - 28)/5
        i = 0
        amount = [7, 7, 7, 7]
        addtolist = [5]
        while i < iterations:
            amount = amount + addtolist
            i += 1
        return amount
print (change(amount))
