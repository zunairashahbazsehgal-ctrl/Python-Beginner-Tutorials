# practicing recursion code

def counter(n):
    if (n == 0):
       return 
    print(n)
    counter(n -1)
counter(4) # 1 2  3 4


# trying with loop

print()
print()
print()
print()
print()


def counter(n):
 for i in range(1, n):
   print(i)
counter(12)
print()
counter(13)

