# this code is ripped form some stack overflow post but it works.
# make it better though, surely there is a way to take it from excel etc


import datetime as dt

dates = ['01/13/2019','01/16/2019','02/21/2019', '04/02/2019', '04/15/2019',
         '04/18/2019','04/19/2019','04/20/2019','04/21/2019','04/22/2019',
         '04/23/2019', '04/24/2019', '04/25/2019', '04/28/2019', '04/29/2019',
         '05/01/2019', '05/02/2019', '05/05/2019']
x = [dt.datetime.strptime(d,'%m/%d/%Y').date() for d in dates]
y = [3250,2940,4140,4650,4990,5090,5210,5190,5430,5190,5310,5290,5360,5400,5470,5580,5590,5640]
#y = range(len(x)) # many thanks to Kyss Tao for setting me straight here



import matplotlib.pyplot as plt
import matplotlib.dates as mdates

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
x1 = x[4:]
y1 = y[4:]
plt.plot(x1,y1)
plt.gcf().autofmt_xdate()
plt.show()