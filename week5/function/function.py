#Step 1

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


#Step 2

def Count_my_Letters(s):
    car={"UPPER_CASE":0, "LOWER_CASE":0}
    for truck in s:
        if truck.isupper():
           car["UPPER_CASE"]+=1
        elif truck.islower():
           car["LOWER_CASE"]+=1
        else:
           pass
    print ("Count_my_Letters: ", s)
    print ("No. of Upper case characters : ", car["UPPER_CASE"])
    print ("No. of Lower case Characters : ", car["LOWER_CASE"])

Count_my_Letters('Do What You Have to Do to Get Where You Want to Go!')