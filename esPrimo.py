def esPrimo(n):
    primo = True
    i = 2
    while(i<n//2):
        #print("Dividiendo ", n , " por " , i)
        if(n%2 == 0):
            primo = False
        i = i+1
    return primo