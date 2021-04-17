def handler(event,context):
    #Time
    import time
    def curTime():
        return time.asctime(time.localtime(time.time()))+"  "

    #SQL
    from sqlalchemy import create_engine
    from sqlalchemy import Column, Integer, String
    from sqlalchemy.ext.automap import automap_base
    try:
        print(curTime()+"开始连接SQL，请稍等") #Connect to database
        #please set your password here, default user name is postgres
        engine = create_engine("postgresql://postgres:yourPassWord@yourDomainName.com:5432/raven",echo=True)
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

    import requests
    import json
    response = requests.get('https://ravencoin.network/api/statistics/richest-addresses-list')
    content=json.loads(response.content)
    topSum=0
    for record in content:
        topSum+=int(record['balance'])
    print(curTime()+"当前top总和："+str(topSum)+"RVN") #top100 sum

    response = requests.get('https://ravencoin.network/api/statistics/total-supply?format=object')
    content=json.loads(response.content)
    supply=content['supply']

    print(curTime()+"当前总流通："+str(supply)+"RVN") #total supply
    session.add(top100sum(topSum=topSum,supply=supply))
    session.flush()
    session.commit()
