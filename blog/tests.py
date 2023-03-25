# from django.test import TestCase

# Create your tests here.
n = 10
a = 3
res = 0

res = a ** n
# print(res)           
# res = pow(a,n)


n = 10
a = 3
res = a
for i in range(n-1):
    res *= a
print(res) 

