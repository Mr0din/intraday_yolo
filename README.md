# intraday_yolo



the idea is to generate chunks of intraday data into qr code the first part does that and the seocnd is to run a yolo model on the generated qr images (trained and then predicted)
unforfunately this method gave about 56% accuracy (i have seen better) and the over loss of about 2% per month (i didnt try it for longer duration say 6 month or year)
the learning here is how crucial is to determine a stoploos is. So as next step i will try to createa model that will only predict the stoploss
i saw that if the stop loss was adjusted correctly i was gaining about 2 percent profit in the model 

