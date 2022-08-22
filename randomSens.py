import random

lowOrHigh=random.randint(1,3)
print(lowOrHigh)
if lowOrHigh == 1:
    newSens=random.uniform(0.01,2.00)
elif lowOrHigh == 2:
    newSens=random.uniform(0.01,2.00)
else:
    newSens=random.uniform(2.01,5.00)
print(newSens)
sensString=("{0:.2f}".format(newSens))
with open('sens.txt', 'w') as f:
    f.write(sensString)
