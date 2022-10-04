# n steps to top, can take 1 or two steps, how many distinct ways can you climb to the top?
# example n=2 --> 1+1=2 & 2=n  --> answer 2.

# every time we take a move we have two choices  either 1step or two, therefore a decision tree with time complexity 2^n (brute force).
# to solve, check every branch, if ends in 5 returne +1 if <5 next branch i.e. depth first search, to improve, cash result for specific values (Memoisation).



# starting at the base
class Solution:
    def climb_stairs(n: int) -> int:
        one, two = 1, 1

        for i in range(n-1):
            temp = one
            one = one + two
            two = temp

        return one

print(Solution.climb_stairs(n=400))