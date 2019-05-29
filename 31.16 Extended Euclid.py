def Ext(a,b):
    """ algorithme d'Euclide étendu. Les nombres a at b doivent être des entiers naturels. L'algorithme renvoie d=pgcd(a,b) et des entiers x et y tels que d=xa+yb."""
    if b==0:
        return(a,1,0)
    else:
        (D,X,Y)=Ext(b,a%b)
        Q=a//b
        return((D,Y,X-Y*Q))