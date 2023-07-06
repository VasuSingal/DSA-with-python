def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

#-----------------------------------------

def power(x,n):
    if n==0:
        return 1
    return x*power(x,n-1)

#----------------------------------------

def print_1_to_n(n):
    if n==0:
        return
    print_1_to_n(n-1)
    print(n)

#-----------------------------------------

def print_n_to_1(n):
    if n==0:
        return
    print(n)                    # I want n to print before calling the next fucntion only then the count will be reversed
    print_n_to_1(n-1)

#-----------------------------------------

def fibonnaci(n):               # Use iterative method for better solution
    if n==1 or n==2:            # two base cases required coz it is sum of two numbers
        return 1
    return fibonnaci(n-1)+fibonnaci(n-2)

print(fibonnaci(5))

#-----------------------------------------

def isSorted(a):               # isSortedBetter is also a way to check if the array is sorted or not
    l = len(a)
    if l==0 or l==1:
        return True
    elif a[0]>a[1]:
        return False
    else:
        a.pop(0)
        return isSorted(a)
    
#-----------------------------------------

def sum_of_n(a):
    l = len(a)
    if l==1:
        return a[0]
    else:
        return a.pop(0)+sum_of_n(a)

#-----------------------------------------

def check_number(a,n):
    if a[0]==n:
        return True
    a.pop(0)
    return check_number(a,n)

#-----------------------------------------

def isSortedBetter(a,si):               # using start index use preserve the original array whereas in the method above we end up deleting the array
    l = len(a)
    if si==l-1 or si==l:
        return True
    elif a[si]>a[si+1]:
        return False
    return isSortedBetter(a,si+1)

#-----------------------------------------

def firstIndex(a,x):                        #more space is required in this method because the list is getting copied and very time a new list is created
    l = len(a)
    if l==0:
        return -1
    if a[0]==x:
        return 0
    if firstIndex(a[1:],x)==-1:             #a[1:] creates a new list by coping 
        return -1
    else:
        return firstIndex(a[1:],x)+1

#-----------------------------------------

def betterFirstIndex(a,si,x):               # here we don't copy the list again n again instead use the same list with different start index
    l = len(a)
    if si==l:                               #if start index is same as length, that means list has ended and we have nothing to FIND FROM
        return -1
    if a[si]==x:                            #if at start index the value is same as the requested value we return the start index
        return si
    else:
        return betterFirstIndex(a,si+1,x)

#-----------------------------------------

def lastIndex(a,x):
    l = len(a)
    if l==0:
        return -1
    if lastIndex(a[1:],x)!=-1:
        return lastIndex(a[1:],x)+1
    else:
        if a[0]==x:
            return 0
        else:
            return -1

#-----------------------------------------

def betterLastIndex(a,x,si):
    l=len(a)
    if si==l:
        return -1
    if betterLastIndex(a,x,si+1)!=-1:
        return betterLastIndex(a,x,si+1)
    else:
        if a[si]==x:
            return si
        else:
            return -1

b = [1,2,3,4,3,7,3]

print(betterLastIndex(b,3,0))
