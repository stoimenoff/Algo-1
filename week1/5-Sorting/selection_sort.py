# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 13:39:00 2015

@author: stoimenoff
"""
class Sorting:

    # Sorts a sequence of integers.
    def sort(self, sequence):
        for index in range(0, len(sequence)):
            minEl = sequence[index]
            minElIndex = index
            for second_index in range(index+1, len(sequence)):
                if sequence[second_index] < minEl:
                    minEl = sequence[second_index]
                    minElIndex = second_index
            swap = sequence[minElIndex]
            sequence[minElIndex] = sequence[index]
            sequence[index] = swap
        return sequence
