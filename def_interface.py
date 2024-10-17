#import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
x=np.linspace(-np.pi,np.pi,40000)
phi=np.sinh(x)/np.cosh(x)
phi=np.reshape(phi,(200,200))
#print(phi[0,0])
#img_w,img_h=200,200
#data=np.zeros((img_h,img_w,3),dtype=np.uint8)

#for i in range (20):
#    for j in range (20):
#        if phi[i,j]<0:
#            data[i,j]=[255,0,0]
#            #print(i,j)
#        else:
#            data[i,j]=[0,255,0]
            #print(i,j)
#img = Image.fromarray(data,'RGB')
phi=(phi-phi.min())/(phi.max()-phi.min()) #to normalize
phi = (phi*255).astype(np.uint8)
#phi = cv2.cvtColor(phi, cv2.COLOR_GRAY2RGB)
img = Image.fromarray(phi.transpose(), 'L').convert('RGB')
#img.save('diffuse_res_high.png')
#img.show()
#plt.plot(phi[:,100])
#plt.show()
phi_v=phi.transpose()
grad=np.zeros((200,200))
for i in range (200):
    for j in range(1,199):
        grad[i,j]=(phi_v[i,j+1]-phi_v[i,j-1])

#print(phi[100:150,100:150],grad[:,:])
#print(np.where(np.max(grad[:,:])))
#grad=(grad*255).astype(np.uint8)
print(phi_v[100,30:50],grad[100,30:50])
img1 = Image.fromarray(grad.astype(np.uint8)).convert('L')
img1.show()
#img1.save('diffuse_gradient_image.png')
#plt.plot(grad[100,:])
#plt.show()
#print(x)
