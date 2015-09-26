# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 12:40:31 2015

@author: stoimenoff
"""
class Peek:
    def __init__(self, id):
        self.id = id
        self.distance = float("inf")
    def __gt__(self, peek):
        return self.distance > peek.distance
    def __lt__(self, peek):
        return self.distance < peek.distance
    def __str__(self):
        return str(self.id) + " " + str(self.distance)

class VitoshaMap:
    def __init__(self, matrix, n):
        self.n = n
        self.matrix = matrix
    def calculate_lowest_distances(self, peek_id):
        distances = [float("inf")] * (self.n * self.n)
        visited = [False] * (self.n * self.n)
        distances[peek_id] = 0
        def lowest_distance_to_unvisited():
            lowest = float("inf")
            id = -1
            for i in range (self.n * self.n):
                if lowest > distances[i] and visited[i] == False:
                    lowest = distances[i]
                    id = i
            return id
            
        for k in range(self.n * self.n):
            current_peek = lowest_distance_to_unvisited()
            #print("current ", current_peek)
            visited[current_peek] = True
            i_curr = int(current_peek/6)
            j_curr = current_peek%6
            for i in range(i_curr - 1, i_curr + 2):
                for j in range(j_curr - 1, j_curr + 2):
                    if i < 0 or j < 0 or i >= self.n or j >= self.n:
                        continue
                    curr_to_ij = abs(self.matrix[i_curr][j_curr] - self.matrix[i][j]) + 1
                    if curr_to_ij + distances[current_peek] < distances[6*i + j]:
                        distances[6*i + j] = curr_to_ij + distances[current_peek]
            #print(distances)            
        return distances
        
def main():
    n = int(input())
    coords = [int(item) for item in input().split()]
    matrix = []
    for i in range(n):
        row = [int(item) for item in input().split()]
        matrix.append(row)
    v_map = VitoshaMap(matrix, n)
    distances = v_map.calculate_lowest_distances(coords[0]*6 + coords[1])
    print(distances[coords[2]*6 + coords[3]])
main()
    