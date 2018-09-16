# Image Processing: Kernel Convolution

# Work still in progress



## Kernel convolution
The idea behind image processing with kernel convolution is to use a special matricial operation called _convolution_ which takes as input two matrices: a matrix of weights, which is the kernel, and the matrix of the RGB values of our image (in the range [0, 255]).  
For instance, supposing we use a 3x3 kernel matrix, the pixel RGB value at position [2,2] in the modified image will be calculates as  
<p align="center">
 <img src="https://github.com/dario-marvin/ImageProcessing-KernelConvolution/blob/master/formula1.png">
</p>
For edge and corner pixels, the idea is to locally overextend the image using the available pixels, that is we calculate 
<p align="center">
 <img src="https://github.com/dario-marvin/ImageProcessing-KernelConvolution/blob/master/formula2.png">
</p>
Visit the dedicated  



[wikipedia page](https://en.wikipedia.org/wiki/Kernel_(image_processing))  





for more information on how to handle corner cases.

## Examples

<p align="center">
  <img src="https://github.com/dario-marvin/ImageProcessing-KernelConvolution/blob/master/rubik_Blur.jpg">
</p>
<p align="center">
  <img src="https://github.com/dario-marvin/ImageProcessing-KernelConvolution/blob/master/rubik_Gaussian_blur.jpg">
</p>
<p align="center">
  <img src="https://github.com/dario-marvin/ImageProcessing-KernelConvolution/blob/master/rubik_Edge_detection.jpg">
</p>

## Applications

## How to compile and execute the files
