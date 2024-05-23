def longestlength(lst):

    longest = ""
    for w in lst:
        if len(w) > len(longest):
            longest = w
    return len(longest)


if __name__ == '__main__':

    print(longestlength(['bounty', 'twister', 'milka']))
