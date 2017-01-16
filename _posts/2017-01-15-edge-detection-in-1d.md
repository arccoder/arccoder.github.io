---
layout: post
title: Edge detection explained in 1D
category: Tech
tags: [Code, Matlab, Computer-Vision]
---

This post is inspired after watching edge detection (2A-L5,2A-L6) related lectures in the [Introduction to Computer Vision][L2] course on Udacity.
Here I have implemented the real world example shown in the using a 1D toy example.

Edges are the most basic and widely used features used in computer vision.
Edges are formed when there is a steep change in the color or intensiy values in the image.
To capture these high differnce ridges we can make use of differential opeartors to create masks that computer gradients.

Real world images or signals are never completelty noise free so first we need to smooth the signal using a low pass filter.
In this case we have choosen a gausian filter as shown in Fig 1. (This post only implements 1D signal but the same logic can be extended to 2D signals.)

![filter][I1]

<center>Fig 1: Gaussian filter</center>

Because filtering or convolution is a linear operator, using the associative property of linear operators
we can take derivatives of the filter and apply it directly to the signal
rather than taking the derivative of the convolved signal and the filter.

Fig 2 shows the first derivative of the gaussian filter and the second derivative is shown in Fig 3.

![dfilter][I2]

<center>Fig 2: First derivative of a gaussian filter</center>

![d2filter][I3]

<center>Fig 3: Second derivative of a gaussian filter</center>

The first order derivative will give the signal which peaks at the location of the largest gradient.
But then we need to find the location of the peak to get the edge location.
For that we can take another derivative and the location at which the signal crosses over zero thats the location of the peak.

No we apply the filters to the signal shown in Fig 4 with some noise added to it.

![signal][I4]

<center>Fig 4: 1D signal denoting a edge</center>

The figures 5, 7, and 8 show the output after been convoluted by the filters shown in figures 1, 2, and 3 respectively.

![convdatafilter][I5]

<center>Fig 5: Filter shown in Fig 1 convolved with signal shown in Fig 4</center>

Fig 6 shows the output after taking the first derivative of the signal in Fig 5.

![dconvdatafilter][I6]

<center>Fig 6: Derivative of the signal shown in Fig 5</center>

![convdatadfilter][I7]

<center>Fig 7: Filter shown in Fig 2 convolved with signal shown in Fig 4</center>

The output signals in figures 6 and 7 are equal. The only difference is the sequence in which the differentiation and convolution is applied.

![convdatad2filter][I8]

<center>Fig 8: Filter shown in Fig 3 convolved with signal shown in Fig 4</center>

Matlab code to generate the signals above can be found [here][L1].

[I1]: /resources/posts/01_2017/filter.png
[I2]: /resources/posts/01_2017/dfilter.png
[I3]: /resources/posts/01_2017/d2filter.png

[I4]: /resources/posts/01_2017/signal.png
[I5]: /resources/posts/01_2017/convdatafilter.png
[I6]: /resources/posts/01_2017/dconvdatafilter.png

[I7]: /resources/posts/01_2017/convdatadfilter.png
[I8]: /resources/posts/01_2017/convdatad2filter.png

[L1]: https://gist.github.com/arccoder/c5c0818acebc588d84392c3a20743076
[L2]: https://www.udacity.com/course/introduction-to-computer-vision--ud810
