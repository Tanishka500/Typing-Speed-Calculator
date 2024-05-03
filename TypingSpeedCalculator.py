from time import *
import random as r

def mistake(partest,usertest):
    error = 0
    for i in range(len(partest)):
        try: 
            if partest[i] != usertest[i]:
                error = error + 1
        except :
            error = error + 1
    return error

def speed_time(time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay,2)
    speed = len(userinput)/time_R
    return round(speed)

while True:
    ck = input("Ready to test : Yes / No :- ")
    if ck == "Yes" :
        test = ["Any instruction written in the source code and executed by the Python interpreter is called a statement.",
            "The Python language has many different types of statements like assignment statements, conditional statements, looping statements, etc.,",
            "that help a programmer get the desired output."]
        test1 = r.choice(test)
        print("***Typing Speed Calculator***")
        print(test1)
        print()
        print()
        time_1 = time()
        testinput = input("Enter : ")
        time_2 = time()

        print('Speed : ',speed_time(time_1,time_2,testinput),"w/sec")
        print("Error : ",mistake(test1,testinput))
    elif ck == "No" :
        print("ThankYou visit again :)")