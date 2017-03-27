# input: string
# output: "letter, freq" in order of ascend freq, then alphabetical


def letter_frequency(string):
    counter = {}

    for letter in string:
        counter[letter] = counter.get(letter, 0) + 1

    vals = sorted(list(set(counter.values())))

    for val in vals:
        keys_lst = []
        for key in counter:
            if counter[key] == vals:
                keys_lst.append(key)

        keys_lst.sort()

        for key in keys_lst:
            print key, val
