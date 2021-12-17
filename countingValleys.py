Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def countingValleys(steps, path):
    # Write your code here
    up= []
    down=[]
    first=[]
    count=0
    for i in path:
        if i == 'U':
            up.append(i)
            if len(first)==0:
                first.append(i)
        if i != 'U':
            down.append(i)
            if len(first)==0:
                first.append(i)    
        if len(up) == len(down) and bool(first):
            if first[0]=='D':
                count +=1
            up,first,down = [],[],[]
        
    return count 