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
    engine = create_engine("postgresql://postgres:yourPassword@yourDomainName.com:5432/raven")
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
plt.figure(figsize=(12, 6))

def genimage():
    Datas=session.query(
        top100sum.time,
        top100sum.topSum,
        top100sum.supply
        ).all()

    def percent(data):
        return [data[0],100*data[1]/data[2]]

    Datas=map(percent,Datas)
    
    Datas = pd.DataFrame(data=Datas, columns=['Time','Position'])
    Conv = pd.DataFrame(data=Datas['Time'][4:],columns=['Time'])
    Conv["Position"]=np.convolve(Datas['Position'],[0.2,0.2,0.2,0.2,0.2],'valid')
    Datas=Datas[4:]
    Datas['Region']="RawPosition(%)"
    Conv['Region']="Convolove(%)"
    # print(Datas)
    # print(Conv)
    Datas=pd.concat([Datas,Conv])
    print(Datas)
    image=sns.lineplot(data=Datas,x='Time',y='Position',hue='Region')
    
    plt.title('Raven Monitor of Top100 Richest  updated:'+curTime())
    plt.savefig("./new.jpg")

while(True):
    genimage()
    print(curTime()+"已更新")
    time.sleep(60*15) #每15分钟更新一次