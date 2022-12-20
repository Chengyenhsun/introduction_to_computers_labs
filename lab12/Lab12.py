#大台南公車轉運站資訊
#https://data.gov.tw/dataset/53570


import pymysql  #導入套件
import requests

#取得資料庫
r = requests.get("https://data.tainan.gov.tw/dataset/63224a5d-8864-4440-b602-6dda51d39a5c/resource/d2f45fea-13f3-4c7a-87c6-baf02f392bfd/download/opendata.json", verify=False)
list = r.json()  #將資料庫json檔轉成list

num = [i["項次"]for i in list]  #建立資料表中各項目的list
pln = [i["站名"]for i in list]
adr = [i["地址"]for i in list]
tel = [i["電話"]for i in list]


#資料庫連線
connect_db = pymysql.connect(host='localhost', port=3306, user='f14106155', passwd='0904', db='wordpress', charset='utf8')

with connect_db.cursor() as cursor:
    #建立資料表
    sql = """  
    CREATE TABLE IF NOT EXISTS 大台南公車轉運站資訊(
        項次 varchar(50),
        站名 varchar(50),
        地址 varchar(50),
        電話 varchar(50)
    );
    """
    cursor.execute(sql)  #執行SQL語法

    for i in range(len(list)):  #將資料庫數據新增至資料表中
        sq2 = "INSERT INTO 大台南公車轉運站資訊(項次, 站名, 地址, 電話)VALUES('"+ num[i] +"', '"+ pln[i] +"', '"+ adr[i] +"', '"+ tel[i] +"')"
        cursor.execute(sq2)  #執行SQL語法
    
    connect_db.commit()  #提交到資料庫內

connect_db.close()  #關閉連線



