# Image Processing: Kernel Convolution

# Work still in progress



## Kernel convolution
The idea behind image processing with kernel convolution is to use a special matricial operation called _convolution_ which takes as input two matrices: a matrix of weights, which is the kernel, and the matrix of the RGB values of our image (in the range [0, 255]). The output will be a new image with pixel values moidfied according to the used kernel.  
For instance, supposing we use a 3x3 kernel matrix, the pixel RGB value at position [2,2] in the modified image will be calculates as  
<p align="center">
 <img src="https://github.com/dario-marvin/ImageProcessing-KernelConvolution/blob/master/formula1.png">
</p>
For edge and corner pixels, the idea is to locally overextend the image using the available pixels. For example the RGB value at position [1,1] is
<p align="center">
 <img src="https://github.com/dario-marvin/ImageProcessing-KernelConvolution/blob/master/formula2.png">
</p>

## Examples
### Simple blurring

Probably the most evident example of this technique is blurring. To achieve this effect, we use a Kernel matrix given by
<p align="center">
  <img width=200 src="https://github.com/dario-marvin/ImageProcessing-KernelConvolution/blob/master/blur.png">
</p>
which means that every pixel is the calibrated mean of the 9 neighbours surrounding it.  

<p align="center">
  <img src="https://github.com/dario-marvin/ImageProcessing-KernelConvolution/blob/master/rubik_Blur.jpg">
</p>

### Gaussian blurring

The gaussian blurring effect is obtained by employing a matrix where the values are not constant as in the previous example, but are chosen according to the Gaussian distribution with regard to the vertical and horizontal distance between each surrounding pixel and the central one. In this example we consider a 13x13 kernel matrix, thus the image appears more "smoothed" than the preceeding one.

<p align="center">
  <img src="https://github.com/dario-marvin/ImageProcessing-KernelConvolution/blob/master/rubik_Gaussian_blur.jpg">
</p>

### Edge detection

When performing edge detection, we want to highlight those pixels whose neighbours are not regular. Or, equivalently, we want to dampen those pixels who are equals in value to the immediately close ones. Thus we consider a Kernel matrix given by
<p align="center">
  <img width=200 src="https://github.com/dario-marvin/ImageProcessing-KernelConvolution/blob/master/edgeDetect.png">
</p>
Notice that by doing so, if the central pixel and the 8 surrounding ones have all the same value, the resulting pixel will have value 0, hence it will be black.

<p align="center">
  <img src="https://github.com/dario-marvin/ImageProcessing-KernelConvolution/blob/master/rubik_Edge_detection.jpg">
</p>

## Applications

## How to compile and execute the files
