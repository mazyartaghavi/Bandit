import numpy as np  #for generating random numbers

class Bandit: 
    def __init__(self, q, Q):
        self.q = q
        self.Q = Q
        self.n = 0
    
    def __str__(self): 
        return f"q:{self.q} | Q:{self.Q} | n:{self.n}"

    def pull(self): 
        return np.random.normal(self.q, 1)
    
    def update(self, r):
        self.n += 1
        self.Q = self.Q + (1.0/self.n)*(r - self.Q) 


class NSBandit: 
    def __init__(self, q, Q, alpha):
        self.q = q
        self.Q = Q
        self.n = 0
        self.alpha = alpha
    
    def __str__(self): 
        return f"q:{self.q} | Q:{self.Q} | n:{self.n}"

    def pull(self): 
        return np.random.normal(self.q, 1)
    
    def update(self, r):
        self.n += 1
        self.Q = self.Q + self.alpha*(r - self.Q) 







class GBandit: 
    def __init__(self, q, H):
        self.q = q
        self.H = H
        self.n = 0
    
    def __str__(self): 
        return f"q:{self.q} | H:{self.H} | n:{self.n}"

    def pull(self): 
        return np.random.normal(self.q, 1)
    
    def update(self, new_H):
        self.n += 1
        self.H = new_H
         

def simple_bandit(q): 
    return Bandit(q = q, Q = 0)

def optimistic_bandit(q, Q): 
    return Bandit(q = q, Q= Q)

def simple_gbandit(q): 
    return GBandit(q = q, H = 0)

def simple_nsbandit(q): 
    return NSBandit(q, Q=0, alpha=0.01)






