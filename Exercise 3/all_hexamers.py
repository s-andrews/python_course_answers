#!python

bases = ['G','A','T','C']

hexamers = bases.copy()

for _ in range(5):
    extended = []

    for start in hexamers:
        for base in bases:
            extended.append(start+base)

    hexamers = extended


for i,hexamer in enumerate(hexamers):
    print(i,hexamer)

