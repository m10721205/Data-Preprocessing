import os #載入系統套件
import pandas as pd #表格處理套件
from datetime import timedelta #時間計算套件
os.getcwd() #取得系統路徑
myData = pd.read_csv('C:/Users/Students/PycharmProjects/ejwang/train_gps_points.csv') #讀取經緯度資料
myData['Datetime'] = pd.to_datetime(myData['Datetime']) #將"日期"欄位轉換日期型態
myData['Datetime'] = myData['Datetime'] + timedelta(hours=8) #將"日期"欄位內的時間+8小時

newDf = pd.DataFrame(columns=['newDatetime', 'newCount']) #新建dataframe
timeStamp = pd.date_range(start='2016-02-01 08:00', end='2017-02-01 00:00', freq='H') #在經緯度資料內的時間區間建立以每小時為單位的時間戳

for i in range(0, len(timeStamp)): #用for跑範圍界timestamp時間戳
    if i != len(timeStamp)-1: #如果計數器i不等於時間戳的數量
        myRange = myData[myData['Datetime'].between(timeStamp[i], timeStamp[i+1])] #從原資料中的時間篩選時間界在一小時的區間內的資料稱為myRange
        newDf.loc[i, 'newDatetime'], newDf.loc[i, 'newCount'] = timeStamp[i], len(myRange) 
        #將篩出來的資料依據當前迴圈內的時間戳放入newDf的"newDatetime"欄位，並對篩選出的myRange變數取len來計算資料筆數放入"newCount"欄位
newDf.to_csv('taxiDataClean.csv', index=0) #輸出CSV檔
