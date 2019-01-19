import math

class M_M_1(object):
    """description of class"""
    def __init__(self, a, b):
        self.x = float(a)
        self.y = float(b)

    def P(self):
        return self.x/self.y

    def L(self):
        """Average Customers in System"""
        return self.P()/(1-self.P())

    def Lq(self):
        """Average Customers in Queue"""
        return self.L()*self.P()
    
    def W(self):
        """Average Time Spent in System"""
        return self.L()/self.x

    def Wq(self):
        """Average Time Waiting in Line"""
        return self.Lq()/self.x;
    
    def P0(self):
        return 1 - self.P()
    
    def PN(self):
        return self.P0()*self.P**2;
    

