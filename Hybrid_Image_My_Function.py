#Develop by - Kunal Khade
#Department of Electrical Engineering
#South Dakota School of Mines and Technology
#Class - Computer Vision
#Professor - Dr.Hoover
#Project - 1.2


#Task - Generate a hybrid image in the spatial domain. Can not use inbuilt function. 
#Approach - Import two images. Designed differnt kernels. Rotate different kernels on difeerent images.
#Combine the result and display 


import cv2
import numpy as np
import matplotlib.pyplot as plt 


input_image1 = cv2.imread('cat.bmp',1)  #for color = 1, for grayscale = 0
input_image2 = cv2.imread('dog.bmp',1)

  
def Gaussian_Kernel_Generate(kernlen, nsig):

    interval = (2*nsig+1.)/(kernlen)
    x = np.linspace(-nsig-interval/2., nsig+interval/2., kernlen+1)
    kern1d = np.diff(st.norm.cdf(x))
    kernel_raw = np.sqrt(np.outer(kern1d, kern1d))
    kernel = kernel_raw/kernel_raw.sum()
    return kernel


def My_Convolution(image_in, kernel, mode, boundry):
    #Parameters - Inpute Image, Kernel size, Mode, Boundry
    #Blur the input image using given kernel 
    #Only Odd size kernel supports
    #Mode and boundries are default 0 
    #Return - Updated image

    #Extract all image properties
    dimensions = image_in.shape
    length = len(dimensions)
    kernel1  = len(kernel)
    kernel_length = int((kernel1 - 1)/2)
    padding = kernel1 - 1

    #Kernel Size Check
    if (kernel1 % 2) == 0:
        return print("Invalid Kernel size. Please Enter correct kernel")
    
    if length == 3:

        color = cv2.split(image_in)
        #Saperate three differnet image plans and process individually 

        #Print all parameters
        print("The image has RGB planes")
        print("Dimensions - ",dimensions[0],'x',dimensions[1])
        print("Kernel Size -",kernel1)
        print("Mode - Default")
        print("Boundry - Default")

        #For Blue Image Plane
        kernel = np.flipud(np.fliplr(kernel))
        output1 = np.zeros_like(color[0])

        image_padded = np.zeros((image_in.shape[0]+padding, image_in.shape[1]+padding))
        image_padded[kernel_length:-kernel_length, kernel_length:-kernel_length] = color[0]

        for x in range(color[0].shape[1]):
            for y in range(color[0].shape[0]):
                output1[y, x] = (kernel * image_padded[y: y+kernel1, x: x+kernel1]).sum()
                
        #For Green Image Plane
        kernel = np.flipud(np.fliplr(kernel))
        output2 = np.zeros_like(color[1])

        image_padded1 = np.zeros((image_in.shape[0]+padding, image_in.shape[1]+padding))
        image_padded1[kernel_length:-kernel_length, kernel_length:-kernel_length] = color[1]

        for x in range(color[1].shape[1]):
            for y in range(color[0].shape[0]):
                output2[y, x] = (kernel * image_padded1[y: y+kernel1, x: x+kernel1]).sum()

        #For Red Image Plane
        kernel = np.flipud(np.fliplr(kernel))
        output3 = np.zeros_like(color[2])

        image_padded2 = np.zeros((image_in.shape[0]+padding, image_in.shape[1]+padding))
        image_padded2[kernel_length:-kernel_length, kernel_length:-kernel_length] = color[2]

        for x in range(color[2].shape[1]):
            for y in range(color[0].shape[0]):
                output3[y, x] = (kernel * image_padded2[y: y+kernel1, x: x+kernel1]).sum()        

        new_img = cv2.merge((output1 , output2 , output3))
        return new_img    
    
    elif length == 2:
        #For GreyScale
        print("The image is Greyscale")
        print("Dimensions - ",dimensions[0],'x',dimensions[1])
        print("Kernel Size -",kernel1)
        print("Mode - Default")
        print("Boundry - Default")
        kernel = np.flipud(np.fliplr(kernel))
        output = np.zeros_like(image_in)

        image_padded = np.zeros((image_in.shape[0]+padding, image_in.shape[1]+padding))
        image_padded[kernel_length:-kernel_length, kernel_length:-kernel_length] = image_in

        for x in range(image_in.shape[1]):
            for y in range(image_in.shape[0]):
                output[y, x] = (kernel * image_padded[y: y+kernel1, x: x+kernel1]).sum()
        return output    

