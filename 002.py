# -*- coding:utf-8 -*-

#将001中随机生成的验证码保存到MySQL数据库
import uuid
import pymysql

#生成num个验证码，每个长度为length，可设置默认长度
def create_num(num,length=16):
    result=[]
    while num>o:
        uuid_id=uuid.uuid4()
        #删除字符串中的'-'，取出前length个字符
        temp=str(uuid_id).replace('-','')[:length]
        if temp not in result:
            result.append(temp)
            num -=1
    return result


#保存到MySQL数据库
def save_to_mysql(code):
    conn=pymysql.connect(host='127.0.0.1',
                         port=3306,
                         user='root',
                         password=None,
                         db='test')

    try:
        with conn.cursor() as cursor:
            #创建一个新记录
            sql="INSERT INTO 'codes'('code') VALUES(%s)"
            cursor.execute(sql,code)

        #记录不是默认提交的，所以要记着提交你的修改
        conn.commit()

        with conn.cursor() as cursor:
            #阅读单个记录
            sql="SELECT 'id','code' FROM 'codes' WHERE 'code'=%s"
            cursor.execute(sql,code)
            result=cursor.fetchone()
            print(result)

    finally:
        conn.close()
for code in create_num(200):
    save_to_mysql(code)

