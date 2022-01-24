msg= 'Python  Week3  split  and  join'
csv='Robert, Blackwell, 2002, Spiderman, Software Engineer, Baltimore, Maryland'
tup_list = ['Robert','Blackwell','2002''Spiderman','Software Engineer','Baltimore, Maryland']

print(list(msg))


print(msg.split())


print(msg.split(' ')), print(msg.split(' '))


print(csv.split(','))


print('-'.join(tup_list))


print('-'.join(tup_list + tup_list))


print(''.join(tup_list))

