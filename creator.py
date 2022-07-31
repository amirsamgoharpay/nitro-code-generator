import random
import time
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz"
check = True
code = ""
cho = 0
while check:
        for i in range(16):
                code =code + random.choice(chars)
        print(code)
        with open("codes.txt" ,"a") as f:
                f.write(f"{code}\n")
        time.sleep(0.001) 



        code = ""
