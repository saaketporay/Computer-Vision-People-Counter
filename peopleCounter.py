import sys,os
sys.path.append(os.path.join(os.getcwd(),'python/'))
import cv2
import time
import darknet

config_file = './cfg/yolov3.cfg'
#config_file = './cfg/yolov3-tiny.cfg'
weights = './weights/yolov3.weights'
net = darknet.load_net(config_file,"yolov3.weights",0)
meta = darknet.load_meta("cfg/coco.data")

cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    cv2.imwrite("/home/jay/Documents/hackathon/inputFiles/input.jpg",frame)
    r = darknet.detect(net,meta,"/home/jay/Documents/hackathon/inputFiles/input.jpg")
    a = r[0]
    people = 0
    for i in r:
        a = i[0]
        print a
        if(a=="person"):
            people+=1
    print people
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.imread("/home/jay/Documents/hackathon/inputFiles/input.jpg")
    b = "People:"+ str(people)
    cv2.putText(img,b,(130,150), font, 1,(0,255,0),2,cv2.LINE_AA)
    cv2.imshow('frame',img)

    if cv2.waitKey(1)&0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
