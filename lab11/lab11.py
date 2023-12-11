#coding=utf-8

# https://data.gov.tw/dataset/166167

import pymysql.cursors
import requests
import json

#GET API data
test = requests.get("https://soa.tainan.gov.tw/Api/Service/Get/1e236a7d-9c44-4809-888c-9a04cd5375d7")
r = json.loads(test.text)

#Connect to the database
try:
    connection = pymysql.connect(host='localhost', 
                                 user='e94121119',      
                                 password='0000', 
                                 database='wordpress',    
                                 cursorclass=pymysql.cursors.DictCursor)
    print("connected success")     
except Exception as error: 
    print(error)


with connection:
    with connection.cursor() as cursor:

        
        
        sql = "INSERT INTO `臺南市112年住宅價格月指數` (`類別`, `住宅價格月指數`, `月變動率`, `季變動率`) VALUES (%s, %s, %s, %s)"
        for i in range( len( r['data']  )):
            cursor.execute(sql, ( r['data'][i]['類別'],r['data'][i]['住宅價格月指數'],r['data'][i]['月變動率'],r['data'][i]['季變動率']))

    connection.commit()
    cursor.close()
