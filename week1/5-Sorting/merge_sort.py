# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 14:19:54 2015

@author: stoimenoff
"""
class Sorting:

    # Sorts a sequence of integers.
    def sort(self, sequence):
        if len(sequence) <= 1:
            return sequence
        first_half = self.sort(sequence[0:len(sequence)/2])
        second_half = self.sort(sequence[len(sequence)/2:])
        sorted_sequence = []
        while first_half != [] and second_half != []:
            if first_half[0] < second_half[0]:
                sorted_sequence.append(first_half[0])
                first_half.remove(first_half[0])
            else:
                sorted_sequence.append(second_half[0])
                second_half.remove(second_half[0])
        sorted_sequence += (first_half + second_half)
        return sorted_sequence
