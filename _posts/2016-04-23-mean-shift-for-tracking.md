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
```
Iteration : 1
Zeroth moment : 1020
First moments : 102510,102510
Center : 101,101
Location : 52,52,98,98
Iteration : 2
Zeroth moment : 689520
First moments : 86534760,86534760
Center : 126,126
Location : 77,77,98,98
Iteration : 3
Zeroth moment : 1511895
First moments : 208641510,208641510
Center : 138,138
Location : 89,89,98,98
Iteration : 4
Zeroth moment : 2019855
First moments : 290859120,290859120
Center : 144,144
Location : 95,95,98,98
Iteration : 5
Zeroth moment : 2301375
First moments : 338302125,338302125
Center : 147,147
Location : 98,98,98,98
Iteration : 6
Zeroth moment : 2449020
First moments : 363679470,363679470
Center : 149,149
Location : 100,100,98,98
```

![Mean Shift](https://raw.githubusercontent.com/arccoder/arccoder.github.io/master/blog/images/_posts/04_2016/meanshift.gif)

**Mean shift Example**

The image above shows how the mean shift converges to the center of the object location.

The mean shift algorithm would not converge if the object does not lie within the extended search window.
