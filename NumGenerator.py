from random import randrange

outfile = open('numbers.in','w')
amount = 50000000
outfile.write(str(amount)+' ')
for x in range(amount):
    outfile.write(str(randrange(1,1000000)))
    outfile.write(' ')
