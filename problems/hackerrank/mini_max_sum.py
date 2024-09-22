# platform: HackerRank
# kit: Week Preparation Kit
# title: Minimum Maximum Sum
# url: https://www.hackerrank.com/challenges/one-week-preparation-kit-mini-max-sum/

# description:
# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. 
# Then print the respective minimum and maximum values as a single line of two space-separated long integers.

def miniMaxSum(arr):
    arr.sort()
    min = sum(arr[:4])
    max = sum(arr[1:])
    print(min, max)