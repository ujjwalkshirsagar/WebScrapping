# opening the csv file in 'w+' mode
uk=[]
print(len(dict_list))
i=0
if len(dict_list)!=0:
    
    for u in dict_list:
        i==0
        keys_values = dict_list[i].items()
        new_d = {str(key): str(value) for key, value in keys_values}
        i+=1
        
        uk.append(new_d)
else:
    print("End of Program")
 
import pandas as pd  
df = pd.DataFrame(uk) 
    
# saving the dataframe 
df.to_csv('Scraped_profile_Details.csv')
print("Go To Scraped_profile_Details.csv for csv file of details")
