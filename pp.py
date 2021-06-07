import pandas as pd
#from pymongo import MongoClient ,ASCENDING,DESCENDING
from tqdm import tqdm
import requests
import h5py    
import numpy as np   
import json

interval_percentage=0.1
def get_data_api (dataframe):

    url = 'http://192.168.0.6:5000'
    x = requests.post(url, json = dataframe)
    result=list(x.json())
    print(result)
    error_total=[]
    for i in result:
        error_total.append(abs(i[1]-0)+abs(i[2]-0)+abs(i[3]-1)+abs(i[4]-1))
    
    max_value=min(error_total)
    index_value = error_total.index(max_value)
    final_value=int(result[index_value][0])
    category_index=[1,2,3]

    final_result=category_index[final_value]

   

    return final_result


def get_real_bband(first,nxt):
    high_future_price = nxt['high'].max()
    low_future_price=nxt['low'].min()
    buy_price= first['close'].iloc[-1]
    
    #shares= no_of_shares(investment,buy_price)
    if ((high_future_price-buy_price)/buy_price )*100 >=((buy_price-low_future_price)/buy_price )*100 and ((high_future_price-buy_price)/buy_price )*100 >= interval_percentage:
        
        call=1 # buy 
        # buy_value=buy_price
        # sell_value=high_future_price
        # diff= abs(buy_price-sell_value)*shares
    elif ((buy_price-low_future_price)/buy_price )*100 >= interval_percentage :
        call=2 # sell
        # sell_value=low_future_price
        # buy_value=buy_price
        # diff= abs(buy_price-sell_value)*shares
    else:
        call= 3 # dont do anything
        # sell_value=buy_price
        # buy_value=buy_price
        # diff= abs(buy_price-sell_value)*shares
    

    
    # print('Call is',call)
    # pnl =taxes(shares,sell_value,buy_value,diff)
    # cat=check_lables( pnl, call)
    return call


def get_real(first,next1):
    high_future_price = next1['high'].max()
    low_future_price=next1['low'].min()
    buy_price= first['close'].iloc[-1]
    #shares= no_of_shares(investment,buy_price)
    if abs(high_future_price-buy_price) > abs(buy_price-low_future_price):
        call=1 # buy 
        # buy_value=buy_price
        # sell_value=high_future_price
        # diff= abs(buy_price-sell_value)*shares
    elif abs(buy_price-high_future_price) < abs(buy_price-low_future_price):
        call= 2 # sell
        # sell_value=low_future_price
        # buy_value=buy_price
        # diff= abs(buy_price-sell_value)*shares
    else:
        call= 3 # dont do anything
        # sell_value=buy_price
        # buy_value=buy_price
        # diff= abs(buy_price-sell_value)*shares

    return call


        
 
def main():

    reread = pd.read_hdf('hfiles/ADANIENT.h5')
    reread=reread[['date','time','close','high','low','open','BBANDSHIGH', 'BBANDSLOW']]
    reread=reread.sort_values(["date",'time'], ascending=[True,True])
    
   
    dates= list(np.unique(reread['date'])) 

    
    real_data=[]
    pred_data=[]
   

    for date in dates:

        new_data= reread.loc[reread['date'] == date]
  
        for i in tqdm(new_data.index):
            if i>= len(new_data.index)-5:
                pass
            else:
                reread1 =new_data[i:i+20]
                reread1.reset_index(inplace=True)
        
                reread2=new_data[i+20:i+25]
               
                reread2.reset_index(inplace=True)
                #print(reread1,reread2)
                input_data =json.loads(reread1.to_json(orient='records'))
                prediction=get_data_api(input_data)
          
                real= get_real_bband(reread1,reread2)
                new_list=[real,prediction]
           
                real_data.append(new_list)
                print(new_list)

         
            
            
        # new_df=(pd.DataFrame(real_data,columns=['real','pred']))
        # new_df.to_csv('sbi.csv')
        # break





main()


