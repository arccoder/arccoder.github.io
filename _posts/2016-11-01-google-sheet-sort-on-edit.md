---
layout: post
title: How to sort columns while editing on the fly in Google Sheets 
category: Tech
tags: [How-to, Google-Apps-Script]
---

In the previous post [**How to create a button to sort columns in Google Sheets**](http://akshaychavan.com/blog/how-to-create-button-to-sort-columns-google-sheets/) we saw how you can sort a column with a click of a button.

Pushing a button to get things done is so not 2016. It would be great if the list sorts itself when you modify or add data to the column.

And its very simple to do that. Just add the sort code into the function named [onEdit()](https://developers.google.com/apps-script/guides/triggers/#onedit).

```javascript
function onEdit() {
  SpreadsheetApp.getActiveSheet().getRange(2,1,8,2).sort( {column: 2,ascending: true} );
  SpreadsheetApp.getActiveSheet().getRange(2,3,7,2).sort( {column: 4,ascending: true} );
  SpreadsheetApp.getActiveSheet().getRange(2,5,8,2).sort( {column: 6,ascending: true} );
}
```

Thats it you are done.

You may also check the range of the data that was edited by using `onEdit(e)` and depending on the range call a specific function.
