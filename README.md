# Image-Segmentation

 This is an application using python OpenCV that processes images with background into output images with white background. In order to achieve the output, we used the adaptive threshold method that implements segmentation, median blur as pre-processing and post processing method, and erosion.

 ![image](https://github.com/tengkoku/Image-Segmentation/assets/148973550/02e582d5-a55d-464d-b0e2-6bbb39e96614)

 Median blur: used to smoothen the image before the segmentation. It is also used after the segmentation to get rid of the apparent noise of the resulting images. 
 Adaptive Gaussian threshold: implement segmentation to partition an image. The image’s threshold value is calculated for smaller regions and therefore, there will be different threshold values for different regions
 Erosion: Used to structure the image where it shrinks the foreground image and enlarges the background image. This will result in a readable output image.

![image](https://github.com/tengkoku/Image-Segmentation/assets/148973550/9ddf7575-1c86-4d17-b02b-098d8acbbff9)
![image](https://github.com/tengkoku/Image-Segmentation/assets/148973550/aa91de28-4b16-4be7-a141-378fe732d233)
![image](https://github.com/tengkoku/Image-Segmentation/assets/148973550/d74bf19b-0ef5-4288-874a-848b93da49be)

 Mask 3 is the most suitable for a fair background that contrasts with the foreground. The higher the number of segmentation masks, the more pixels will be isolated. Images with shadows at the background and 
 different pixels that make it hard to segment. Therefore, the suitable segmentation masks for these images are 5.
