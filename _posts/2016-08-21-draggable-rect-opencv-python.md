---
layout: post
title: Draggable rectangle in opencv (Python)
category: Tech
tags: [opencv, python]
---

If you use [opencv](http://opencv.org/) then you probabaly are interested in computer vision and image processing. Many times you need a area or a region on an image as a starting value or region of interest. For instance, while collecting data for object detection you might want to known the location of the object on the image which can be used as ground truth for calculating the accuracy of the classification algorithm. Another instance is if you want to provide a seed region for a tracking algorithm. In such scenarios, it is very useful if this region selection can be accompolished by a simple user interface preferably by dragging a rectangle on the image.

I have already implemented a rectangle dragging algorithm in javascript '[selectincanvas](https://github.com/arccoder/selectincanvas.js)'. Here I have implemented the same algorithm using opencv in python. Some time back I learned about the Opencv's [User Interface](http://docs.opencv.org/2.4/modules/highgui/doc/user_interface.html) module and I always wanted a quick way of dragging a rectangle on an image using opencv. I was finally able to implement draging and adjusting a rectangle on an image window within opencv and get the coordinates of the rectangle.

![Preview gif](https://cdn.rawgit.com/arccoder/opencvdragrect/master/preview.gif "Preview Image")

The implementation and the documentation can be found in this repo(https://github.com/arccoder/opencvdragrect).

One issue I faced with the python implementation is that if you drag the rectangle for a long time then the stack overflows. I implemented this in python but this can also be implemented in c++.
