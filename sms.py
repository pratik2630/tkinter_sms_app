import re
import os
from dotenv import load_dotenv
load_dotenv()
import vonage
import time


From = input("Enter your number:")
fileName = input("Enter Phone number file name: ")
msg = input("Enter message to sent:")

file = open(fileName,"r")

text = file.read()
delay = input("enter delay:")
def convert_phone_number(phone):
  result = re.sub(r'(?<!\S)(\d{3})-(\d{3})-(\d{4}\b)', r'\1\2\3', phone)
  return result
  
#pattern matching from file to match numbers
pattern = r"\d{3}\-\d{3}\-\d{4}"
phone_numbers = re.findall(pattern , text)

for i in range(len(phone_numbers)):
    # print(convert_phone_number(phone_numbers[i]))
    print("phone numbers",phone_numbers[i])
    converted_num = convert_phone_number(phone_numbers[i])
    print(converted_num)

#importing key and secret from .env
nkey = os.getenv("key")
nsecret = os.getenv("secret")


#function for sending message
def Text_SMS(num, msg):
    time.sleep(int(delay))
    responseData = sms.send_message({
        'from': From,
        'to': num,
        'text': msg,
        'type': "unicode"
    })
    
    if responseData["messages"][0]["status"] == "0":
        print("Message sent successfully to",num)
    else:
        print(f"Message failed with error: {responseData['messages'][0]['error-text']}")



client = vonage.Client(key= nkey, secret= nsecret)
sms = vonage.Sms(client)



#Iterating through given numbers and sending message
for i in range(len(phone_numbers)):
    print(phone_numbers[i])
    Text_SMS(str(phone_numbers[i]), msg)
    #pass