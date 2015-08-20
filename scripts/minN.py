import numpy as n, pylab as p


def minN(NZ=2):
    """Calculates the minimum number of nodes to have more graphs than atoms in the universe.
    
    NZ=2 # number of different edge types. E.g. a digraph as NZ=2
    Considered 10^80 to be the number of atoms in the universe"""
    delta_=1+4*160/(n.log10(2)*NZ)
    N=(1+delta_**0.5)/2
    return N

NZs=list(range(150))
minNs=tuple(minN(i) for i in range(150))
p.plot(NZs,minNs,"ro",label="real value")
p.plot(NZs,n.ceil(minNs),"bo",label="integer value")

p.xlabel("number of different edges")
p.ylabel("minimum number of nodes")
p.title(r"minimum number of nodes to have more graphs than the $10^{80}$ atoms in the universe ")
p.legend()
p.show()
