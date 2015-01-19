#Tony K.
#Class Work
#2D List

def table(players):
    length =  len(players)
    longest = 0
    for player in range(length):
        player = player - 1
        temp = len(players[player][0])
        if temp > longest:
            longest = temp
    
    print(longest)
    print("-"*31)
    print("|{0:<}|{1:>6}|{2:>6}|".format("Player","Kills","Deaths"))
    print("-"*31)
    for each in range(length):
        each = each - 1
        print("|{0:<15}|{1:>6}|{2:>6}|".format(players[each][0],players[each][1],players[each][2]))
        print("-"*31)

players = [["k1llmAchine",51,49],["bob2247",5,99],["hAxOr12",72, 30]]

table(players)
