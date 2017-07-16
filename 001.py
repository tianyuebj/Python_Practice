# -*- coding:utf-8 -*-

import uuid

#生成num个验证码，每个长度为length，可设置默认长度
def create_num(num,length=16):
    result=[]
    while num>0:
        #使用uuid.uuid4（）随机生成，目前看效果比 基于硬件地址和时间生成的uuid.uuid1()效果要好
        uuid_id=uuid.uuid4()
        #删去字符串中'-',取出前length个字符。对uuid4（）而言，不要[:length]会生成32长度的字符。
        temp=str(uuid_id).replace('-','')[:length]
        if temp not in result:
            result.append(temp)
            num -=1
    return result

print(create_num(200,4))
print(create_num(200))

"""
uuid是一种唯一标识，在许多领域作为标识用途。python的uuid模块就是用来生成它的。
闲话不说，python提供的生成uuid的方法一共有4种，分别是：
1.从硬件地址和时间生成
2.从md5算法生成
3.随机生成
4.从SHA-1算法生成
他们在uuid模块里对应uuid1, uuid3, uuid4, uuid5这几个方法，注意没有uuid2。
下面是示例： 

import uuid
print uuid.uuid1()
print uuid.uuid3(uuid.NAMESPACE_DNS, 'testme')
print uuid.uuid4()
print uuid.uuid5(uuid.NAMESPACE_DNS, 'testme')

"""

