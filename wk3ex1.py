
#initialize amount

#request entry of amount
#i = 0
#charlist = list()
amount = input('Enter a number between 24 and 1000:')
def change(amount):
    intamount = int(amount)
    if intamount < 24:
        print ("Less than min range")
    elif intamount >1000:
        print("Greater than max range")
    elif intamount % 5 == 0:
        divisor = 5
        listchars = int(intamount / divisor)
        i = 0
        charlist = [5]
        outputlist = [5]
        while i < listchars-1:
            outputlist = charlist + outputlist
            i += 1
        print(outputlist)
    elif intamount % 7 == 0:
        divisor = 7
        listchars = int(intamount / divisor)
        i = 0
        charlist = [7]
        outputlist = [7]
        while i < listchars-1:
            outputlist = charlist + outputlist
            i += 1
        print(outputlist)
    elif (intamount - 7) % 5 == 0:
        listchars = (intamount - 7)/5
        i = 0
        charlist = [5]
        outputlist = [7]
        while i < listchars:
            outputlist = charlist + outputlist
            i += 1
        print(outputlist)
    elif (intamount - 14) % 5 == 0:
        listchars = (intamount - 14)/5
        i = 0
        charlist = [5]
        outputlist = [7,7]
        while i < listchars:
            outputlist = charlist + outputlist
            i += 1
        print(outputlist)
    elif (intamount - 21) % 5 == 0:
        listchars = (intamount - 21)/5
        i = 0
        charlist = [5]
        outputlist = [7,7,7]
        while i < listchars:
            outputlist = charlist + outputlist
            i += 1
        print(outputlist)
    elif (intamount - 28) % 5 == 0:
        listchars = (intamount - 28)/5
        i = 0
        charlist = [5]
        outputlist = [7,7,7,7]
        while i < listchars:
            outputlist = charlist + outputlist
            i += 1
        print(outputlist)

change(amount)
