import sys
lines = sys.stdin.read().splitlines()

dic = {"Algorithm" :204,
       "DataAnalysis" :	207,
       "ArtificialIntelligence" : 302,
       "CyberSecurity" : "B101",
       "Network" :303,
       "Startup":501,
       "TestStrategy" : 105}
for i in lines[1:]:
    print(dic[i])