#Kernels 
kernel1 = np.array([[1, 1, 1],
                   [1, 1, 1],
                   [1, 1, 1]]) / 9 

kernel7 = np.array([[1, 1, 1, 1, 1,1,1],
                    [1, 1, 1, 1, 1,1,1],
                    [1, 1, 1, 1, 1,1,1],
                    [1, 1, 1, 1, 1,1,1],
                    [1, 1, 1, 1, 1,1,1],
                    [1, 1, 1, 1, 1,1,1],
                    [1, 1, 1, 1, 1,1,1]])/49

kernel9 = np.array([[1, 1, 1, 1, 1,1,1,1,1],
                    [1, 1, 1, 1, 1,1,1,1,1],
                    [1, 1, 1, 1, 1,1,1,1,1],
                    [1, 1, 1, 1, 1,1,1,1,1],
                    [1, 1, 1, 1, 1,1,1,1,1],
                    [1, 1, 1, 1, 1,1,1,1,1],
                    [1, 1, 1, 1, 1,1,1,1,1],
                    [1, 1, 1, 1, 1,1,1,1,1],
                    [1, 1, 1, 1, 1,1,1,1,1],])/81

kernel15 = np.array([[1, 1, 1, 1, 1,1,1,1,1,1,1,1,1,1,1],
                    [1, 1, 1, 1, 1,1,1,1,1,1,1,1,1,1,1],
                    [1, 1, 1, 1, 1,1,1,1,1,1,1,1,1,1,1],
                    [1, 1, 1, 1, 1,1,1,1,1,1,1,1,1,1,1],
                    [1, 1, 1, 1, 1,1,1,1,1,1,1,1,1,1,1],
                    [1, 1, 1, 1, 1,1,1,1,1,1,1,1,1,1,1],
                    [1, 1, 1, 1, 1,1,1,1,1,1,1,1,1,1,1],
                    [1, 1, 1, 1, 1,1,1,1,1,1,1,1,1,1,1],
                    [1, 1, 1, 1, 1,1,1,1,1,1,1,1,1,1,1],
                     [1, 1, 1, 1, 1,1,1,1,1,1,1,1,1,1,1],
                     [1, 1, 1, 1, 1,1,1,1,1,1,1,1,1,1,1],
                     [1, 1, 1, 1, 1,1,1,1,1,1,1,1,1,1,1],
                     [1, 1, 1, 1, 1,1,1,1,1,1,1,1,1,1,1],
                     [1, 1, 1, 1, 1,1,1,1,1,1,1,1,1,1,1],
                     [1, 1, 1, 1, 1,1,1,1,1,1,1,1,1,1,1],])/225


kernel23 = np.array([[1, 1, 1, 1, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1, 1, 1, 1, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1, 1, 1, 1, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1, 1, 1, 1, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1, 1, 1, 1, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1, 1, 1, 1, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1, 1, 1, 1, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1, 1, 1, 1, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1, 1, 1, 1, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1, 1, 1, 1, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1, 1, 1, 1, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1, 1, 1, 1, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1, 1, 1, 1, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1, 1, 1, 1, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1, 1, 1, 1, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1, 1, 1, 1, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1, 1, 1, 1, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1, 1, 1, 1, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1, 1, 1, 1, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1, 1, 1, 1, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1, 1, 1, 1, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1, 1, 1, 1, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1, 1, 1, 1, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]])/529


#Pass two different from My_Convolution function
#Use different kernels for different images 
image_blur1 = My_Convolution(input_image1, kernel23,1 ,0)
image_blur2 = My_Convolution(input_image2, kernel23,1, 0)

#Add two images 
final = (image_blur1 -input_image1) + image_blur2  
image1 = cv2.resize(final,(180,205))

cv2.imshow('Hybrid_Image', final)
cv2.waitKey(0)
cv2.destroyAllWindows()