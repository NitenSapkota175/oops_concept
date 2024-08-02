class Fraction:

    def __init__(self,n,d):
        self.num = n
        self.deno = d
        
        
    def __str__(self):
        return f"{self.num} / {self.deno}" 
    
    def __add__(self,other):
        
        new_num = self.num * other.deno + other.num * self.deno
        new_deno = self.deno * other.deno
        
        return f"{new_num} / {new_deno}"
    
    def __sub__(self,other):
        new_num = self.num * other.deno - other.num * self.deno
        new_deno = self.deno * other.deno
        
        return f"{new_num} / {new_deno}"
    
    
    def __mul__(self,other):
        
        new_num = self.num * other.num
        new_deno = self.deno * other.deno
        
        return f"{new_num} / {new_deno}"
    
    def __truediv__(self,other):
        
        new_num = self.num * other.deno
        new_deno = self.deno * other.num
        
        return f"{new_num} / {new_deno}"


        
        