def replaceChar(s, a, b):                          #Replace a character "a" with character "b"
    if len(s)==0:
        return s
    if s[0]!=a:
        return (s[0]+replaceChar(s[1:],a,b))
    else:
        return (b+replaceChar(s[1:],a,b))

#-----------------------------------------

def removeChar(s,a):                              #Remove a character "a"
    if len(s)==0:
        return s
    if s[0]==a:
        return removeChar(s[1:],a)
    else:
        return s[0]+removeChar(s[1:],a)

#-----------------------------------------

def replacePi(s):                                  #replace "pi" with "3.14"
    if len(s)==0 or len(s)==1:
        return s
    if s[0]=="p" and s[1]=="i":
        return "3.14"+replacePi(s[2:])
    else:
        return s[0]+replacePi(s[1:])

#-----------------------------------------

def removeDup(s):                                  #Removing duplicates
    if len(s)==0 or len(s)==1:
        return s
    if s[0]!=s[1]:
        return s[0]+removeDup(s[1:])
    else:
        return removeDup(s[1:])

#-----------------------------------------

def hanoiTower(n,a,b,c):                          #Print steps to create a Hanoi Tower
    if n==0 or n==1:
        print (a + c)
        return
    hanoiTower(n-1,a,c,b)
    print(a+c)
    hanoiTower(n-1,b,a,c)
