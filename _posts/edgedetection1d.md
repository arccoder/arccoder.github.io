---
layout: post
title: Edge detection explained in 1D
category: Tech
tags: [Matlab]
---


![filter][I1]

Fig 1: Gaussian filter

![dfilter][I2]

Fig 2: First order derivative of a gaussian filter

![d2filter][I3]

Fig 3: Second order derivative of a gaussian filter

![signal][I4]

Fig 4: 1D signal denoting a edge

![convdatafilter][I5]

Fig 5: Filter shown in Fig 1 convolved with signal shown in Fig 4

![dconvdatafilter][I6]

Fig 6: Derivative of the signal shown in Fig 5

![convdatadfilter][I7]

Fig 7: Filter shown in Fig 2 convolved with signal shown in Fig 4

![convdatad2filter][I8]

Fig 8: Filter shown in Fig 3 convolved with signal shown in Fig 4

Matlab code to generate the signals above can be found [here](L1).

[I1]: /resources/posts/01_2017/filter.png
[I2]: /resources/posts/01_2017/dfilter.png
[I3]: /resources/posts/01_2017/d2filter.png

[I4]: /resources/posts/01_2017/signal.png
[I5]: /resources/posts/01_2017/convdatafilter.png
[I6]: /resources/posts/01_2017/dconvdatafilter.png

[I7]: /resources/posts/01_2017/convdatadfilter.png
[I8]: /resources/posts/01_2017/convdatad2filter.png

[L1]: https://gist.github.com/arccoder/c5c0818acebc588d84392c3a20743076
