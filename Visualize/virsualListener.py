#Time
import time
def curTime():
    return time.asctime(time.localtime(time.time()))+"  "

#SQL
from sqlalchemy import create_engine,func
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.automap import automap_base
try:
    print(curTime()+"开始连接SQL，请稍等") #Connect to database
    #please set your password here, default user name is postgres
    engine = create_engine("postgresql://postgres:MeiYouMiMa!@Infiiinity.xyz:5432/raven")
    base = automap_base()
    base.prepare(engine, reflect=True)

    print(curTime()+"开始打印Table") #Start print all table for debug
    for theClass in base.classes:
        print(theClass)

    top100sum=base.classes.top100sum
except Exception as err:
    print(curTime()+str(err)+"数据库连不上了") #the database failed

#SQL session
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

#Seaborn
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime
plt.figure(figsize=(16, 8))

def genimage():
    Datas=session.query(
        top100sum.time,
        top100sum.topSum100,
        top100sum.topSum20,
        top100sum.supply
        ).all()

    def percentOf100(data):
        return [data[0],100*data[1]/data[3]]
        
    def percentOf20(data):
        return [data[0],100*data[2]/data[3]]

    DatasOf100=map(percentOf100,Datas)
    DatasOf20=map(percentOf20,Datas)
    
    DatasOf100 = pd.DataFrame(data=DatasOf100, columns=['Time','Position'])
    DatasOf20 = pd.DataFrame(data=DatasOf20, columns=['Time','Position'])

    Conv100=[]
    Conv20=[]

    if(len(DatasOf100)>=10):
        Conv100 = pd.DataFrame(data=DatasOf100['Time'][9:],columns=['Time'])
        Conv100["Position"]=np.convolve(DatasOf100['Position'],[0.1]*10,'valid')

    if(len(DatasOf20)>=10):
        Conv20 = pd.DataFrame(data=DatasOf20['Time'][9:],columns=['Time'])
        Conv20["Position"]=np.convolve(DatasOf20['Position'],[0.1]*10,'valid')

    DatasOf100['Region']="RawTop100Position(%)"
    print(DatasOf100)
    DatasOf20['Region']="RawTop20Position(%)"
    print(DatasOf20)
    if(len(Conv100)>0):
        Conv100['Region']="Top100Convolove(%)"
        print(Conv100)
    if(len(Conv20)>0):
        Conv20['Region']="Top20Convolove(%)"
        print(Conv20)
    if((len(Conv100)>0) & (len(Conv20)>0)):
        Datas=pd.concat([DatasOf100,Conv100,DatasOf20,Conv20])
    else:
        Datas=pd.concat([DatasOf100,DatasOf20])
    plt.cla()
    image=sns.lineplot(data=Datas,x='Time',y='Position',hue='Region')
    plt.title('Raven Monitor of Top100 Richest  updated:'+curTime())
    plt.savefig("./new.jpg")

while(True):
    genimage()
    print(curTime()+"已更新")
    time.sleep(60*15) #每15分钟更新一次