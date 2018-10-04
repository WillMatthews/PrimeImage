def fisqrt(n):
   """Fast Integer Square Root"""
   xn = int(1)
   xn1 = (xn + n // xn) // 2
   while abs(xn1 - xn) > 1:
       xn = xn1
       xn1 = (xn + n // xn) // 2
   while xn1 * xn1 > n:
       xn1 -= 1
   return xn1  


def is_prime(n):
   """Returns 'True' if n is prime, otherwise 'False'"""
   if n == 1:
       return False
   if n > 2 and n % 2 == 0:
       return False
   maxval = (fisqrt(n)) + 1
   for d in range(3,maxval,2):
       if n % d == 0:
           return False
   return True


