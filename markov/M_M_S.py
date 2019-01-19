import math

class M_M_S(object):
    """description of class"""
    def __init__(self, a, b, c):
        self.num_sever = int(a)
        self.x = float(b)
        self.y = float(c)

    def P(self):
        return self.x/(self.num_sever*self.y)

    def L(self):
        """Average Customers in System"""
        temp = (self.x*self.y*(self.x/self.y)**self.num_sever)/(math.factorial(self.num_sever-1)*((self.num_sever*self.y - self.x)**2))
        return temp*self.P0() + (self.x/self.y)

    def Lq(self):
        """Average Customers in Queue"""
        return self.L() - (self.x/self.y)

    def W(self):
        """Average Time Spent in System"""
        return self.L()/self.x;

    def Wq(self):
        """Average Time Waiting in Line"""
        return self.Lq()/self.x;

    def P0(self):
        """Server Utilization"""
        sum = 0
        temp = ((self.x/self.y)**self.num_sever*self.y*self.num_sever)/(math.factorial(self.num_sever)*(self.num_sever*self.y - self.x))
        for i in range(0,self.num_sever):
            sum += ((self.x/self.y)**i)/(math.factorial(i))

        return 1/(sum + temp)


        
    


