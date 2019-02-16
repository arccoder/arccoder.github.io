---
layout: post
title: Comment lines with a pattern in multiple files using regex in notepad++ 
category: Tech
tags: [How-to, Notepad++, Regex]
---

If you ever had to comment lines in source code with a particular pattern there is a easier way to do that using regular expression in notepad++.

Open the replace dialog box using `Ctrl+H`.

To comment lines with a "pattern" type `^(.*pattern.*)` in the "Find what" text box, where `^` references to the beginning of the line in which the "pattern" exists. [[1]]

Add comment tags `//\1` in the "Replace with" text box, where `\1` is a reference to the first bracketed expression. [[1]]

You can add any comment tags you like `//` for c++ or `#` for python.

Make sure you select the "Regular Expression" radio button as the "Search Mode".

Finally click "Replace All"

![Replace using notepad](/resources/posts/11-2017/notepad-replace.jpg)

If you want to comment lines with the same pattern in multiple files you should open all the files in notepad++ and click "Replace All in All Openned Documents".

Here I have used notepad++. You can use any other software the supports regex to accompolish the same thing.

[1]:https://www.regular-expressions.info/backref.html
