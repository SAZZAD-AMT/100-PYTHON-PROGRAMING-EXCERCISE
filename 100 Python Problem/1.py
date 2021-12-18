# link of all : https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt?fbclid=IwAR2XKByzol8mRQnV30gOyEjBsIdnG7-JrHyuwZcGNvFwn6ZuUljXNuiaAZo


l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print (','.join(l))