def gp(n):                              #finding the sum of gp 
    if n==1:                            #n is not the number of termsbut the power of 2
        return 1.5                      #for n to be the number of terms change 1.5 to 1
    output = (1/2**(n))+gp(n-1)
    return output

#-----------------------------------------

def pallindrome(s,si,ei):                       #check if the entered string is a pallindrome or not
    if si==ei:                                   
        return "Yes"    
    if len(s)%2==0:                             #if the length of the string is even then the string cannot be a pallindrome
        return "No"
    else:
        if s[si]==s[ei]:
            return pallindrome(s,si+1,ei-1)
        else:
            return "No"

#-----------------------------------------

def sumOfDigits(n,si,ei):
    if si>=ei:
        return int(n[si])
    return int(n[si])+sumOfDigits(n,si+1,ei)

#-----------------------------------------

def multiplication(a,b):
    if a==1:
        return b
    if b==1:
        return a
    return a + multiplication(a,b-1)

#-----------------------------------------

def countZeros(n):
    if n//10 == 0 and n!=0:
        return 0
    if n==0:
        return 1
    ans = countZeros(n//10)
    if n%10 == 0:
        return ans+1
    return ans
