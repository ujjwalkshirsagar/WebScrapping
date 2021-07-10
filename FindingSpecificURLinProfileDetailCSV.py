import csv
import re
re.compile('<title>(.*)</title>')
new=[]
instaId=[]
def Find(string):
   # findall() has been used 
    # with valid conditions for urls in string
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)      
    return [x[0] for x in url]


i=0
a='instagram'     #String that you want to search


with open("Scraped_profile_Details.csv",encoding="utf8") as f_obj:
    reader = csv.reader(f_obj, delimiter=',')
    
    for line in reader:           #Iterates through the rows of your csv
        #print(line)              #line here refers to a row in the csv
        
        if a in str(line):        #If the string you want to search is in the row
            
            new.append(str(line))
            i+=1
        continue
        
      
#print(new)

str1 = ''.join(str(e) for e in new)


#print("Urls: ", Find(str1))        #Finds Every URL in String Including Youtube and all

d=Find(str1)
i=0
j=len(d)
while i!=j:
    m=d[i][0:21]
    if m=="https://www.instagram":
            print(d[i])
            instaId.append(d[i])
    else:
        print("")
    i+=1

if len(instaId)==0:
    print("No Insta Profile Found")
#print(instaId)

import pandas as pd  
df = pd.DataFrame(instaId) 
    
# saving the dataframe 
df.to_csv('Scraped_profile_Details_instaID.csv')
