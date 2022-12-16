# n = int(input("Enter the number :\n"))
# for i in range(2,n + 1):
#     if n % i == 0:
#         count = 1
#         for j in range(2,(i//2 + 1)):
#             if(i % j == 0):
#                 count = 0
#                 break
#         if(count == 1):
#             print(i)

def find_prime_facs(n):
  factors=[]
  c=2
  while n>1:
    if n%c==0:
      factors.append(c)
      n=n/c
      c=c-1
    c+=1
  return factors
print(find_prime_facs(120))
print(find_prime_facs(39))
# abstract duplication
def lcm(a , b):
  all=[]
  lcm=1
  new_a=[]
  for i in range(len(a)):
    if a[i] not in b  :
      new_a.append(a[i])
  all=new_a + b
  for x in all:
    lcm = lcm * x
  return lcm
print(lcm(find_prime_facs(120) ,find_prime_facs(39) ))

all = lcm(find_prime_facs(120) ,find_prime_facs(39) )
lcm=1

print('lcm is {}'.format(lcm()))
# print(lcm)

# print(find_prime_facs(3))
# print(find_prime_facs(12))
# print(find_prime_facs(39))
# print(find_prime_facs(120))
