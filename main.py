import numpy as np

a=([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
b=([[1,2,3,4],[1,2,3,4],[9,2,3,0],[1,2,3,4]])
mtrx1=np.array(a)
mtrx2=np.array(b)
print(type(mtrx1))

class Mtrx_manip(object):

    def __init__(self, mtrx1, mtrx2):
        self.mtrx1 = mtrx1
        self.mtrx2 = mtrx2

    def add_matr(self, res):
        mtrx1rsh = mtrx1.reshape(4, 4)
        mtrx2rsh = mtrx2.reshape(4, 4)
        res = mtrx1rsh + mtrx2rsh
        print(res)

    def __add__(self, other):
        return self.mtrx1 + other.mtrx

    def minus_matr(self, got):
        mtrx1rsh = mtrx1.reshape(4, 4)
        mtrx2rsh = mtrx2.reshape(4, 4)
        res = mtrx1rsh + mtrx2rsh
        got = mtrx1 - mtrx2
        print(got)

    def __sub__(self, other):
        return self.mtrx2 - other.mtrx

    def increase_nmb(self,rcvd):
        rcvd = np.multiply(mtrx1, c)
        rcvd = np.multiply(mtrx2, c)
        print(rcvd)

    def incr_incr(self, rec):
        if len(mtrx1[0])==len(mtrx2):
            rec = mtrx1.dot(mtrx2)
            print(rec)
            rec = mtrx2.dot(mtrx1)
            print(rec)
        else:
            pass

    def transpose(self):
        mtrx1=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
        print(mtrx1.transpose())

a=([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
b=([[1,2,3,4],[1,2,3,4],[9,2,3,0],[1,2,3,4]])
mtrx1=np.array(a)
mtrx2=np.array(b)
c = 8
Mtrx_manip.add_matr(mtrx1, mtrx2)
Mtrx_manip.minus_matr(mtrx1, mtrx2)
Mtrx_manip.incr_incr(mtrx1, mtrx2)
Mtrx_manip.increase_nmb(mtrx1, c)
Mtrx_manip.transpose(mtrx1)

