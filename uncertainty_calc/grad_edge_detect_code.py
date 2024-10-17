import numpy as np
import matplotlib.pyplot as plt
import cv2
from PIL import Image
image_path = 'bike.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
#print(image.shape)
gx=np.array([[1,0],[0,-1]])
gy=np.array([[0,1],[-1,0]])


#sobel operator
#gx=np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
#gy=np.array([[1,2,1],[0,0,0],[-1,-2,-1]])


(imH,imW)=image.shape
kH=gx[1].size
kW=gx[0].size
edge_image=np.zeros(image.shape)
new_img=np.zeros(image.shape)
pad=int((kH-1)/2)
print(kH,kW)
for y in range (imH-kH+1):
    for x in range (imW-kW+1):
        new_img[y+pad,x+pad] = (((gx*image[y:y+kH,x:x+kW]).sum())**2+((gy*image[y:y+kH,x:x+kW]).sum())**2)**0.5
        if( new_img[y+pad,x+pad]>50):  #thresholding
            edge_image[y,x]= new_img[y+pad,x+pad]
print(edge_image[0,0],new_img[0,0],np.max(new_img))
edge_image=edge_image.astype(np.uint8)
plt.title('Edge-detected image with threshold = 50')
plt.imshow(edge_image,cmap='gray')
plt.show()


#example of convolution
img=np.array([[3,0,1,2,7,4],[1,5,8,9,3,1],[2,7,2,5,1,3],[0,1,3,1,7,8],[4,2,1,6,2,8],[2,4,5,2,3,9]])
kernel=np.array([[1,0,-1],[1,0,-1],[1,0,-1]])
new_img=np.zeros(img.shape)
(imH,imW)=img.shape
kH,kW=kernel.shape
p=int((kH-1)/2)
#padded_img=np.zeros((imH+kH,imW+kW))
#padded_img[p:p+imH,p:p+imW]=img
#print(padded_img)

for y in range(imH-kH+1):
    for x in range(imH-kH+1):
        new_img[y+p,x+p]=(kernel*img[y:y+kH,x:x+kW]).sum()

#print(new_img)
