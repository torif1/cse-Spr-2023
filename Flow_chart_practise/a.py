def clasify(n):
    lst=['rational number']
    if (n.is_integer()):
        lst.append('integer')
        if n>=0:
            lst.append('natural')
            if n==0:
                lst.append('0')
    return lst

def slope(a,b,c,d):
    if (a-c==0):
        return 'slope is 0'
    if (b-d==0):
        return 'slope undefined'
    else:
        slope=(a-c)/(b-d)
        return slope

def roots(a,b,c):
    if a==0:
        if b==0:
            return 'function is y={c}, no roots'
        else:
            num=-c/b
            return 'x={num}'
    else:
        d=b**2-4*a*c
        if d<0:
            return 'roots are imaginary'
        else:
            x1=(-b+d**1/2)/2*a
            x2=(-b-d**1/2)/2*a
            return 'roots are {x2} and {x1}'