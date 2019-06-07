import requests
import bs4
import scrap
import csv
# funtion takes input: a file name to store data
# output : scrapped data is stored in csv file it collects test match data
def marks(filename):
    
    count=0
    teamscount=0
    with open(filename,'w',newline='')as f: #opening a csv file
        thewritter=csv.writer(f)
        thewritter.writerow(['rank','Name','Score','submission'])
        for i in range(0,1):
            tr=requests.get("http://mentorpick.com/course/view/5be560ff5f929e4e6b540f79")
            sopu=bs4.BeautifulSoup(tr.text,'lxml')
            rt=[]
            containers = sopu.findAll('span')
            print(containers)
           #for row in sopu.findAll('table')[0].tbody.findAll('tr'):
             #   count=count+1
               # if True: # if and else are used to change in rows data in diffrent webpages
                 #   x= row.findAll('td')[0]
                   # xx= row.findAll('td')[1]
                    #y= row.findAll('td')[2]
                    #yy=row.findAll('td')[3]
                    #print("{} {} {} {}".format(x,xx,y,yy))"""



marks("abc.csv")
