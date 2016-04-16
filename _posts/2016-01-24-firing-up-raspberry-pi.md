---
layout: post
title: Firing Up Raspberry Pi
category: Tech
tags: [raspberry-pi, setup, unbox, boot]
---

Just got a Raspberry Pi 2 Model B to get my hands on some embedded system development.

Things that you need to get started :
1. Raspberry Pi (Rpi)
2. Micro SD card and with a reader
3. HDMI cable
4. Ethernet cable
5. Wired keyboard and mouse
6. Cell phone charger with micro USB connector (5V - 700mA)

Before unboxing the Rpi you need to load the operating system on the micro SD card. You can buy micro SD cards that comes preloaded with an operating system, but I am taking this up as a DIY project.

### Step 1: Download the operating system

I downloaded the Raspbian image RASPBIAN JESSIE from [Ref1]([Ref]). The only reason i downloaded the Raspbian image is because the first link of the page says 
> Raspbian is the Foundation’s official supported Operating System.
> ---<cite>[Ref1]

Unzip the file.

### Step 2: Download Win32DiskImager and run it.

I am using a windows 7 system and I followed the steps on [Ref3]([Ref3]) to the T. Use the link on [Ref3]([Ref3]) to download the latest version of Win32DiskImager. Unzip it and and run it as administrator. If you don't run it as admin it will give you some permission error.

### Step 3: Load your micro SD card with OS
Select the letter corresponding to the micro SD card drive on the right hand side of the Win32DiskImager window and select the unzipped image file (.img) from step 1. Press write. Sit back and relax, this should be done in a few minutes depending on your system.

At the end you should get a message that suggests write successful.

If you see this you are done. I have did not face issue with this so if you find some issues do let me know. The OS will take up around 3 GB space. It is advised to use a 8 GB card so you have ample space to save your stuff. Some blogs say it even works with 32 GB cards, I cannot confirm that. I have used 16 GB and that works.

### Step 4: Connect the peripherals 
![alt text](https://raw.githubusercontent.com/officiallytech/officiallytech.github.io/master/images/_posts/01_2016/box.JPG "Boxed")

Unbox the raspberry pi.

![alt text](https://raw.githubusercontent.com/officiallytech/officiallytech.github.io/master/images/_posts/01_2016/unbox.JPG "Unboxed")

Connect the peripherals 2 to 6 from the list. 
DO NOT SWITCH ON POWER.

![alt text](https://raw.githubusercontent.com/officiallytech/officiallytech.github.io/master/images/_posts/01_2016/connected.JPG "Connected")

One weird thing that I experienced while inserting the micro SD card is that the card does not go entirely inside the slot. There are 2 states the card stays in the slot one where the card is little outside than the other. Image below. First I thought it did not fit well, so I surfed through a few videos to check and found that that's how it is suppose to be.

![alt text](https://raw.githubusercontent.com/officiallytech/officiallytech.github.io/master/images/_posts/01_2016/incorrect.jpg "Incorrect")

Incorrectly inserted SD card.

![alt text](https://raw.githubusercontent.com/officiallytech/officiallytech.github.io/master/images/_posts/01_2016/correct.jpg "Correct")

Correctly inserted SD card.

It will not fit snugly and will pop out a little.

### Step 5: Fire it up

Once everything is connected, I think it you to fire up the pi.

There are 2 lights that you have to look at after the power up.
The RED light denotes the power the board is powered and the GREEN light shows the state of internet connectivity.

![alt text](https://raw.githubusercontent.com/officiallytech/officiallytech.github.io/master/images/_posts/01_2016/start.JPG "Fired Up")

Start Up screen.

![alt text](https://raw.githubusercontent.com/officiallytech/officiallytech.github.io/master/images/_posts/01_2016/internet.JPG "Connected to the internet")

Connected to the internet.

You are ready to experiment.

### *References:*
[Ref1]:https://www.raspberrypi.org/downloads/raspbian/
[Ref2]:https://www.raspberrypi.org/documentation/installation/installing-images/windows.md
[Ref3]:https://www.raspberrypi.org/documentation/installation/installing-images/README.md
[Ref4]:https://www.raspberrypi.org/documentation/installation/installing-images/windows.md

*Ref1:* https://www.raspberrypi.org/downloads/raspbian/

*Ref2:* https://www.raspberrypi.org/documentation/installation/installing-images/windows.md

*Ref3:* https://www.raspberrypi.org/documentation/installation/installing-images/README.md

*Ref4:* https://www.raspberrypi.org/documentation/installation/installing-images/windows.md
