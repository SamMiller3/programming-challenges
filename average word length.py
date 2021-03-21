#average word length, 21/03/2021, problem from towardsdatascience.com / sololearn.com
sentance = input()
sentance = sentance.split()
i = 0
average = 0
for i in range(len(sentance)):
    average += len(sentance[i])
average = average/len(sentance)
print("average word length: " + str(average))
