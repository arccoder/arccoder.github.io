---
layout: post
title: Post code on blogger from source file
category: Tech
tags: [blogger, C#]
---

I have a blog Code Sangraha where I post usually C++ implementations. Everytime I have to post a implementation I have to do it manually to get the syntax highlighting. It was a tedious process to  copy the code from visual studio to a word file and then to the blogger editor. This caused a lot of issues in the indentation of the code on the blogger.

I was looking for a automated or a semi automated way to post the code directly from the cpp file to the blog. Before starting work on a non manual process to post code on the blog, it was essential to find a cpp to html format converter. Some sort of library in which I could read the code from a text file and prefix and postfix a html tag.

[Syntax Highlighter](http://alexgorbatchev.com/SyntaxHighlighter/) seems to be one of the best know code highlighters which provided such an option, but for some reason I wasn't able to get it working. After a lot of research on an alternative to syntax highlighter which also involved implementing a preliminary python based code highlighter myself, I came across [google-code-prettify](https://code.google.com/p/google-code-prettify/) and it worked in the first go and gave pretty good results (other than the border around the code). Therefore I decided to go with this library.

Now coming to the point of actually posting a blog. On that aspect the [Google-Data API](https://code.google.com/p/google-gdata/downloads/detail?name=Google_Data_API_Setup_2.2.0.0.msi) works perfectly and as I am more familiar with Microsoft development environment I choose to use C# to build a executable with command line. The sample code found in [ConsoleSample.cs](https://google-gdata.googlecode.com/svn/trunk/clients/cs/samples/blogger/ConsoleSample.cs) explains ways to log into a blog, select a blog, post a blog and update a blog. I choose to go with a command line interface cause I find it easy to use and probably anyone who writes code would be able to figure it out.

_Code2Blogger_ usage

Code2Blogger -[OPTIONS] Arguments
-[OPTIONS]
-h or -help          Shows how to use Code2Blogger Application
-u                         Email ID / Username of the blogger account
-p                         Password of the blogger account
-b                         Blog ID for the blog
-t                          Name / Title of the blog to be posted
-a                         Name of the author
-i                          Path to the code file
Currently supports only one file at a time
-o                         Path to the file containing the codes output

To find your Blog ID
- Log into your blogger account and open the dashboard of your blog
- In the URL you should find your 18 digit blog id
- https://www.blogger.com/blogger.g?blogID=XXXXXXXXXXXXXXXXXX#overview/src=dashboard

[**{source code}**](https://bitbucket.org/akshay_chavan/code2blogger/src)

Command line usage

-u    youremailaddress    -b    yourblogid    -t    "BlogTitle"    -a    "Author"    -i    ../../source.file    -o    ../../output.txt
