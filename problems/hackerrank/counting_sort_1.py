# platform: HackerRank
# kit: Week Preparation Kit
# title: Counting Sort 1
# url: https://www.hackerrank.com/challenges/one-week-preparation-kit-countingsort1/

# description:
# Quicksort usually has a running time of n*log(n), but is there an algorithm that can sort even faster? In general, this is not possible. 
# Most sorting algorithms are comparison sorts, i.e. they sort a list just by comparing the elements to one another. 
# A comparison sort algorithm cannot beat n*log(n) (worst-case) running time, 
# since n*log(n) represents the minimum number of comparisons needed to know where to place each element. For more details, you can see these notes (PDF).

# Another sorting method, the counting sort, does not require comparison. 
# Instead, you create an integer array whose index range covers the entire range of values in your array to sort. 
# Each time a value occurs in the original array, you increment the counter at that index. 
# At the end, run through your counting array, printing the value of each non-zero valued index that number of times.

def counting_sort(arr):
    result = [0] * 100
    for i in arr:
        result[i] += 1
    return result