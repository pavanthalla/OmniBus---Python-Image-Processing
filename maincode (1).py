import os
import message
import processing
import time
def assign(route_path):
    num=0
    for f in os.listdir(route_path):
        # img_path=os.path.join(route_path,f)
        num += processing.process()
        # os.remove(img_path)
    return num
def main():
    dict1={}
    path=r'C:\Users\pradyumna\Desktop\omnibus'
    for l in os.listdir(path):
        dict1[l]=0
    while(1):
        for l in os.listdir(path):
            elapse_time=time.time()-dict1[l]
            if(dict1[l]>0 and elapse_time>30):
                print(time.time())
                dict1[l]=0
                num=assign(route_path)
            elif(dict1[l]==0):
                route_path=os.path.join(path,l)
                num=assign(route_path)
                if(num>=30):
                    message.sendmessage(l[5:])
                    dict1[l]=time.time()
main()