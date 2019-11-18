# 1xn numpy array of Conns
from builtins import range
from builtins import object
import numpy

class Conn(object):

    def __init__(self,w,d):
        self.w = float(w)
        self.d = float(d)


n=int(1e7)

l = [None]*n
for i in range(n):
    l[i] = Conn(1.0,1.0)
A = numpy.array(l)
del l

while True:
    pass
