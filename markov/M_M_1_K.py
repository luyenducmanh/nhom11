class M_M_1_K(object):
    """description of class"""
    def __init__(self, b, c, d):
        self.x = float(b)
        self.y = float(c)
        self.k = int(d)

    def P(self):
        return self.x/self.y
    
    def P0(self):
        if self.P() != 1:
            return (1 - self.P())/(1 - self.P()**self.k + 1)
            
        elif self.P() == 1:
            return 1/(self.k + 1)


    def L(self):
        """Average Customers in System"""
        if self.P() != 1:
            temp = 1 + (self.k * self.P()**(self.k + 1)) - (self.k + 1)*self.P()**self.k
            return self.P()*temp/((1 - self.P())*(1 - self.P()**(self.k + 1)))
        elif self.P() == 1:
            return self.k/2

    def Lq(self):
        """Average Customers in Queue"""
        if self.P() != 1:
            temp = self.P()*(1 - self.P()**(self.k))
            return self.L() - (temp/(1 - self.P()**(self.k + 1)))
        elif self.P() == 1:
            return self.k*(self.k - 1) / (2*(self.k + 1))

    def W(self):
        """Average Time Spent in System"""
        return self.L()/(self.x*(1 - self.PK()))

    def Wq(self):
        """Average Time Waiting in Line"""
        return self.W() - 1/self.y;

    def PK(self):
        
        return self.P()**self.k*self.P0()


