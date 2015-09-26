# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 13:52:48 2015

@author: stoimenoff
"""
class Sorting:

    # Sorts a sequence of integers.
    def sort(self, sequence):
        sorted_sequence = [sequence[0]]
        for index in range(1, len(sequence)):
            for index_of_sorted in range(0, len(sorted_sequence)):
                if sequence[index] <= sorted_sequence[index_of_sorted]:
                    sorted_sequence.insert(index_of_sorted, sequence[index])
                    break
                if index_of_sorted == len(sorted_sequence) - 1:
                    sorted_sequence.append(sequence[index])
        return sorted_sequence
