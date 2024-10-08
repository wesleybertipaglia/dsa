# platform: Code Wars
# title: Multiples of 3 or 5
# url: https://www.codewars.com/kata/514b92a657cdc65150000006

# description:
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
# Additionally, if the number is negative, return 0.
# Note: If the number is a multiple of both 3 and 5, only count it once.

def solution(number):
    sum_multiples = 0
    
    for num in range(3, number):
        if num % 3 == 0 or num % 5 == 0:
            sum_multiples += num
    return sum_multiples