def hanoi(n, s, t, b):
    if (n == 1):
        print s, "->", t 
    else:
        hanoi(n-1, s, b, t)
        hanoi(1,s,t,b)
        hanoi(n-1,b,t,s)
