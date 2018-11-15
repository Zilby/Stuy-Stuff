Usage: python writer.py <xres> <yres> <output fname> <script file>
Parsing -works- but is NOT recommended, because colors are sent as an array, and it's hard to specify a color in text (not going to repr() it or anything).
And it's not flexible enough to deal with the optional parameters for 2-color gradients...so scripting can only give you a single color.  Which is the default white.

On the other hand, to get pretty colors and actually do things...code it in main.
Use a dummy script file (a.txt is one).