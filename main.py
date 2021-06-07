
import pandas as pd
from pymongo import MongoClient ,ASCENDING,DESCENDING
from image_generator import image_generator
from category_generator import category_generator
from tqdm import tqdm
import numpy as np
from sklearn.preprocessing import MinMaxScaler


 


def data_generator(data1):

    data1=data1[['close','high','low','open','BBANDSHIGH', 'BBANDSLOW']]
    # scaler = MinMaxScaler((1,100))

    # scaled = scaler.fit_transform(data1)
    # data=pd.DataFrame(scaled, columns=data1.columns)
    

    change_status=0
    for i in data.index:
        if i >= len(data.index)-12 or i <= 2 or change_status==1:
            pass
        else:
            first_part=data[i:i+5]
            second_part= data[i+7:i+12]
            category_index=category_generator(first_part,second_part)
            if category_index ==2:
             
                pass
            else:
                new_data_set= data[i-2:i+3]
                name,labels=image_generator(new_data_set)
                new_string= str(category_index)+' '+''.join(str(labels))
                new_string=new_string.replace('(','')
                new_string=new_string.replace(')','')
                new_string=new_string.replace(',','')
                text_file=open('img_data/train/labels/'+name+'.txt','w')
                text_file.write(new_string)
                text_file.close

            # new_string= str(category_index)+' '+''.join(str(labels))
            # new_string=new_string.replace('(','')
            # new_string=new_string.replace(')','')
            # new_string=new_string.replace(',','')
            # text_file=open('img_data/train/labels/'+image_name+'.txt','w')
            # text_file.write(new_string)
            # text_file.close


        

        
    return 1


def trainsession(reread):
    dates = list(np.unique(reread['date']))
   
    for date in dates:
        data_set = reread.loc[reread['date'] == date]
        data_generator(data_set)
        
        
     
storage_list=["ADANIENT","ADANIPORTS","AMBUJACEM","ARVIND","ASHOKLEY","ASIANPAINT","AUROPHARMA","AXISBANK","BAJAJ-AUTO","BAJFINANCE","BANKBARODA","BANKINDIA","BHARATFORG","BHARTIARTL","BHEL","BOSCHLTD","BPCL","CANBK","CENTURYTEX","CIPLA","COALINDIA","DISHTV","DLF","DRREDDY","EICHERMOT","GAIL","GOLDBEES","GRASIM","HCLTECH","HDFC","HDFCBANK","HDIL","HEROMOTOCO","HINDALCO","HINDPETRO","HINDUNILVR","IBREALEST","IBULHSGFIN","ICICIBANK","IDBI","IDEA","IDFC","INDUSINDBK","INFRATEL","INFY","IOC","ITC","JINDALSTEL","JSWSTEEL","KOTAKBANK","LICHSGFIN","LT","LUPIN","M&M","MARUTI","NMDC","NTPC","ONGC","PFC", "PNB","POWERGRID","RCOM","RELCAPITAL","RELIANCE","RELINFRA","RPOWER","SAIL","SBIN","SIEMENS","SUNPHARMA","SUNTV","TATAGLOBAL","TATAMOTORS"]
storage_list2=["TATAMTRDVR","TATAPOWER","TATASTEEL","TCS","TECHM","TITAN","ULTRACEMCO","UNIONBANK","UPL","VEDL","VOLTAS","WIPRO","WOCKPHARMA","YESBANK","ZEEL"]



if __name__ == "__main__":

    for i in tqdm(storage_list):
        reread = pd.read_hdf('hfiles/'+i+'.h5','data_set')
        if reread['close'][10]<50:
            pass
        else:
         
            data=reread.sort_values(["date",'time'], ascending=[True,True])
            trainsession(data)
    
 

    
    

