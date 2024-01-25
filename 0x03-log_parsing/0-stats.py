#!/usr/bin/python3
"""
log parsing
"""
import sys


try:
    mydict = {}
    size = 0
    for i, ln in enumerate(sys.stdin, start=0):
        line = ln.strip()
        sections = line.split(" ")
        size += int(sections[-1]) 
        if sections[-2] in mydict:
           mydict[sections[-2]] += 1
        else:
            mydict[sections[-2]] = 1
        
        mydict = dict(sorted(mydict.items()))
        
        if i % 10 == 0:
            print(f'File size: {size}')
            for key, value in mydict.items():
                print(f'{key}: {value}')

except KeyboardInterrupt:
    pass
finally:
    print("File size: {}".format(total_size))
    for key, val in my_dict.items():
        print("{}: {}".format(key, val))
