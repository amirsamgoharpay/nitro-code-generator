import requests
import random
import json
import time
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz"
check = True
code = ""
cho = 0
while check:
        for i in range(16):
                code =code + random.choice(chars)
        res = requests.get(f"https://discord.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true")
        res = res.json()
        #if res["message"] == "The resource is being rate limited." :
                #print("this proses after 1 min")
        if res["message"] == "Unknown Gift Code" :
                print(f"{code} was invalid")
        else :
                print(res["message"])
                print(code)
        dic = {"message" : res["message"],
                "code" : code}
        with open("codes.txt" ,"a") as f:
                f.write(f"{dic}\n")
                #json.dump(dic , f)
        time.sleep(12)



        code = ""
