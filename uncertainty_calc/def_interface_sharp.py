import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
#x=np.linspace(0,200,200)
#phi=np.zeros((2000,2000))
phi=np.zeros((200,200))
for i in range(100,200):
    for j in range(200):
         phi[i,j]=1

phi=(phi-phi.min())/(phi.max()-phi.min()) #to normalize
phi = (phi*255).astype(np.uint8)
phi_v= phi.transpose() # gradient along x
#phi = cv2.cvtColor(phi, cv2.COLOR_GRAY2RGB)
img = Image.fromarray(phi_v,'L').convert('RGB')
#img.save('sharp_edge.png')
#img.show()

#intensity profile plot
#plt.plot(phi[:,100])
#plt.show()



#calculating gradient in horizontal direction(change in column values)
grad=np.zeros((200,199))
for i in range (200):
    for j in range(199):
        grad[i,j]=(phi_v[i,j+1]-phi_v[i,j])
    
#print(phi[100:150,100:150],grad[:,:])
#print(np.where(np.max(grad[:,:])))
#grad=(grad*255).astype(np.uint8)

img1 = Image.fromarray(grad.astype(np.uint8)).convert('L')
img1.save('sharp_gradient_image.png')
plt.plot(grad[100,:])
plt.show()
