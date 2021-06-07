
import pandas as pd
from pymongo import MongoClient ,ASCENDING,DESCENDING
from image_generator import image_generator
from category_generator import category_generator
from tqdm import tqdm


reread = pd.read_hdf('hfiles/ICICIBANK.h5','data_set')
data=reread.sort_values(["date",'time'], ascending=[True,True])

interval=20



def conn(n): # data connection 
    conn = MongoClient("192.168.0.10", 27017)
    db = conn.market
    collection = db[n]
    return collection


def data_generator(data1):
    for count in range (len(data1.index)):
        if count > (len(data1.index)-5):
            pass
        else:
            first_set= data1.iloc[count:count+interval]
            next_set= data1.iloc[count+interval:count+interval+5]
        
            # image image_generator
            image_name,labels=image_generator(first_set)
        
        

            # # # label generator
            category_index= category_generator(first_set,next_set)
          
            new_string= str(category_index)+' '+''.join(str(labels))
            new_string=new_string.replace('(','')
            new_string=new_string.replace(')','')
            new_string=new_string.replace(',','')
            text_file=open('img_data/train/labels/'+image_name+'.txt','w')
            text_file.write(new_string)
            text_file.close


    

        
    return 1


def trainsession():
    tikr_list=["AUROPHARMA"]
   
    for tikr in tikr_list:
        dates=list(conn('with_sense').distinct('date'))
     
        for d in tqdm(dates):
            data_set=list(conn('with_sense').find({'date':d,'tikr':tikr}).sort('time',ASCENDING))
            data_set=pd.DataFrame(data_set)
            data_generator(data_set)
           
     




trainsession()

#"ADANIENT","ADANIPORTS","AMBUJACEM","ARVIND","ASHOKLEY","ASIANPAINT","AUROPHARMA","AXISBANK","BAJAJ-AUTO","BAJFINANCE","BANKBARODA","BANKINDIA","BHARATFORG","BHARTIARTL","BHEL","BOSCHLTD","BPCL","CANBK","CENTURYTEX","CIPLA","COALINDIA","DISHTV","DLF","DRREDDY","EICHERMOT","GAIL","GOLDBEES","GRASIM","HCLTECH","HDFC","HDFCBANK","HDIL","HEROMOTOCO","HINDALCO","HINDPETRO","HINDUNILVR","IBREALEST","IBULHSGFIN","ICICIBANK","IDBI","IDEA","IDFC","INDUSINDBK","INFRATEL","INFY","IOC","ITC", "JINDALSTEL","JSWSTEEL","KOTAKBANK","LICHSGFIN","LT","LUPIN","M&M","MARUTI","NMDC","NTPC","ONGC","PFC", "PNB","POWERGRID","RCOM","RELCAPITAL","RELIANCE","RELINFRA","RPOWER","SAIL","SBIN","SIEMENS","SUNPHARMA","SUNTV","TATAGLOBAL","TATAMOTORS","TATAMTRDVR","TATAPOWER","TATASTEEL","TCS","TECHM","TITAN","ULTRACEMCO","UNIONBANK","UPL","VEDL","VOLTAS","WIPRO","WOCKPHARMA","YESBANK","ZEEL"