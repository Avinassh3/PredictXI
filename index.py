import dumbster
import cleandata
import genrat




batna=['odidata.csv','testdata.csv','t20data.csv']
bowna=['odibowldata.csv','testbowling.csv','t20bowling.csv']
print("-----------------Welcome to statical predictor-----------")
print("-----Want to update data------")
sq=input("YES OR NO : ")
if(sq=="YES"):
    dumbster.workit()
    cleandata.clean()

    print("---------Updated Data---------")

team=["England","Australia","SouthAfrica","Newzealand","Westindies","INDIA","Pakistan","Srilanka"]
formt=["ODI","TEST","T20"]
pitch=["BATTING","Bowling"]
a=[]
b=[]
dd=[]
sss=0
ssss=0

print("------Select Two teams------- ")
while True:

    for i in range(8):
        print("{}          {}".format(i+1,team[i]))
    s=int(input("enter team no 1 : "))
    g=int(input("enter team no 2 : "))
    if(s!=g):
        a.append(team[s-1])
        a.append(team[g-1])
        print("selection done")
        break
print("-------Select format of play---------")
while True:
    for j in range(3):
        print("{}          {}".format(j+1,formt[j]))
    fo=int(input("enter your choice : "))
    if(fo<=3):
        b.append(formt[fo-1])
        sss=fo-1
        print("format selected")
        break
print("-------Select pitchType---------")
while True:
    for j in range(2):
        print("{}          {}".format(j+1,pitch[j]))
    fo=int(input("enter your choice : "))
    if(fo<=2):
        dd.append(pitch[fo-1])
        ssss=fo-1
        print("PitchType selected")
        break

print("----------------XXXXX----------------")
print("-----generating playing Xl For Details  ----- ")
print("-----teams selected are : ")
print(a[0])
print(a[1])
print("------Format selected is : {} ".format(b[0]))
print("--------Pitch type : {} ".format(dd[0]))
print("----------------XXXXX----------------\n")
#genrat.odiBAT(a)
#genrat.odiBOWL(a)
#genrat.finalteam(a,batna[sss],bowna[sss],sss)
genrat.finalteam(a,batna[sss],bowna[sss],sss,ssss)