#Google Codejam 2022, d1000000 challenge, 02/04/2022
#get number of testcases
T=int(input())
testcasesN=[]
testSides=[]
#get all input
for i in range(T):
    N=int(input())
    testcasesN.append(N)
    S=input()
    testSides.append(S)
#iterate through testcases
for i in range(len(testcasesN)):
    #convert current index of testSides to a list
    _=testSides[i].split()
    #output largest possible number of straights
    print(f"Case #{i+1}: {len(_)-_.count(max(_))+1}")
