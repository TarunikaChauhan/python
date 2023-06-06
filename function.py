def most_frequent(string):
    # create an empty dictionary to store the frequency of each letter
    frequency = {}

    # iterate over the characters in the string
    for char in string:
        # check if the character is already in the dictionary
        if char in frequency:
            # if the character is in the dictionary, increment its count
            frequency[char] += 1
        else:
            # if the character is not in the dictionary, add it with a count of 1
            frequency[char] = 1

    # sort the dictionary by value (i.e., by frequency) in decreasing order
    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

    # print the letters and their frequencies in decreasing order
    for item in sorted_frequency:
        print(item[0], "=", item[1], end=" ")
