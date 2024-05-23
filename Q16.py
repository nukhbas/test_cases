def long_words(list1, n):

    return [word for word in list1 if len(word) > n]


list1 = ['twister', 'candy', 'bubbly', 'galaxy']

if __name__ == '__main__':
    print(long_words(list1, 5))
