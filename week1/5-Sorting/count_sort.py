# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 14:45:01 2015

@author: stoimenoff
"""
class Sorting:

    # Sorts a sequence of integers.
    def sort(self, sequence):
        minEl = sequence[0]
        maxEl = sequence[0]
        for value in sequence:
            if value <= minEl:
                minEl = value
            if value >= maxEl:
                maxEl = value
        count_sequence = [0] * (maxEl - minEl + 1)
        for value in sequence:
            count_sequence[value - minEl] += 1
        sorted_sequence = []
        for index in range(0, len(count_sequence)):
            sorted_sequence += [index + minEl] * count_sequence[index]
        return sorted_sequence
        