test_case_1 = "abacdaefdjij"
test_case_2 = "abacdfgdy"

dict = {}
for i in range(len(test_case_2)):
    letter = test_case_2[i]
    dict.setdefault(letter, []).append(i)

print(dict)

arrays = []
offset = 0
for i, (current_letter, letter_indexes) in enumerate(dict.items()):

    # there's only 1 occurrence of the letter in the string
    if len(letter_indexes) == 1:
        v_val = letter_indexes[0] - offset

        if len(arrays) == 0:  # if this the first case we're dealing with?
            arrays.append([current_letter])
        elif len(arrays[-1]) > v_val:   # is the letter inside of the last array's range
            arrays[-1][v_val] = current_letter
        else:
            offset += len(arrays[-1])
            arrays.append([current_letter])  # letter is outside

    # there's more than one letter in the string
    if len(letter_indexes) >= 2:
        v_min = letter_indexes[0] - offset
        v_max = letter_indexes[-1] - offset

        if len(arrays) == 0:
            by = v_max - v_min + 1
            arrays.append([''] * by)
        elif v_min < len(arrays[-1])-1 < v_max:  # current range intersects with the last array's range
            by = v_max - len(arrays[-1]) + 1
            arrays[-1].extend([''] * by)  # extend the last array
        elif len(arrays[-1])-1 < v_min:  # new range is outside of the last array's range
            offset += len(arrays[-1])
            by = v_max - len(arrays[-1]) + 1
            arrays.append([''] * by)  # create a new array

        for v_val in letter_indexes:
            arrays[-1][v_val - offset] = current_letter

    # print(f'k: {k}, v: {v}')

# print(arrays)
print(["".join(x) for x in arrays])
