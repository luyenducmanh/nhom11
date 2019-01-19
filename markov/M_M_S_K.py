import math

class M_M_S_K(object):
    """description of class"""
    def __init__(self, a, b, c, d):
        self.num_sever = int(a)
        self.x = float(b)
        self.y = float(c)
        self.k = int(d)
        self.r = self.x/self.y
        
    def P(self):
        return self.x/(self.num_sever * self.y)
        
    def P0(self):
        sum = 0
        temp = self.r**self.num_sever/math.factorial(self.num_sever)
        for i in range(0,self.num_sever):
            sum += self.r**i/math.factorial(i)

        if self.P() != 1:
            return sum + temp * (1 - self.P()**(self.k-self.num_sever+1)/(1-self.P()))
        elif self.P() == 1:
            return sum + temp * (self.k-self.num_sever+1)
    
    def L(self):
        """Average Customers in System"""
        sum = 0
        for i in range(0,self.num_sever):
            sum += (self.num_sever - i)*(self.P()*self.num_sever)**i/math.factorial(i)

        return self.Lq() + self.num_sever - self.P0()*sum

    def Lq(self):
        """Average Customers in Queue"""
        sum = 0
        for i in range(self.num_sever + 1 , self.k + 1):
            sum += i - self.num_sever
        return sum

    def W(self):
        """Average Time Spent in System"""
        return self.Wq() + (1/self.y);

    def Wq(self):
        """Average Time Waiting in Line"""
        return self.Lq()/self.x;

    def PK(self):
        sum = 0
        for i in range(self.num_sever + 1 , self.k + 1):
            sum += (i - self.num_sever)*(self.x**i)/(self.num_sever**(i - self.num_sever)*math.factorial(self.num_sever)*self.y**i)
            
        return sum;

