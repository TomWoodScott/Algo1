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

# print(perm("ABC"))
"""
8 queens on a chess board with none targetting eachother
"""

class Fibi:

    """
    Fibinachi sequence with memoization
    """
    # basic
    def fib(n):
        if n<=2:
            return 1
        else: return Fibi.fib(n-1) + Fibi.fib(n+2)

    """
    Memoization
    """
    

    def fib1(n, memo_dict = {}):
        if n <= 2:
            return 1

        if n in memo_dict: 
            return memo_dict[n]

        else:
            num = Fibi.fib1(n-1) + Fibi.fib1(n-2)
            memo_dict[n] = num
            return num

print(Fibi.fib1(n = 200))

