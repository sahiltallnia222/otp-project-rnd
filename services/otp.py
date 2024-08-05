import base64
import time
 
import pyotp
 
 
def generateOTP(secret):
    totp = pyotp.TOTP(s=secret,digits=6,interval=20)
    return totp.now()
 
def verifyOTP(secret,otp):
    totp = pyotp.TOTP(secret, digits=6, interval=20)  # Set interval to 60 seconds
    if totp.verify(otp):
        return True
    else:
        return False
 
def derive_secret(mobile_number):
    secret_base32 = base64.b32encode(f'{mobile_number}'.encode()).decode('utf-8')
    return secret_base32
 
# secret=derive_secret(9175743910,20) 
# print(secret)# ye kaam har time hash(mobileno,window time)->otp
# otp=generateOTP(secret) #hash(mobileno,window time)->gener
# print(otp)
secret=derive_secret(9175743911) 
print(secret)
otp=generateOTP(secret)
print(otp)
print(verifyOTP(secret,otp))
time.sleep(5)
secret=derive_secret(9075743911)
print(secret)
otp2=generateOTP(secret)
print(otp2)
print(verifyOTP(secret,otp))
 
time.sleep(30)
 
secret=derive_secret(9175743911)
print(secret)
otp3=generateOTP(secret)
print(otp3)
print(verifyOTP(secret,otp2))