def sequence(original, target):

    permutation = []

    chars_original = []
    for char in original:
        chars_original.append(char)
    print('original: ', chars_original)

    chars_target = []
    for char in target:
        chars_target.append(char)
    print('target: ', chars_target)


    for i in range(0, len(target)):
        if chars_target[i]== chars_original[i]:
            continue
        else:
            temp_list = []
            temp_list.append(i)
            j = chars_original.index(chars_target[i])
            temp_list.append(j)
            temp = chars_original[i]
            chars_original[i] = chars_original[j]
            chars_original[j] = temp
            a = tuple (temp_list)
            permutation.append(a)
            print(permutation)
            print(chars_original)

    return permutation

sequence('MARINE', 'AIRMEN')
