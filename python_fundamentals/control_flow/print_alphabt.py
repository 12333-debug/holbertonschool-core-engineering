#!/usr/bin/env python3
i=0

for i in range(ord('a'),ord('z')+1):
   
    if(i != ord('e') and i != ord('q')):
        print(chr(i), end="")
    i = i + 1
	