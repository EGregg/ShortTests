#Interview prep question, wanted to compare a string with the next string in a list. If the the 2 are different, then print out the pair, if the 2 are the same then do nothing.

pairs = ["tiger", "lion", "penguin", "leopard"]

for x in range(1,len(pairs)):
    for y in range(1,len(pairs)):
        if pairs[x] != pairs[y]:
            print (pairs[x] + " and " + pairs[y]) 
