def longest_length(ch):

    longest = ""
    for w in ch:
        if len(w) > len(longest):
            longest = w
    return len(longest)


if __name__ == '__main__':

    print(longest_length(['bounty', 'twister', 'milka']))
