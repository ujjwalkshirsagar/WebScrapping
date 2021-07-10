import requests
import re
import json
from bs4 import BeautifulSoup
import requests
import csv


def csv_reader_list(file_name):
    
    list_l=[]
    csv_file= open(file_name, 'r')
    csv_reader = csv.reader(csv_file)
    for row in csv_reader: 
        list_l.append(row)
    csv_file.close()
    return list_l


def extract_json_objects(text, decoder=json.JSONDecoder()):

    pos = 0
    while True:
        match = text.find('{', pos)
        if match == -1:
            break
        try:
            result, index = decoder.raw_decode(text[match:])
            yield result
            pos = match + index
        except ValueError:
            pos = match + 1
            
            
            
list_to_scrape = csv_reader_list("Scraped_profile.csv") 


dict_list = []  
error_roposo = []   


for row in list_to_scrape:
    url = ' '.join(map(str, row))
    key_id=url[-36:]
    
    
    if (len(url)!=0):
        print(url)
        
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content,'html.parser')
        data=soup.find_all(id='initial-state'.strip())
        listToStr = ' '.join([str(elem) for elem in data])
        listTostr1=listToStr[52:-10]
        data=listTostr1.replace('\\','')
        
        
        for result in extract_json_objects(data):
            try:
                dict1 = {}
                dict_publishers= result['data']['det'][key_id]
                
                keys = ['sex', 'followers','following','twHandle']
                dict1 = {x:str(dict_publishers[x]).replace('\n',' || ') for x in keys}
                dict1["link"] = url
                print(json.dumps(dict1,indent=2))
                dict_list.append(dict1)
                #listD.append(url)
            except Exception as e: 
                print("Cannot Find ", e)
                error_roposo.append(url)
                continue
                
            
            try:
                dict1 = {}
                dict_publishers= result['data']['det'][key_id]
                
                keys = ['blogURL']
                dict1 = {x:str(dict_publishers[x]).replace('\n',' || ') for x in keys}
                #dict1["link"] = url
                print("Youtube Link :",json.dumps(dict1,indent=2))
                dict_list.append(dict1)
                #listD.append(url)
            except Exception as e: 
                print("Cannot Find ", e)
                error_roposo.append(url)
               
        
            try:
                dict1 = {}
                dict_publishers= result['data']['det'][key_id]
                
                keys = ['about']
                dict1 = {x:str(dict_publishers[x]).replace('\n',' || ') for x in keys}
                #dict1["link"] = url
                print(json.dumps(dict1,indent=2))
                dict_list.append(dict1)
                #listD.append(url)
            except Exception as e: 
                print("Cannot Find ", e)
                error_roposo.append(url)

       
            

        
        
        print(len(dict_list)+1)
    else:
        print("----------")
  
                              

print("\n ========================= END OF PROGRAM ========================= ")

       
