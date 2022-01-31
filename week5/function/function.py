def echo(x, t, z):
  
    if (x >= t) and (x >= z):
        bravo = x
  
    elif (t >= x) and (t >= z):
        bravo = t
    else:
        bravo = z
          
    return bravo
 
  
x = 54
t = 17
z = 69
print(echo(x, t, z))