# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 12:46:49 2015

@author: stoimenoff
"""
def main():        
    target_sum = int(input())
    coins = [1,2,5,10,20,50,100]
    ways = [0] * (target_sum + 1)
    for coin in coins:
        if coin <= target_sum:
            ways[coin] += 1
        else:
            break
        for i in range(coin + 1, target_sum + 1):
            ways[i] += ways[i - coin]            
    print(ways[target_sum])
main()