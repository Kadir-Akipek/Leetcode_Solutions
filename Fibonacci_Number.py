#Recursive
class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        else:
            return self.fib(n-1) + self.fib(n-2)

#Iterative
class Solution:
    def fib(self, n: int) -> int:
        x,y = 0,1

        for i in range(n):
            x,y = y,x+y

        return x