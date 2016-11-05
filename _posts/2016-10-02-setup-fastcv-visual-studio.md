---
layout: post
title: Setup FastCV on Visual Studio 2010
description: Steps to setup FastCV 1.7.1 on Visual Studio 2010 Express
category: Tech
tags: [fastcv, visual studio, opencv]
---

Qualcomm's [FastCV SDK](https://developer.qualcomm.com/software/fastcv-sdk) is a mobile-optimized computer vision library which offers a wide range functionality. It is specially optimized for [Qualcomm's snapdragon processor](https://developer.qualcomm.com/hardware/which-processor). Today we will go through the steps to use FastCV 1.7.1 on windows using Visual Studio 2010 Express.

First you need to download the SDK using the following [link](https://developer.qualcomm.com/software/fastcv-sdk). You would be required to create an developer account to download the library. After downloading the library (zip file), extract it and run the excutable. Complete the installation process. Once the installation is complete, in the installation directory you will find an include folder (_inc_) and a library folder (_lib_). Within the _lib_ folder there are folders containing pre-compiled libraries for _Andriod_, _VS2010_, _VS2012_, and _VS2013_.

As I using VC++ 2010 Express, I shall be using the _libfastcv.lib_ in the MD folder within the _VS2010_ folder. The libraries are complied in 2 different ways for each of the visual studio version, [MD and MT](https://msdn.microsoft.com/en-us/library/2kzt1wy3(v=vs.100).aspx). You may use the libray the fits your needs.

Now create an empty C++ project in visual studio and include the paths for header and libs in the project properties as shown in the images below.

![Include Directories](https://cdn.rawgit.com/arccoder/arccoder.github.io/master/blog/images/_posts/10_2016/fastcvsetup1.JPG)
![Library Directories](https://cdn.rawgit.com/arccoder/arccoder.github.io/master/blog/images/_posts/10_2016/fastcvsetup2.JPG)
![Additinal Dependencies](https://cdn.rawgit.com/arccoder/arccoder.github.io/master/blog/images/_posts/10_2016/fastcvsetup3.JPG)

We are almost there. Create a source file with the following code in it.

```cpp
#include "fastcv.h"

int main()
{
    // FastCV - Initialization process
    fcvOperationMode mode = FASTCV_OP_CPU_PERFORMANCE;
    FASTCV_API int fcvSetOperationMode( mode );
    
    // FastCV - De-initialization process
    FASTCV_API void fcvCleanUp();
    
    return 0;
}
```

Build and run the code. You are now ready to explore FastCV's functionality on windows.

The setup process described here should be vary similar if you use a different version of visual studio.

------

Note: 

In the above images you will also see OpenCV included and libraries added. I am using OpenCV 2.4.9 and its the last version of OpenCV that coes with prebuild VS2010 libraries.

FastCV does not provide a way to read images. So I use opencv to read and display images and FastCV to process them.


