import os
import pandas as pd
from datetime import timedelta
os.getcwd()
myData = pd.read_csv('C:/Users/Students/PycharmProjects/ejwang/train_gps_points.csv')
myData['Datetime'] = pd.to_datetime(myData['Datetime'])
myData['Datetime'] = myData['Datetime'] + timedelta(hours=8)

newDf = pd.DataFrame(columns=['newDatetime', 'newCount'])
timeStamp = pd.date_range(start='2016-02-01 08:00', end='2017-02-01 00:00', freq='H')

for i in range(0, len(timeStamp)):
    if i != len(timeStamp)-1:
        myRange = myData[myData['Datetime'].between(timeStamp[i], timeStamp[i+1])]
        newDf.loc[i, 'newDatetime'], newDf.loc[i, 'newCount'] = timeStamp[i], len(myRange)
newDf.to_csv('myResult.csv', index=0)