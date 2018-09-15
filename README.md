# Image Processing: Kernel Convolution

# Work still in progress

## Kernel convolution
The idea behind image processing with kernel convolution is to use a special convolution operation between the kernel, a matrix of weights, and the matrix of the image, containing its pixel values in the range [0, 255].  
For instance, if we use a 3x3 kernel matrix and for simplicity a 3x3 pixel image, the central pixel of the modfiied image will be evaluated as
<p align="center">
 <img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/570600fdeed436d98626278f22bf034ff5ab5162">
</p>
For edge and corner pixels, the idea is to locally overextend the image using the available pixels. Visit the

[wikipedia page](https://en.wikipedia.org/wiki/Kernel_(image_processing))
on the subject for more information.

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
