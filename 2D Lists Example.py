#Tony K.
#Class Work
#2D List

def table(players):
    print("|-----------------------------|")
    print("|{0:<15}|{1:>6}|{2:>6}|".format("Player","Kills","Deaths"))
    print("|-----------------------------|")
    for each in range(3):
        each = each - 1
        print("|{0:<15}|{1:>6}|{2:>6}|".format(players[each][0],players[each][1],players[each][2]))
        print("|-----------------------------|")

players = [["k1llmAchine",51,49],["bob2247",5,99],["hAxOr12",72, 30]]

table(players)
