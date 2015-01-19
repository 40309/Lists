#Tony K.
#19/01/2015
#Spotcheck Q1 - part d

scores = [18,23,36,21,58,40,45,59]
temp = 0
maximum = 8
for count1 in range(1,(maximum-1)):
    for count2 in range(1,(maximum-1)):
        if scores[count2] > scores[count2 + 1]:
            temp = scores[count2]
            scores[count2] = scores[count2 + 1]
            scores[count2 + 1] = temp
print(scores)

length = len(scores)
count = 0
for score in scores:
    count = count + 1
    print("{0:>2}. | {1:>2}".format(count,score))
