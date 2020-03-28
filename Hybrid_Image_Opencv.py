#Develop by - Kunal Khade
#Department of Electrical Engineering
#South Dakota School of Mines and Technology
#Class - Computer Vision
#Professor - Dr.Hoover
#Project - 1


#Task - Generate a hybrid image in the frequency domain. Allow using the inbuilt library (Opencv)
#Approach - Import two images. Convert into the frequency domain using FFT. Implement highpass and low pass filter on each image. 
#Combine both the images and generate a hybrid image. To get better results tune cutoff frequency. 



import numpy as np
import cv2
from matplotlib import pyplot as plt

#Two different frequency cutoffs
lpf_constant = 10  #Low Pass Frequency Cut off
hpf_constant = 1   #High Pass Frequency Cut off 

#Read Images from given dataset 
img1 = cv2.imread('cat.bmp',1)
img2 = cv2.imread('dog.bmp',1)

#Convert images into grayscale 
image1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
image2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

#Convert both the images into frequency domain 
dft1 = cv2.dft(np.float32(image1),flags = cv2.DFT_COMPLEX_OUTPUT)
dft2 = cv2.dft(np.float32(image2),flags = cv2.DFT_COMPLEX_OUTPUT)

#Add FFT Shift 
dft_shift1 = np.fft.fftshift(dft1)
dft_shift2 = np.fft.fftshift(dft2)

#Take magnitude spectrum of images
magnitude_spectrum1 = 20*np.log(cv2.magnitude(dft_shift1[:,:,0],dft_shift1[:,:,1]))
magnitude_spectrum2 = 20*np.log(cv2.magnitude(dft_shift2[:,:,0],dft_shift2[:,:,1]))

#Extract dimensions of images
dimensions = image1.shape
rows1 = dimensions[0]
cols1 = dimensions[1]
crow1,ccol1 = rows1//2 , cols1//2
crow2,ccol2 = rows1//2 , cols1//2

# Create a mask first, center square is 1, remaining all zeros
mask1 = np.zeros((rows1,cols1,2),np.uint32)

##filterout all other frequency which is not in the mask
mask1[crow1-lpf_constant:crow1+lpf_constant, ccol1-lpf_constant:ccol1+lpf_constant] = 1   #LPF
dft_shift2[crow2-hpf_constant:crow2+hpf_constant, ccol2-hpf_constant:ccol2+hpf_constant] = 0   #HPF

# Apply mask and inverse DFT on different image
fshift1 = dft_shift1 * mask1
fshift2 = dft_shift2

#Take inverse fourier transform from resultant signals
f_ishift1 = np.fft.ifftshift(fshift1)
f_ishift2 = np.fft.ifftshift(fshift2)

img_back1 = cv2.idft(f_ishift1)
img_back2 = cv2.idft(f_ishift2)

img_back1 = cv2.magnitude(img_back1[:,:,0],img_back1[:,:,1])
img_back2 = cv2.magnitude(img_back2[:,:,0],img_back2[:,:,1])

#combine both images and get the result 
new_image = img_back1 + img_back2  #Hybrid Image

#Plot all images 
f, axarr = plt.subplots(2,3)
axarr[0,0].imshow(image1, cmap = 'gray')
axarr[0,0].set_title('Input_Image_1')
axarr[0,1].imshow(magnitude_spectrum1, cmap = 'gray')
axarr[0,1].set_title('Magniture_Spectrum_Image1')
axarr[0,2].imshow(img_back1, cmap = 'gray')
axarr[0,2].set_title('Image1_after_IFT')

axarr[1,0].imshow(image2, cmap = 'gray')
axarr[1,0].set_title('Input_Image_2')
axarr[1,1].imshow(magnitude_spectrum2, cmap = 'gray')
axarr[1,1].set_title('Magniture_Spectrum_Image2')
axarr[1,2].imshow(img_back2, cmap = 'gray')
axarr[1,2].set_title('Image2_after_IFT')

#Display image plot
plt.show()
plt.imshow(new_image, cmap = 'gray')
plt.title('Hybrid Image'), plt.xticks([]), plt.yticks([])
plt.show()
