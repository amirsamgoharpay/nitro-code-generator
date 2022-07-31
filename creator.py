import random
import time
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz"
check = True
code = ""
cho = 0
print("starting...")
while check:
        try:
                for i in range(16):
                        code =code + random.choice(chars)
                #print(code) this line prints the codes that are generated (its kinda annoying)
                with open("code.txt" ,"a") as f:
                        f.write(f"{code}\n")
                time.sleep(0.001) 
                code = ""
        except KeyboardInterrupt as error :
                print("codes are saved in code.txt")
                exit()

