# platform: HackerRank
# kit: Week Preparation Kit
# title: Plus Minus
# url: https://www.hackerrank.com/challenges/one-week-preparation-kit-plus-minus/

# description:
# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
# Print the decimal value of each fraction on a new line with  places after the decimal.

def plus_minus(arr):
    for item in arr:
        result = item / len(arr)
        print(result:6)