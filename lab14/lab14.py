import cv2
import numpy as np


#原始照片
image = cv2.imread("TW.jpg", 1)  #讀取圖片
cv2.imshow("TW", image)    #顯示圖片


#使用函式灰階照片
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)    #把image這個檔案從BGR轉成灰階，放到gray這個變數
cv2.imshow("gray", gray)  #顯示圖片


#不使用函式灰階照片
imgInfo = image.shape  
height = imgInfo[0]  #圖像的高度
width = imgInfo[1]   #圖像的寬度

dst = np.zeros((height, width, 3), np.uint8)  #建立三維陣列
for i in range(0,height):
    for j in range(0,width):

        (b, g, r) = image[i, j]
        gray1 = (int(b) + int(g) + int(r)) / 3  #將RGB3個維度的數相加除以3
        dst[i, j] = np.uint8(gray1)

cv2.imshow('gray1',dst)  #顯示圖片


#二值化照片
ret, output = cv2.threshold(gray, 245, 255, cv2.THRESH_BINARY)     # 如果大於 245 就等於 255，反之等於 0。
cv2.imshow('binary', output)  #顯示圖片


cv2.waitKey(0)             #等待 enter被按下
cv2.destroyAllWindows()    #關閉opencv開啟的視窗