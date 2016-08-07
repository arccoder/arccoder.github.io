---
layout: post
title: Datepicker in Meteor
category: Tech
tags: [meteor, datepicker, jquery-ui]
---

I spent a week trying to get datepicker working in one of my meteor projects. After a preliminary search I found a few packages that show an easy way to add a date picker. But I was having a hard time adding a datepicker to a template and in my project the template was the one displaying elements in a list. Which means that I either had to add a datepicker dynamically for every element in the list or use one datepicker and access it from a number of places.

I was looking for examples for the later option which is where I spent a week, but no luck. Finally I found that most of these packages are based on jquery's datepicker package which allowed me to set a div `id = datepicker` without an input element as I had a separate text field to display the date.

Enough of this  discussion lets see some code on to implemet this and I guess thats what many of you reading this blog are interested in.

**Add jquery-ui package to your meteor app**

```bash
meteor add mrt:jquery-ui
```

or you can simply add `mrt:jquery-ui` in the packages file in .meteor folder.

**Add a div to html**

```html
<div id="datepicker"></div>
```

This does not needs to be in a template.

**Add a style sheet**

```html
<link rel="stylesheet" href="//code.jquery.com/ui/1.12.0/themes/base/jquery-ui.css">
```

You can add your custom style sheet as well.

I wanted to use this date picker from the buttons I added in the template for each element in the list.
For which I added an icon in the template.

```html
<i class="glyphicon glyphicon-calendar buttoncliked"></i>
```

Glyphicon's can be found in bootstrap. `glyphicon-calendar` inserted a calender icon. `buttoncliked` is the class assigned to the icon.

The date picker added is not initialized because of which nothing is displayed on the screen.
Once you intialize the date picker, a calender should show up on the screen.
So whenever the icon is clicked we will initialize the date picker.

```javascript
'click .buttoncliked': function(e) {
    e.preventDefault();
    $("#datepicker").datepicker({   // initializes the datepicker
        onSelect: function() {      // once a date is selected
            var dateAsObject = $(this).datepicker( 'getDate' ); //calls getDate method
            $(this).datepicker( 'destroy' );    // destroy the datepicker object
            // ...
            // Make use of the date object
            // ...
        }
    });
}
```

`$("#datepicker").datepicker({})` initializes the date.
As we have initialized the datepicker locally. We can access the date using `$(this).datepicker()`.
Implement the `onSelect` callback function.
`$(this).datepicker( 'getDate' );` gets the selected date.
`$(this).datepicker( 'destroy' )` destroys the datepicker object and so the calender displayed on the screen.

This way you can use one datepicker on your entire page from different initialization points.

You display the datepicker as an overlay on the page and block access to anything else on the page till a date is selected or the datepicker is closed.

**References:**

[How to get the date from jQuery UI datepicker](http://stackoverflow.com/questions/4919873/how-to-get-the-date-from-jquery-ui-datepicker)
