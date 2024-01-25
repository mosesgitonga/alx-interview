#!/usr/bin/env python3.10
import sys


    
def count_status_type(func):
    """
    counts the number of status
        eg: if status 401 appears 3 times in 
            the live streamed data the count becomes 3
    """
    count_401, count_400, count_404, count_200, count_301 =  0, 0, 0, 0, 0
    count_403, count_500 = 0, 0
    

    def wrapper(*args, **kwargs):
        nonlocal count_200, count_301, count_401, count_400, count_404
        nonlocal count_403, count_500

        res = func(*args, **kwargs)

        if res == '200':
            count_200 += 1
        elif res == '301':
            count_301 += 1
        elif res == '401':
            count_401 += 1
        elif res == '400':
            count_400 += 1
        elif res == '404':
            count_404 += 1
        elif res == '403':
            count_403 += 1
        elif res == '500':
            count_500 += 1
        
        return res, count_401, count_400, count_404, count_200, count_301, count_403, count_500

    return wrapper

@count_status_type
def status(status_code):
    return status_code


        
def log_parse():
    try:     
        for i, ln in enumerate(sys.stdin, start=0):
            line = ln.strip()
            sections = line.split()
            status(sections[-2])
            status_code, count_401, count_400, count_404, count_200, count_301, count_403, count_500 = status(sections[-2])

            if status_code == '200':
                print(f'{status_code}: {count_200}')
            elif status_code == '301':
                print(f'{status_code}: {count_301}')
            elif status_code == '401':
                print(f'{status_code}: {count_401}')
            elif status_code == '400':
                print(f'{status_code}: {count_400}')
            elif status_code == '404':
                print(f'{status_code}: {count_404}')
            elif status_code == '403':
                print(f'{status_code}: {count_403}')
            elif status_code == '500':
                print(f'{status_code}: {count_500}')


    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    log_parse()