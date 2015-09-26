# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 14:59:49 2015

@author: stoimenoff
"""
class Sorting:

    # Sorts a sequence of integers.
    def sort(self, sequence):
        if len(sequence) <= 1:
            return sequence
        pivot = sequence[0]
        before_pivot = []
        after_pivot = []
        for value in sequence[1:]:
            if value <= pivot:
                before_pivot.append(value)
            else:
                after_pivot.append(value)
        before_pivot = self.sort(before_pivot)
        after_pivot = self.sort(after_pivot)
        return before_pivot + [pivot] + after_pivot
