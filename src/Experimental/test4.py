import cv2

img = cv2.imread(r'Assets\throwback.png',0)

ret, thresh = cv2.threshold(img,254,255,cv2.THRESH_BINARY_INV)

clicked =False
def callBack(event,x,y,param,flag):
    global clicked,img

    if event == cv2.EVENT_LBUTTONDOWN:
        print(img[y,x])


cv2.namedWindow('f')
cv2.setMouseCallback('f',callBack)


while 1:
    cv2.imshow('f',thresh)


    if cv2.waitKey(100) == 27 & 0xFF:
        break



cv2.imwrite(r'Assets\throwbackBIN.png',thresh)