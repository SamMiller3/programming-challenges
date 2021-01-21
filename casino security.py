#CASINO SECURITY, for sololearn.com
#input format: xxxGGxx$xxGxxT
#G=guards
#$=safe
#T=Thief
inpt = list(input(""))
t=inpt.index("T")
g=inpt.index("G")
d=inpt.index("$")
guards = list()
i=0
while i<=len(inpt)-1:
 if inpt[i] == "G":
  guards.append(i)
 i+=1
i=0
while i<=len(guards)-1:
 if abs(t-d) < abs(guards[i]-d):
  print("ALARM")
  exit()
 else:
  print("quiet")
  exit()
 i+=1
