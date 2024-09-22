# platform: HackerRank
# kit: Interview Preparation Kit
# title: Sock Merchant
# url: https://www.hackerrank.com/challenges/sock-merchant/

# description:
# There is a large pile of socks that must be paired by color. 
# Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

def sock_merchant(stock_list: list) -> int:
    color_count = {} # Red: 2, Blue: 1, Green: 1
    pairs = 0
    
    for sock in stock_list:
        if sock in color_count:
            color_count[sock] += 1
        else:
            color_count[sock] = 1
    
    for count in color_count.values():
        pairs += count // 2
    
    return pairs