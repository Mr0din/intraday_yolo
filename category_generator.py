

investment =400000
profit=10
category_index=[1,2,3]
interval_percentage=0.8
def no_of_shares(investment,stock_price):
    no_of_shares= round(investment/stock_price)
    return no_of_shares






def taxes(no_of_shares,sell_value,buy_value,diff):
    turnaround=no_of_shares*(sell_value+buy_value)
    print('turnaround',turnaround)
    brokerage= min(20,turnaround*0.0001) 
    print('brokerage',brokerage)
    stt= round((sell_value*no_of_shares)*0.00025)
    print('stt',stt)
    tc=round(turnaround*0.0000325,2)
    print('tc',tc)
    gst=round(0.18*(brokerage+tc),2)
    print('gst',gst)
    sebi=round(0.000001*turnaround,2)
    print('sebi',sebi)
    stamp=round(0.000002*turnaround,2)
    print('stamp',stamp)
    total=brokerage+stt+tc+gst+sebi+stamp
    print("Total Cost",total)
    print("trade_profit",diff)
    pnl=diff-total

    
    return pnl

def check_lables( profit, call):
    
    label=[0,0]
    if profit  in range (10, 100):
        label= [call,1]
    elif int(profit) in range (100, 300):
        label= [call,2]
    elif int(profit) in range (300, 500):
        label= [call,3]
    elif profit>= 500:
        label= [call,4]
    else:
        label= [3,0]

    label=int("".join(map(str, label)))
    
    return label


def category_generator(first,nxt):
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
    cat_index=category_index.index(call)
 


    return cat_index



    


    













