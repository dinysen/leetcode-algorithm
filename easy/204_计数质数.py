"""
import math;
class Solution:
    def countPrimes(self, n):
        if n == 0 or n == 1 or n == 2:
            return 0;
        l = [x for x in range(2,n)];
        l_c = l[:];
        for i in l_c:
            if i**2 > n:
                break;
            if not i in l:
                continue;
            if self.isPrime(i):
                l = list(filter(lambda x : x % i != 0,l));
                l = [i] + l;
        return len(l);
        
    def isPrime(self,x):
        for i in range(2,math.floor(math.sqrt(x))+1):
            if x % i == 0:
                return False;
        return True;
"""

import math;
class Solution:
    def countPrimes(self, n):
        if n < 3:
            return 0;
        primes = [True]*n;
        primes[0] = primes[1] = False;
        for i in range(2,int(n**0.5)+1):
            if primes[i]:
                primes[i*i:n:i] = [False]*len(primes[i*i:n:i]);
        return sum(primes);