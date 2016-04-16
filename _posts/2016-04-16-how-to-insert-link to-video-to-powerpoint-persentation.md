---
layout: post
title: How to insert a link to local video to a powerpoint persentation.
category: 
tags: [powerpoint, insert-video]
---

Its good to have a video in a presentation. It helps you convey your message efficiently. 

But you will see people providing ~103mb powerpoint file for 30 min presentation. Just because it has a ~100mb video inserted in it. Without the video the file would be about ~3mb which is a very protable size. 

You can always insert a video using an url but then you need to have a reliable internet connection to buffer the video during presenting. Plus if you happen to present at client corporate location you need to be connected to their guest network, which isn't always stong and before you can even connect you need to get through their firewall.

If you want to send the ~103mb presentation to people you probabaly cannot email it. So you need to make another presentation without the video and then maintaining the 2 presentations simultaneously with your last minute changes, that just gets tedious.

There is a quick and easy way to get around this problem by insertint a local video as a link or insert a link to the video (not an online url). 

You have to follow the same steps that you take to insert the video using graphical user interface (gui) with one small variation.

When you browse the file rather than selecting 'Insert' the file use the dropdown menu (on that same insert button) and select 'Link To File'. As you see in the images below.

**Insert video for PC**

![Insert video for PC](https://raw.githubusercontent.com/arccoder/arccoder.github.io/master/blog/images/_posts/04_2016/pptx_video_1.png)

**Insert link to video**

![Insert link to video](https://raw.githubusercontent.com/arccoder/arccoder.github.io/master/blog/images/_posts/04_2016/pptx_video_2.png)

You just have to make sure that the location of the video and the presentation does not change. Actually the link to the video is **absolute as well as relative**. If your video in a particular location on your machine when you inserted the link to the video and then you happen to move the video to the same folder as the presentation, the link will still work. But if powerpoint cannot find the video locally (same folder as the presentation) or in its original location (absolute path) the video won't work. The link would not work if you rename the video after the link was inserted.

A **best practice** is this case will be to keep the video in the same folder as the presentation and insert it. That way the entire folder becomes your presentation and if you really need to give someone the presentation with the video just zip up the folder. Guess what, the zip file will be of the same size as the presentation inserted in it. 

This avoids some redundant work to maintain 2 presentations and all your presentation content stay in one place.

**Reference:**

[Insert or link to a video stored on your PC](https://support.office.com/en-us/article/Insert-or-link-to-a-video-stored-on-your-PC-f4db9074-91cb-49fa-a82a-81835af6913d)


