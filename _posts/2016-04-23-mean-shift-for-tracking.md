---
layout: post
title: Mean shift for tracking
category: Tech
tags: [object-tracking, mean-shift]
---

Here I want to show how mean shift is used for tracking. The camshift algorithm for tracking first showed how mean shift can be applied for tracking faces. 

An object tracking algorithm works on two modules, one is matching the objects characteristics from the previous frame/loaction to the current and the second to define and assist to locate and measure the size of the object. 

Camshift uses a probability mask generated from the hue channel of HSV image. They choose hue channel because it remains same irrespective of the saturation (skin tone), which works well for skin detection. Mean shift is used to find the location of the object, mainly the center (mean) using moments.

In this post, I am using a toy example to show how mean shift finds the center location of the objet. I have used a binary image, the matching region is denoted by ones and zeros else where. The code and the output is shown below. 

<script src="https://gist.github.com/arccoder/22d0b9feb71a8ad3958a3811d1bed0b6.js"></script>

**Output**

<script src="https://gist.github.com/arccoder/eaa12b2f54f301c3b4aa5de3f51cc97c.js"></script>

![Mean Shift](https://raw.githubusercontent.com/arccoder/arccoder.github.io/master/blog/images/_posts/04_2016/meanshift.gif)

**Mean shift Example**

The image above shows how the mean shift converges to the center of the object location.

The mean shift algorithm would not converge if the object does not lie within the extended search window.
