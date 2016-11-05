---
layout: post
title: Compute Integral Image in C++
category: Tech
tags: [C++, Algorithm]
---
**C++ Code**

```c++
#include 

using namespace std;

void integral(int *pIn, int widthIn, int heightIn, int *pOut)
{
    int i, j;
    int widthOt = widthIn + 1;
    int heightOt = heightIn + 1;
	
    for(i = 0; i <= heightIn; i++)
	*(pOut + (i*widthOt)) = 0;

    for(j = 0; j <= widthIn; j++)
	*(pOut + j) = 0;

    for(i = 0; i < heightIn; i++)
	for(j = 0; j < widthIn; j++)
		*(pOut + ((i+1)*widthOt) + (j+1)) = *(pIn  + (i*widthIn) + j) +
						    *(pOut + (i*widthOt) + (j+1)) +
						    *(pOut + ((i+1)*widthOt) + j) -
						    *(pOut + (i*widthOt) + j);
}

void display(int *pIn, int widthIn, int heightIn)
{
    int i, j;
    for(i = 0; i < heightIn; i++)
    {
	for(j = 0; j < widthIn; j++)
	    cout << *(pIn + (i*widthIn) + j) << '\t';		
	cout << endl;
    }
}

int main()
{
    int * pOut = new int[25];
    int width = 4;
    int height = 4;

    int arr[16] = {1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7};
    int * pIn = arr;

    display( pIn, width, height);
    cout << endl << endl;
	
    integral( pIn, width, height, pOut);

    display( pOut, width+1, height+1);

    return 0;
}
```
**Output**

Input Image <br>
1 2 3 4 <br>
5 6 7 8 <br>
9 1 2 3 <br>
4 5 6 7 <br>

Integral Image <br>
0 0 0 0 0 <br>
0 1 3 6 10 <br>
0 6 14 24 36 <br>
0 15 24 36 51 <br>
0 19 33 51 73 <br>

**MATLAB Code**

```matlab
A
```

A = <br>
1     2     3 <br>
4     5     6 <br>
7     8     9 <br>

```matlab
cumsum(cumsum(A,1),2)
```

ans = <br>
1     3     6 <br>
5    12    21 <br>
12    27    45 <br>
