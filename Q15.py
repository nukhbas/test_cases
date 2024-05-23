def highest_limit(int):
    
    longest = ""
    for w in int:
        if len(w) > len(longest): 
            longest = w
    return len(longest)
 
           
if __name__ == '__main__':

    print(highest_limit(['bounty', 'twister', 'milka']))

