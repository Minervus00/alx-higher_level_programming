#!/usr/bin/python3
x, y = str(1).translate({49: None}), chr(10)
list(map(lambda j: print(chr(j), end=(x, y)[j == 90]), range(65, 91)))
