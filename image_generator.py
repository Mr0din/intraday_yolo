

import pandas as pd
from datetime import datetime
import random
import string
import numpy as np 
from sklearn import preprocessing 

import itertools


import plotly.graph_objects as go
from plotly.graph_objects import Layout
from datetime import datetime




def convert_labels(w,h,x1, y1, x2, y2):
    """
    Definition: Parses label files to extract label and bounding box
        coordinates.  Converts (x1, y1, x1, y2) KITTI format to
        (x, y, width, height) normalized YOLO format.
    """
    def sorting(l1, l2):
        if l1 > l2:
            lmax, lmin = l1, l2
            return lmax, lmin
        else:
            lmax, lmin = l2, l1
            return lmax, lmin
    
    xmax, xmin = sorting(x1, x2)
    ymax, ymin = sorting(y1, y2)
    dw = 1./h
    dh = 1./w
    x = (xmin + xmax)/2.0
    y = (ymin + ymax)/2.0
    w = xmax - xmin
    h = ymax - ymin
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)



def candlestick_generator(data,name):
    data.reset_index(inplace=True)
    df=data
    df =df[0:10]
    layout = Layout(
    # paper_bgcolor='rgba(255,255,255,255)',
    # plot_bgcolor='rgba(255,255,255,255)',
    width=400,
    height=400,
    margin={'l':5,'r':5,'t':5,'b':5}
)
    fig = go.Figure(data=[go.Candlestick(open=df['open'],high=df['high'],low=df['low'],close=df['close'])], layout=layout)
    fig.update_layout(xaxis_rangeslider_visible=False)
    fig.update_yaxes(showticklabels=False)
    fig.update_xaxes(showticklabels=False)
    

    # N = len(df['open'])
    # x = np.linspace(0, 4,5)

    # y = df['open'][x]

  
    

    fig.add_shape(type='line',x0=0,y0=df['BBANDSHIGH'][0],x1=1,y1=df['BBANDSHIGH'][1])
    fig.add_shape(type='line',x0=1,y0=df['BBANDSHIGH'][1],x1=2,y1=df['BBANDSHIGH'][2])
    fig.add_shape(type='line',x0=2,y0=df['BBANDSHIGH'][2],x1=3,y1=df['BBANDSHIGH'][3])
    fig.add_shape(type='line',x0=3,y0=df['BBANDSHIGH'][3],x1=4,y1=df['BBANDSHIGH'][4])


    fig.add_shape(type='line',x0=0,y0=df['BBANDSLOW'][0],x1=1,y1=df['BBANDSLOW'][1])
    fig.add_shape(type='line',x0=1,y0=df['BBANDSLOW'][1],x1=2,y1=df['BBANDSLOW'][2])
    fig.add_shape(type='line',x0=2,y0=df['BBANDSLOW'][2],x1=3,y1=df['BBANDSLOW'][3])
    fig.add_shape(type='line',x0=3,y0=df['BBANDSLOW'][3],x1=4,y1=df['BBANDSLOW'][4])


    
    fig.write_image("img_data/train/images/"+name+".png")
    x11,y11,x22,y22=0,0,400,400
    labels=convert_labels(300,300,x11, y11, x22, y22)
    return labels


    

# def stockline_generator(dataqr,name):
#     plt.figure(figsize=(2,1))
#     plt.plot(dataqr )
#     #plt.tight_layout()
#     plt.axis('off')
#     name ='img_data/train/images/'+name+'.png'

#     # img = qrcode.make(dataqr)
#     # img=img.resize((400,400))
#     # img1 = ImageDraw.Draw(img)  
#     x1,y1,x2,y2=5,5,200,200
#     labels=convert_labels(200,200,x1, y1, x2, y2)
#     plt.savefig(name)
#     plt.close()
#     return labels
    


#     #x,y,w,h=convert_labels(w,h,)


 

def image_generator(data):
    data= data[['high', 'low','close','open', 'BBANDSLOW','BBANDSHIGH']]
    name= (''.join(random.choices(string.ascii_uppercase +string.digits, k = 8)))
    labels=candlestick_generator(data,name)
    return name, labels


     

           
    