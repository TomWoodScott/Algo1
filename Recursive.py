"""
A recursive function is one which calls itself until some condition is met.

Factorials with recursion:
"""

def fact(n, total = 1):
    if n == 1: return total
    else: return fact(n-1, total = total * n)

# print(fact(5))

"""
show all - Permutations:
"""
def perm(string: str, pocket=""):
    if len(string) == 0:
        print(pocket)
    else:
        for i in range(len(string)):
            letter = string[i]
            front = string[:i]
            back = string[i+1:]
            concat = front + back
            perm(concat, letter + pocket)

print(perm("ABC"))

